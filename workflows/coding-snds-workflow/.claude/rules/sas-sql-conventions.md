---
paths:
  - "**/*.sas"
---

# SAS/SQL Conventions — SNDS (Oracle, secure portal)

> Examples below use a generic example cohort named `COND` (e.g. an ALD condition) — adapt table/column names to your project. The partition-key, join-key, safe-replace, and verification rules are SNDS-universal: keep them.

Conventions for all SAS programs operating on the SNDS Oracle database via the secure portal.

---

## 1. Macro Variable Conventions

All study parameters must be defined as `%let` at the top of every script — never hardcoded inline.

```sas
/* Standard macro block — copy to top of every script */
%let yr_start_full = 2010;
%let yr_end_full   = 2019;
%let yr_start      = 10;          /* 2-digit suffix for PMSI table names */
%let yr_end        = 19;
%let ald_code      = 14;          /* ALD 14 = chronic respiratory insufficiency */
%let min_prescriber_n = 10;       /* Minimum patient volume for LOO reliability */
%let outpath       = .;           /* Output directory — adjust per portal */
```

**Rationale:** The SNDS portal does not allow interactive editing. All parameters must be
auditable from the script header.

---

## 2. Oracle Date Filter — Critical Rule

**ALWAYS filter on `FLX_DIS_DTD`** when querying `ER_PRS_F` or `ER_BIO_F`.

```sas
/* CORRECT — uses Oracle partition key */
WHERE r.FLX_DIS_DTD >= "&claims_start"d
  AND r.FLX_DIS_DTD <= "&claims_end"d

/* WRONG — EXE_SOI_DTD is not the partition key; causes full table scan */
WHERE r.EXE_SOI_DTD >= "&claims_start"d   /* DO NOT USE */
```

`FLX_DIS_DTD` = date claim became available for processing (indexed partition key).
`EXE_SOI_DTD` = date care was provided (not indexed; triggers full table scan).

---

## 3. Standard SNDS Join Keys

### ER_PRS_F ↔ ER_BIO_F (9-key composite join)

```sas
ON  l.DCT_ORD_NUM = r.DCT_ORD_NUM
AND l.FLX_DIS_DTD = r.FLX_DIS_DTD
AND l.FLX_EMT_NUM = r.FLX_EMT_NUM
AND l.FLX_EMT_ORD = r.FLX_EMT_ORD
AND l.FLX_EMT_TYP = r.FLX_EMT_TYP
AND l.FLX_TRT_DTD = r.FLX_TRT_DTD
AND l.ORG_CLE_NUM = r.ORG_CLE_NUM
AND l.PRS_ORD_NUM = r.PRS_ORD_NUM
AND l.REM_TYP_AFF = r.REM_TYP_AFF
```

All 9 keys are required. Omitting any key produces duplicate rows.

### IR_IMB_R ↔ IR_BEN_R (ALD to demographics)

```sas
ON  l.BEN_NIR_PSA = r.BEN_NIR_PSA
AND l.BEN_RNG_GEM = r.BEN_RNG_GEM
```

### DCIR ↔ PMSI (via chainage table)

```sas
/* cond_ben → T_MCOaaC → T_MCOaaB → T_MCOaaE */
INNER JOIN oravue.T_MCO&yy.C AS c
    ON p.BEN_NIR_PSA = c.NIR_ANO_17   /* Bridge: NIR_ANO_17 = BEN_NIR_PSA in chainage */
WHERE c.NIR_RET = '0'
  AND c.NAI_RET = '0'
  AND c.SEX_RET = '0'    /* Quality filters: accept only clean linkages */
```

---

## 4. Table Naming Conventions

| Prefix | Usage |
|--------|-------|
| `ORAUSER.cond_*` | Cohort-construction stages |
| `ORAUSER.prescriber_*` | Instrument-construction stage |
| `_v2` suffix | Safe-replace intermediary; verified before original is dropped |

Never use work library for tables that need to survive step boundaries in long scripts.

---

## 5. Safe Drop/Replace Pattern

```sas
/* Step N output */
proc sql;
CREATE TABLE ORAUSER.my_table_v2 AS
SELECT ...;
quit;

%macro safe_replace;
    %if %sysfunc(exist(ORAUSER.my_table_v2)) %then %do;
        proc sql;
        DROP TABLE ORAUSER.my_table;
        CREATE TABLE ORAUSER.my_table AS SELECT * FROM ORAUSER.my_table_v2;
        DROP TABLE ORAUSER.my_table_v2;
        quit;
    %end;
    %else %do;
        %put ERROR: my_table_v2 was NOT created. Original preserved.;
    %end;
%mend;
%safe_replace;
```

Use for any step that replaces an existing table. Oracle does not support `CREATE OR REPLACE TABLE`.

---

## 6. Leave-One-Out (LOO) Instrument Construction

Standard sum-and-subtract LOO — exact, avoids GROUP BY complications with PROC MEANS.

```sas
/* Step A: compute prescriber-year totals */
proc sql;
CREATE TABLE ORAUSER.prescriber_totals AS
SELECT PFS_PRE_NUM,
       CARE_YEAR,
       count(DISTINCT BEN_NIR_PSA) AS N_j,
       sum(TESTED_COND)            AS TOTAL_TESTED_COND,
       sum(TESTED_ALL)             AS TOTAL_TESTED_ALL
FROM ORAUSER.prescriber_pt_panel
GROUP BY PFS_PRE_NUM, CARE_YEAR;
quit;

/* Step B: join back and compute LOO */
proc sql;
CREATE TABLE ORAUSER.panel_with_loo AS
SELECT
    p.*,
    CASE WHEN t.N_j >= 2
         THEN (t.TOTAL_TESTED_COND - p.TESTED_COND) / (t.N_j - 1)
         ELSE .   /* Missing for singletons — expected; exclude from first stage */
    END AS Z_LOO_COND,
    CASE WHEN t.N_j >= 2
         THEN (t.TOTAL_TESTED_ALL - p.TESTED_ALL) / (t.N_j - 1)
         ELSE .
    END AS Z_LOO_ALL
FROM ORAUSER.prescriber_pt_panel AS p
INNER JOIN ORAUSER.prescriber_totals AS t
    ON  p.PFS_PRE_NUM = t.PFS_PRE_NUM
    AND p.CARE_YEAR   = t.CARE_YEAR
WHERE t.N_j >= &min_prescriber_n;
quit;
```

**Never** compute LOO by calling PROC MEANS with `BY` — it does not exclude self from the mean.

---

## 7. Verification Steps (Mandatory After Every CREATE TABLE)

```sas
/* After every CREATE TABLE — both steps required */
proc contents data=ORAUSER.my_table; run;

proc sql;
SELECT count(*)                    AS num_obs,
       count(DISTINCT BEN_NIR_PSA) AS n_patients  /* or relevant ID */
FROM ORAUSER.my_table;
quit;
```

For rate tables — add range check:

```sas
proc sql;
SELECT min(RATE_COND) AS rate_min,
       max(RATE_COND) AS rate_max,
       nmiss(Z_LOO_COND) AS n_loo_missing
FROM ORAUSER.prescriber_rate_indiv;
quit;
/* Expected: rate_min >= 0, rate_max <= 1, n_loo_missing = N singletons */
```

---

## 8. ODS Output Conventions

```sas
/* Open RTF */
ods rtf file="&outpath./output_filename.rtf" style=journal;
ods graphics on / width=6in height=4in;

/* Tables: use PROC TABULATE or PROC MEANS with ODS */

/* Histogram */
proc sgplot data=ORAUSER.prescriber_hist_data;
    vbar BIN_LABEL / response=N_PRESCRIBERS
         fillattrs=(color=CX4472C4)
         barwidth=0.9;
    xaxis label="Prescriber Testing Rate (COND-Relevant Tests)" values=(0 to 1 by 0.05);
    yaxis label="Number of Prescribers" grid;
    title "Distribution of Prescriber-Level Testing Intensity";
    title2 "COND Cohort 2010-2019 | Minimum 10 Patients per Prescriber";
run;

/* Close ODS — ALWAYS */
ods graphics off;
ods rtf close;
```

Style notes:
- Use `style=journal` (clean, publication-ready)
- Always set axis labels and informative titles
- Include sample size and date range in title2
- Color: `CX4472C4` (muted blue) as default for single-series bar charts

---

## 9. FICHSUP Table Guards

BPHNA/RIHNP/RIHND FICHSUP tables may not exist on all portals or for all years.

```sas
%if %sysfunc(exist(oravue.T_MCO&yy.SUP_BPHNA)) %then %do;
    /* Include this year in UNION ALL */
%end;
%else %do;
    %put NOTE: T_MCO&yy.SUP_BPHNA not found — skipping year &i;
%end;
```

Always check existence before referencing. A missing table causes a hard PROC SQL error.

---

## 10. PROC SQL in Oracle Context

- Prefer `count(DISTINCT col)` over `n(col)` for patient counts (Oracle handles it correctly)
- Use `datepart()` to extract date from datetime variables: `year(datepart(EXE_SOI_DTD))`
- Use `cats()` for string concatenation: `cats(SOR_ANN, SOR_MOI)` (no spaces)
- `CASE WHEN ... THEN ... ELSE ... END` works identically in PROC SQL and Oracle SQL
- Avoid `HAVING` with aggregated `CASE WHEN` — compute derived column in subquery first
- **Never `GROUP BY` an EXPRESSION against an Oracle table** (`group by year(x)`, `group by
  calculated col`, `group by substr(...)`) — it triggers a PROC SQL *remerge* that pulls the full
  table into WORK. Group by RAW columns; decode in a follow-up WORK DATA step.

---

## 11. Column types — VERIFY, don't assume (the silent-wrong-result trap)

DCIR/PMSI date and année-mois fields are NOT all the same type, and a literal of the wrong type fails
*silently* (matches nothing / everything) rather than erroring:

| Field family | Type | Filter literal |
|---|---|---|
| `FLX_DIS_DTD`, `EXE_SOI_DTD`, `*_DTD` (dates) | **DATETIME** (Oracle DATE; shows as DATETIME20.) | date literal `"01JAN2018"d` — correct ONLY under Oracle pushdown |
| `EXE_SOI_AMD`, `*_AMD` (année-mois) | **CHAR** `'YYYYMM'` | char literal `"201801"` (lexicographic = chronological) |

- A date literal vs a DATETIME column is correct only because it is **pushed to Oracle** (compared as
  an Oracle DATE). If a predicate is ever evaluated SAS-side, date(~21000) vs datetime(~1.8e9) →
  silent empty/garbage. Confirm pushdown with a one-period probe (prunes → minutes, not hours).
- `EXE_SOI_DTD > '01JAN2100'd` is the date-vs-datetime guard: a real datetime ≫ 51500, so it routes
  to `year(datepart(...))`.
- **Confirm every filter/join/group column's type with `dictionary.columns` / `proc contents` before
  writing the predicate — never from memory or a comment.**

## 12. Data-extraction pre-flight (MANDATORY before any portal submission of a pull script)

Portal scripts cannot be tested locally; a wrong query costs hours or silently poisons everything
downstream. **Structural/parse correctness is NOT correctness.** Before submitting:

1. **VERIFY column types** (§11) — don't assume.
2. **PROBE the partition/flux LAYOUT** (which `FLX_DIS_DTD` values exist; real monthly vs consolidated)
   with a committed `_diag_*` that RAN — never infer from a comment or "it worked before."
3. **RANGE, not exact-equality, on a date/partition key.** Sweep with a **half-open** range
   `WHERE FLX_DIS_DTD >= "&begin"d AND FLX_DIS_DTD < "&nextbegin"d` (gap-free, overlap-free,
   layout-agnostic). NEVER `= "single_date"d` — it silently collapses to a fraction if the layout
   differs from what was assumed.
4. **Flux window = care window + reimbursement lag (~6 months)** (claims surface at reimbursement);
   trim the care window via the char année-mois field (datetime-safe).
5. **BENCHMARK-GATE the output IN THE SCRIPT'S OWN LOG**: emit total rows + per-period counts and
   compare to a known benchmark (prior-run counts, or a published table). **A rewrite is not "done"
   until the counts match** — never ship on "it parses / looks right."
6. **Fail-fast** `%if &SQLRC >= 8 %then %abort` after every CREATE/INSERT; **drop large
   intermediaries** after their last consumer; header and code must agree on drops.

> The most expensive SNDS mistake class is the **silent wrong result** — an under/over-pull that
> parses cleanly. Items 1–5 exist to catch it. When in doubt, probe first.

---

## 13. DCIR régularisations — count acts by SUMMING the SIGNED quantity, never `COUNT(*)` lines

**The DCIR contains régularisation (annulation) lines: a billed act can be cancelled — and re-billed
— with a line *identical in care content but with a NEGATIVE quantity*, arriving in a LATER flux.
Counting rows (`COUNT(*)`) therefore over-counts and can count acts that never happened.** This is
official, documented behavior — verify before changing any count.

**Official rule (verbatim, [DCIR requête-type](https://documentation-snds.health-data-hub.fr/snds/fiches/sas_prestation_dcir)):**
> *« Dans les tables de prestations … il existe des lignes de régularisation. Elles correspondent à
> des annulations de prestations avec ou non enregistrement d'une nouvelle ligne … La ligne de
> régularisation est en tout point identique à la ligne initiale mais avec une quantité d'actes
> négative. En pratique, il faut donc **sommer les quantités des lignes identiques de prestations et
> ne garder que les lignes dont la somme est strictement positive**. »*

**Official netting GROUP BY** ([OMOP ETL — traitement préliminaire DCIR](https://documentation-snds.health-data-hub.fr/omop/documentation_etl/traitements_preliminaires/dcir_intermediaire)):
`ben_nir_psa, ben_rng_gem, exe_soi_dtd, ben_res_dpt, org_aff_ben, pse_spe_cod, psp_spe_cod, <code acte>`
→ `SUM(<quantité>)` → keep `> 0`. **Groups on the CARE date (`EXE_SOI_DTD`), NOT the flux key** —
that is how a cancellation in a later flux matches its original (the 9-key composite is the *unique
prestation-within-flux id* per the schéma relationnel, so it does NOT join a régularisation to its
original; there is no cross-flux "claim id").

**Quantity fields are genuine signed counts, not coefficients.** `BIO_ACT_QSN` = *« Quantité affinée
**signée** de biologie »* ([ER_BIO_F](https://documentation-snds.health-data-hub.fr/tables/er_bio_f/));
it is the quantity multiplier in the amount formula `coef(BTF_TAR_COF) × prix(BSE_REM_PRU) ×
BIO_ACT_QSN × taux` ([tables affinées](https://documentation-snds.health-data-hub.fr/snds/fiches/tables_affinees)).
The pricing coefficient is the *separate* `BTF_TAR_COF`. (`PRS_ACT_QTE` is the prestation-level
quantity — constant within a prestation, usually 1 — not the per-act count.)

**Empirically confirmed (biology tables, COND cohort):** a régularisation is overwhelmingly a
**reimbursement-RATE correction** (e.g. `−1` at taux 80% + `+1` at taux 100% in a later flux, same
`PFS_PRE_NUM`/specialty/act/care-date) — the act *did* happen, the billing rate was fixed. Of 947
negative-containing care-groups: 857 net `>0`, **42 net `=0` (true ghosts → drop)**, 48 orphan
negatives (original outside window → floor at 0). **941/947 share one `PFS_PRE_NUM`**, so netting
can keep the individual prescriber. Magnitude: line count 330,250 → netted quantity 327,909 (≈ 0.7%).

**House rule when a prescriber-IV design needs the prescriber** (dropped by the official patient-level grouping):
- Net at **`(BEN_NIR_PSA, BEN_RNG_GEM, EXE_SOI_DTD, BEN_RES_DPT, PSE_SPE_COD, PSP_SPE_COD,
  PFS_PRE_NUM, BIO_PRS_IDE)`**, `SUM(BIO_ACT_QSN)`, **keep net `> 0`** (drops ghosts, floors orphans).
- `N_TESTS_* = SUM(net BIO_ACT_QSN)` (NOT `COUNT(*)`); `TESTED_COND = (net COND quantity > 0)` (NOT
  `MAX(COND_RELEVANT_FLAG)`, which would mark a cancelled-only month as tested).
- Do this **upstream** (on `cond_bio`, before building the patient/provider panel) so ghost claims
  never reach any count or the modal-prescriber assignment.
- `ORG_AFF_BEN` is not in the key above; adding it gives exact official-recipe fidelity but is
  near-immaterial (care-groups are 99.9% single-affiliation). Exclude administrative bio codes
  upstream (`BSE_PRS_NAT` / act-code filter per your project).

**Fact-check sources** (all on `documentation-snds.health-data-hub.fr`): régularisation rule →
`/snds/fiches/sas_prestation_dcir`; netting keys → `/omop/documentation_etl/traitements_preliminaires/dcir_intermediaire`;
`BIO_ACT_QSN` → `/tables/er_bio_f/`; amount formula → `/snds/fiches/tables_affinees`.
