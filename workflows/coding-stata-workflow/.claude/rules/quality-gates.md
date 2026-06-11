---
paths:
  - "**/*.do"
  - "**/*.R"
---

# Quality Gates & Scoring Rubric (Stata pipeline)

## Thresholds

- **80/100 = Save** — runs clean, reproducible from a fresh session.
- **90/100 = Handoff** — merges audited, variables labeled, estimates captured to file.
- **95/100 = Replication-grade**.

## Stata (.do)

| Severity | Issue | Deduction |
|---|---|---|
| Critical | Syntax error / script does not run | -100 |
| Critical | Unintended `m:m` merge (Cartesian product) | -30 |
| Critical | Hardcoded machine-specific absolute path | -20 |
| Critical | `merge` with >5% unmatched, unexplained / `_merge` not inspected | -20 |
| Major | No `set seed` where randomness is used | -10 |
| Major | Estimates console-only (not stored/exported) | -10 |
| Major | `_merge` not dropped before the next merge | -5 |
| Major | New variables unlabeled | -5 |
| Minor | No log opened/closed | -5 |
| Minor | Missing header block | -5 |
| Minor | Style inconsistency | -2 |

## R (.R) — for the figure/table side

| Severity | Issue | Deduction |
|---|---|---|
| Critical | Syntax error / does not run | -100 |
| Critical | Hardcoded absolute paths | -20 |
| Major | Missing `set.seed()` where randomness is used | -10 |
| Major | Output not regenerated from current code | -5 |

## Enforcement

- **< 80:** block. List blocking issues (correctness/merge first).
- **< 90:** allow save, warn.
- User can override with explicit justification.
