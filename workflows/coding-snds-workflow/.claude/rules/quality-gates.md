---
paths:
  - "**/*.sas"
  - "**/*.R"
---

# Quality Gates & Scoring Rubric (SNDS pipeline)

## Thresholds

- **80/100 = Save** — runs correctly, secure, reproducible from the header.
- **90/100 = Handoff/PR** — domain-correct, audited at every step, disclosure-safe.
- **95/100 = Manuscript-ready** — replication-grade.

## SAS scripts (.sas)

| Severity | Issue | Deduction |
|---|---|---|
| Critical | PII identifier written to a flat file / log / shared mount | -100 |
| Critical | Aggregate exported without a disclosure-control check (cell-size masking) | -100 |
| Critical | Identifier-class variable in any ODS output, title, footnote, or filename | -20 |
| Critical | Individual-scale output: row-per-patient/provider/facility table, one-mark-per-unit scatter, or per-unit effect vector | -20 |
| Critical | Exported cell/bin/plotted point below the export gate (≥ 11 units AND nonzero events, or DUA value) without masking/coarsening | -15 |
| Critical | Wrong date field in an Oracle filter (`EXE_SOI_DTD` instead of `FLX_DIS_DTD`) | -30 |
| Critical | Composite join missing a key (duplicate-row risk) | -30 |
| Critical | Sentinel date (`'01JAN1600'dt`) fed into date arithmetic | -25 |
| Critical | Claims table pulled at full-population scale (no cohort restriction) | -25 |
| Major | Missing `proc contents` verification after a `CREATE TABLE` | -10 |
| Major | Missing row-count / distinct-id check after a major data step | -5 |
| Major | Output-producing script missing the export-gate block (`*_export_annex` + PASS/FAIL log assertion) | -5 |
| Major | Masked table without secret secondaire (masked cell recomputable from margins/other tables) | -5 |
| Major | MIN/MAX (or outlier marks) in an exported summary table or box plot | -5 |
| Major | Rate/percentage exported with denominator or implied numerator below the gate; or 0%/100% cell on a sensitive characteristic | -5 |
| Major | Hardcoded threshold with no citation or `[CHOICE]` tag | -5 |
| Major | Estimates console-only (no `ods output`) | -10 |
| Minor | Missing/incomplete header block | -5 |
| Minor | Style inconsistency (indentation, date-constant format) | -2 |

## R scripts (.R)

| Severity | Issue | Deduction |
|---|---|---|
| Critical | Syntax error / does not run; or PII exported | -100 |
| Critical | Hardcoded absolute paths | -20 |
| Major | Missing `set.seed()` where randomness is used | -10 |
| Major | Merge with >5% unmatched, unexplained | -10 |

## Enforcement

- **< 80:** block. List blocking issues (security/disclosure first).
- **< 90:** allow save, warn.
- Security and disclosure violations are **never** overridable without an explicit, documented data-access justification.
