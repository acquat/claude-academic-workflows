---
paths:
  - "**/*.tex"
  - "scripts/**/*.R"
---

# Quality Gates & Scoring Rubrics (manuscript)

## Thresholds

- **80/100 = Save** — good enough to keep (working draft).
- **90/100 = Submission-ready** — ready to send to co-authors / submit.
- **95/100 = Excellence** — aspirational.

## Manuscript (.tex)

| Severity | Issue | Deduction |
|---|---|---|
| Critical | LaTeX compilation failure (3-pass + bibtex) | -100 |
| Critical | Unverified factual/numeric claim in prose (see `no-fabrication.md`) | -30 |
| Critical | Undefined citation / `??` cross-reference in the compiled PDF | -15 |
| Critical | Numeric claim outside replication tolerance (see `replication-protocol.md`) | -20 |
| Major | Notes-to-self left in compiled output (`\hl{}`, `\textcolor{orange}{}`, `% TODO`, `\begin{comment}`, `////`) | -15 |
| Major | Citation not logged in `lit_review.md` before use | -10 |
| Major | Overfull `hbox` > 10pt in a display | -5 |
| Minor | Notation inconsistent with the registry (`paper-writing-conventions.md`) | -5 |
| Minor | Abstract over the journal word limit | -3 |

## R / analysis scripts (.R)

| Severity | Issue | Deduction |
|---|---|---|
| Critical | Syntax error / script does not run | -100 |
| Critical | Hardcoded absolute paths | -20 |
| Major | Missing `set.seed()` where randomness is used | -10 |
| Major | Output table/figure not regenerated from current code | -5 |

## Enforcement

- **Score < 80:** block "done." List blocking issues.
- **Score < 90:** allow save, warn. List recommendations before submission.
- User can override with explicit justification.

## Quality Reports

Generated at completion using `.claude/templates/quality-report.md`. Save to `.claude/quality_reports/completions/YYYY-MM-DD_[task].md`.
