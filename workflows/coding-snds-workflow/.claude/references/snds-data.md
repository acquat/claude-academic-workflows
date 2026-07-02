# SNDS Data Reference (project-local)

> Your project's SNDS lookup table — read first by `sas-reviewer` and `/sds-doc`. Fill it in as you go
> so you don't re-fetch the same definitions every session. **Always cite a source** (a URL or your DUA).

## Identifier-class variables (PII — never export; see `rules/snds-data-security.md`)

| Variable | Meaning | Notes |
|---|---|---|
| `BEN_NIR_PSA` | Pseudonymised beneficiary id (DCIR) | identifier — enclave only |
| `BEN_NIR_ANO` / `BEN_IDT_ANO` | Anonymised beneficiary ids | identifier — enclave only |
| `NIR_ANO_17` | Beneficiary id in PMSI / chainage | identifier — enclave only |
| [add others] | | |

## Disclosure-control threshold (from your DUA)

- Minimum cell size for export: **[confirm and record the exact threshold from your data-access agreement]**.
- Until confirmed, the **safe-harbor default is ≥ 11 units per cell/bin/point** — the verified
  French health-data norm (ATIH/ScanSanté masking; CASD PMSI rule). Verbatim citations +
  CONFIRMED/UNCONFIRMED ledger: [`snds-export-rules.md`](snds-export-rules.md). Coding rules:
  `rules/export-compliance.md`. Pre-submission gate: [`snds-export-checklist.md`](snds-export-checklist.md).
- Référent answers (turnaround, formats, DCIR/CEPIDC thresholds — §5 of the rules doc):
  **[record here as they come in]**.

## Tables used in this project

| Table | Library | Grain | Key(s) | Notes |
|---|---|---|---|---|
| `ER_PRS_F` | ORAVUE | claim/encounter line | composite (see `sas-sql-conventions.md`) | partition key `FLX_DIS_DTD` |
| [add others, e.g. `ER_BIO_F`, `T_MCO…`, `IR_IMB_R`, `IR_BEN_R`] | | | | |

## Code lists / nomenclatures used

| Concept | Nomenclature | Codes | Source |
|---|---|---|---|
| [e.g. condition flag] | CIM-10 / ALD | […] | [dico-snds / paper] |
| [e.g. procedure] | CCAM | […] | |
| [e.g. biology test] | NABM | […] | |
| [e.g. drug] | ATC / CIP | […] | |

> ⚠️ **Audit every code in a clinical indicator list for billing-supplement status.** French
> nomenclatures (NABM, CCAM) mix genuine assays/procedures with **« cotations supplémentaires »**
> — billing supplements that add a fee to an act performed in a particular setting or context
> (e.g. a nosocomial-infection supplement). A supplement fires *mechanically with the care
> setting/acuity*, not with the clinical decision your indicator means to capture — including one
> in a "test performed" or treatment indicator contaminates it with case-mix, which is fatal when
> the indicator feeds an instrument or exposure measure. Check each code's libellé in the official
> nomenclature (dico-snds / ameli) and record the include/exclude decision + reason in this table.

## Authoritative sources (for `/sds-doc`)

- **dico-snds** (variable dictionary): <https://health-data-hub.shinyapps.io/dico-snds/>
- **Health Data Hub training repo:** <https://gitlab.com/healthdatahub/se-former-au-snds>
- **kwikly documentation** (structural overview): <https://documentation-snds.health-data-hub.fr/snds/cnam/formations/kwikly/>

## Project conventions / gotchas

<!-- Record reusable lookups and decisions here as you confirm them, each with a source. -->
