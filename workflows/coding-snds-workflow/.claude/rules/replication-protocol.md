# Replicate Before You Extend

When building on published results (or on a co-author's prior output): **first reproduce their numbers, to tolerance, from their materials — only then modify anything.** An extension built on an unverified base inherits every silent discrepancy.

## The contract

1. **Record the targets first.** Before writing code, list the numbers you must hit (table, column, value, SE) in a targets file under `.claude/quality_reports/`.
2. **Translate faithfully, then improve.** Match the original specification exactly — sample, covariates, clustering, SE method — before any refactor. "Improvements" during replication are how mismatches hide.
3. **Compare against tolerance:**

| Quantity | Must match |
|---|---|
| Counts, N | exactly |
| Point estimates | to display rounding (≈ 3rd decimal) |
| Standard errors | within simulation/bootstrap noise |
| Significance calls | same stars, same level |

4. **On a mismatch: stop.** Do not proceed to the extension. Isolate the step where the numbers diverge (sample size first — it explains most gaps), and document the investigation even if unresolved.
5. **Only after all targets pass**, build the extension on the verified base, keeping the replication script untouched as the anchor.

## Why this is a hard rule

A referee who finds one un-replicable number stops trusting the rest. The cost of replicating first is hours; the cost of discovering a base-level discrepancy after the extension is the whole project's credibility.
