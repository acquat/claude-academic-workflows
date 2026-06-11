---
paths:
  - "**/*.xlsx"
  - "submissions.md"
---

# Quality Gates & Scoring Rubric (form completeness)

## Thresholds

- **80/100 = Print** — form is complete and compliant; OK to print and sign.
- **90/100 = Hand off** — receipts attached, both currencies present, within the deadline, ledger row drafted.
- **95/100 = Excellence** — ledger updated, folder README written, exchange rate documented in the folder.

## Expense Claim Form (.xlsx)

| Severity | Issue | Deduction |
|---|---|---|
| Critical | Past the filing deadline (rule A4 / hard cap A5) | -100 |
| Critical | Missing or wrong budget/financement code | -50 |
| Critical | Missing/wrong identity fields | -30 |
| Critical | Total mismatch (sum of line items ≠ TOTAL cell) | -25 |
| Critical | **A subtotal or TOTAL cell is a formula or `None` instead of a hardcoded numeric value** | -25 |
| Critical | No receipt attached for a line item | -25 |
| Major | Non-home-currency line missing the converted amount | -15 |
| Major | Conversion not at the reference rate on the date of purchase | -10 |
| Major | Mission-purpose field empty or non-specific | -10 |
| Major | Date format inconsistent across line items | -5 |
| Minor | Folder README missing | -5 |
| Minor | Ledger row not yet drafted | -5 |
| Minor | Receipt filename non-descriptive (opaque UUID) | -2 |

## Ledger (`submissions.md`)

| Severity | Issue | Deduction |
|---|---|---|
| Critical | Row missing for a filed claim | -50 |
| Major | Status stale (Filed > 60 days, no Paid date) | -10 |
| Minor | Period field empty for a multi-period claim | -3 |

## Enforcement

- **Score < 80:** block the print step; list blocking issues.
- **Score < 90:** allow print, warn; list recommendations.
- User can override with explicit justification (e.g. "the admin contact pre-approved the informal receipt").

## Audit reports

Generated at submission time using `.claude/templates/submission-audit.md`. Save to `.claude/quality_reports/audits/YYYY-MM-DD_<folder-name>.md`.
