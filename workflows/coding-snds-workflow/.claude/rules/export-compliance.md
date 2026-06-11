---
paths:
  - "**/*.sas"
  - "**/*.R"
  - "draft/**/*.tex"
---

# Export Compliance — Write Outputs That Can Leave the Enclave

**Every output a script produces (table, figure, log, annex) is a candidate « sortie de
données » from the secure environment. Write it export-compliant BY CONSTRUCTION — a rejected
export costs days of review turnaround and may force a portal re-run.**

Authority: `.claude/references/snds-export-rules.md` (fully cited — verbatim quotes from the
arrêté/CNIL/ATIH/CASD primary sources, with a CONFIRMED/UNCONFIRMED ledger). Before an actual
export request, run `.claude/references/snds-export-checklist.md`. Record YOUR channel's
confirmed threshold in `.claude/references/snds-data.md`.

Legal frame (one line): only **anonymous** results may leave the SNDS environment (arrêté du
6 mai 2024 §4.5; CNIL MR-005 SEC-EXP-1/2/3; CNAM CGU v4.0 — full citations in the
reference doc). On the **CNAM portal** there is no published numeric gate — each export is
reviewed **case-by-case** by a security expert. On the **CASD channel**, the CASD « Règles de
confidentialité » guide IS the operative ruleset. The verified French health-data norm
(ATIH/ScanSanté masking; CASD PMSI rule) is **counts < 11 masked** — adopt it as the
**safe-harbor default** unless your DUA/référent confirms something else.

---

## The 10 coding rules

### 1. The ≥ 11 double gate (cells, bins, plotted points) — default
Every aggregated cell/bin/point in ANY output must rest on **≥ 11 individuals AND ≥ 11 events**
(deaths, hospitalizations, treated…) — or the event count is exactly 0. Applies to displayed
values AND recoverable ones (`N × rate` reveals the count; displayed categories imply their
complement). Put `%let min_cell = 11;` (or your DUA's confirmed value) at the top of every
output-producing script. ⚠️ Estimation-sample filters (e.g. "providers with ≥ 10 patients") are
NOT export gates — export gates apply to what is *shown*.

### 2. Aggregate first, suppress second, then secret secondaire
Prefer **coarser bins** (quintiles not deciles; broader age bands; pooled years) over masking.
If you must mask: replace the value with missing + a `MASKED` flag (display « S » or « <11 »),
and apply **secret secondaire** — with margins/totals present, mask **≥ 2 cells per affected
row/column** or drop the margin, so nothing is recomputable by sum/difference. Check across the
whole table *family* (tables sharing margins across an output set), not within one table only.

### 3. No individual-scale outputs — patients, providers, OR facilities
No row-per-patient / row-per-provider / row-per-facility ODS output. No scatter where one
mark = one unit (bin first: ≥ 11 units per plotted bin). Never output per-provider random/fixed
effects as a vector — distributional summaries only (variance components, ICC, decile cuts
computed over ≥ 11 providers per bin). **Health professionals are protected persons too** (HDH:
no « identifiants de personnes bénéficiaires ou professionnels de santé »).

### 4. No identifiers anywhere in outputs
`BEN_NIR_PSA`, `BEN_NIR_ANO`, `BEN_IDT_ANO`, `NIR_ANO_17`, `PFS_PRE_NUM`, `ETB_PRE_FIN`,
`ETA_NUM`, commune codes — never in ODS outputs, BY-group headers, TITLE/FOOTNOTE, filenames,
or annexes. Specialty × fine geography × volume crossings are potential identifiers — keep
geography at département or coarser unless your DUA says otherwise.

### 5. No MIN/MAX, no outliers
MIN/MAX are single-individual statistics. Exported summaries: `N MEAN STD MEDIAN P25 P75`
(P5/P95 acceptable; P1/P99 only if each tail ≥ 11 obs). Box plots without outlier points.

### 6. Rates and percentages
Export a rate only if **denominator ≥ 11 AND implied numerator ≥ 11 (or 0, masked)**. No 0 % /
100 % — and avoid ≳ 90 % quasi-unanimous — cells on sensitive characteristics within a
recognizable subgroup (non-inférence): coarsen until the cell diversifies.

### 7. Amount (€) cells: dominance check
For any exported €/volume aggregate: no single contributor (patient, provider, facility) may
account for **≥ 85 %** of the cell (dominance rule — confirmed for French business statistics,
adopted here by analogy). Emit the max-share per cell in the reviewer annex only.

### 8. Auto-emit the reviewer annex + export-gate check (mandatory step)
Every script with exportable outputs ends with an **export-gate block** that (a) writes
`<output>_export_annex` — per-cell/per-bin `N` and `N_EVENTS` for every figure/table — and
(b) asserts the gate in the log:

```sas
%let min_cell = 11;            /* safe-harbor default — see rules/export-compliance.md */

proc sql;                      /* annex: one row per plotted bin / table cell          */
  create table fig1_export_annex as
  select bin, count(*) as n_units, sum(event_flag) as n_events
  from analysis_sample
  group by bin;
quit;

proc sql noprint;              /* gate assertion — PASS/FAIL in the log                */
  select min(n_units),
         min(case when n_events > 0 then n_events end)
    into :min_n trimmed, :min_e trimmed
  from fig1_export_annex;
quit;
%put EXPORT-GATE fig1: min N=&min_n, min nonzero events=&min_e
     %sysfunc(ifc(&min_n >= &min_cell and &min_e >= &min_cell, PASS, FAIL — mask or coarsen));
```

R equivalent: `dplyr::count()` the plotted bins, `stopifnot(min(n) >= 11)` before `ggsave()`.
The annex ships with the export request (flagged "reviewer annex — not for publication"); it is
what lets the security reviewer approve quickly.

### 9. Figures and maps
Flat formats only (PNG/PDF inside RTF) — never formats embedding the data (SAS `.sge` editable
graphics, Stata LIVE `.gph`, RDS of the plot object, Excel with pivot caches). Histogram tail
bars are counts → same gate (merge tails). Maps: every shaded zone passes rules 1 & 6; failing
zones greyed out with a footnote; never the same indicator on two overlapping geographies
(differencing risk) without a check; per-zone count annex required.

### 10. Models, programs, logs — and the two-stream policy
Model tables always print **N + number of clusters/groups**; avoid saturated specifications
whose coefficients are recoverable cell means over < 11 obs. Exported programs must contain no
data (no hard-coded IDs, no pasted results in comments). **Raw logs are never exported** —
produce a clean run-summary instead. Titles/footnotes carry no IDs and no sub-threshold Ns.

**Two-stream policy.** Rules 1–9 bind the **EXPORT stream** only — files destined to leave the
enclave (`EXPORT_*` + `*_export_annex`). The **DIAG stream** (enclave-only) is exempt and
encouraged: full-detail diagnostics — small cells, MIN/MAX, per-provider detail, raw cell
grids, `%PUT`/`print()` — are fine **as long as they stay in the log/listing on the server**.
Label them `TITLE "ENCLAVE-ONLY DIAGNOSTIC — NOT FOR EXPORT";` (or a `DIAG_` file prefix) so
they can never slip into an export package.

---

## Common pitfalls (seen in real SNDS projects)
- A provider-level scatter (one dot = one prescriber/physician) — individual-scale data on a
  protected person; bin before plotting.
- `HAVING count(*) >= 5` (or 10) gates copied from methods papers — below the ≥ 11 norm.
- MIN/MAX columns left in default `PROC MEANS` output.
- Rare cause-of-death (or rare-comorbidity) count tables — mask + collapse into "Other", with
  secret secondaire across the table family.
- Event-study / DiD descriptives with very few facilities per cell (adopter-type × period).
- Age×sex×group standardization grids exported wholesale — export the standardized rates, keep
  the cell grid in the enclave; ship only `min cell N` in the annex.

## For `draft/**/*.tex` (paper writing)
Only export-approved numbers/figures enter the paper. Cite the data source (a CGU publication
obligation on the CNAM channel); nothing directly or indirectly identifying. A referee's finer
cut must itself clear these gates before a new export request.

## UNCONFIRMED items — do not improvise
Channel turnaround, allowed file formats, DCIR/CEPIDC-specific thresholds, facility-cell
minimums: ask YOUR data provider's référent (question list in
`references/snds-export-rules.md` §5) and record answers in `references/snds-data.md`.
**When in doubt: more suppression, not less.**
