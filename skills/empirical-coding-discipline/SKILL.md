---
name: empirical-coding-discipline
description: Enforces disciplined empirical coding practices — audit data at every step, verify units and identifiers, never brute-force, clean up after yourself
---

# Empirical Coding Discipline

This skill governs all data construction, cleaning, and analysis work. The user is building research datasets where errors compound silently. Every step must be deliberate and verified.

## Before Writing Any Code

1. **Understand the data before touching it.** Read documentation, check variable names, examine a few rows. Never assume column names, types, **or storage structure** (how dates/keys are physically partitioned or stored — e.g. monthly vs consolidated partitions, date vs datetime) — verify them against the data dictionary or a quick probe, never from a comment or memory. A filter built on an assumed structure fails *silently* (returns the wrong rows), it does not error.
2. **Know your unit of observation.** Before any merge, reshape, or collapse: state explicitly what the unit of observation is (hospital-year? person-quarter? firm?) and confirm it.
3. **Know your unique identifiers.** Before merging, run the equivalent of `isid` / `duplicates report` on the key variables. If the merge key isn't unique where it should be, stop and investigate — don't let it silently create duplicates.
4. **Ask before proceeding.** When a design choice has multiple valid approaches (sample restrictions, variable definitions, merge strategies), present the options and ask. Don't pick one silently.

## During Code Construction

5. **Check variable names against the actual data.** Before referencing any variable in a merge, filter, or computation, verify it exists in the dataset with the exact spelling. The near-miss-variable-name class of error (e.g. `entity_id` grabbed when `entity_ever_treated` was meant) must never happen.
6. **Handle merges carefully.**
   - Always check for suffix conflicts (`entity_id.x`, `entity_id.y`) before they cause downstream failures.
   - Report merge rates: how many matched, how many didn't, from which side.
   - If an m:1 merge produces unexpected duplicates, stop.
7. **No magic numbers.** Every constant (distance thresholds, year cutoffs, bed counts) must have a comment citing why that value was chosen and where it comes from.
8. **No ad-hoc terminal commands for data processing.** Every data transformation must be in a script file with a header, not an inline `Rscript -e` one-liner. One-liners are acceptable only for quick diagnostic queries that produce no output files.

## Diagnostic Checks (Required)

9. **At every stage of the pipeline, print:**
   - Number of observations
   - Number of unique entities/identifiers
   - Range of key variables (years, values)
   - Missing value counts for critical variables
10. **After any sample restriction, report what was dropped and why.** Not just "N observations deleted" but the composition of what was lost.
11. **After constructing any derived variable, sanity-check it.** Summary statistics, cross-tabs against known values, spot-check individual cases. Does operating margin of -5,338 make sense? No — investigate.
12. **Cross-validate against external benchmarks.** When possible, compare your summary statistics to published numbers (a benchmark table from the paper you build on, fully cited). Flag and explain discrepancies.

## After Code Runs

13. **Read the log.** Don't assume success — check for warnings, unexpected counts, failed merges, convergence issues.
14. **Clean up.** Delete or archive temporary/diagnostic scripts once the diagnosis is complete. Don't leave stale files that will confuse future sessions. Keep the repo tidy.
15. **Update numbering.** When scripts are added or removed, renumber so the sequence is clean and unambiguous. Don't leave gaps or inconsistencies.

## Level of Variation

16. **Always be explicit about what level variation comes from.** If treatment varies at the state level, say so. If you're clustering at entity level but treatment is state-level, flag the mismatch. Think about what identifies the coefficient.
17. **When constructing instruments or treatment variables, trace the source of variation.** Is it cross-sectional? Time-series? Both? Is it predetermined or potentially endogenous? State this in comments.

## Upstream Pipeline Verification

18. **Before writing any analysis script, read the upstream scripts that produce its inputs.** Verify variable names, units, and structure at the source — don't guess what's in `pos_panel.dta` or `entity_events.dta`, read the script that created it.
19. **When an upstream script changes, trace all downstream dependencies.** If `04_build_entity_timeline.do` renames a variable, every script that reads its output must be checked and updated.
20. **Test merges against the actual data before embedding them in a long script.** A quick `describe` or `names()` call to confirm the key variable exists and is spelled correctly prevents 20 minutes of debugging later.

## What NOT To Do

- **Never brute-force a fix.** If code fails, diagnose the root cause. Don't try 5 different workarounds hoping one sticks.
- **Never fabricate sample sizes, variable names, or data properties.** If you don't know, check.
- **Never filter a partitioned/keyed column by exact-equality on an assumed value** (`x == "2018-01-01"`). Use a **range** (`>= a & < b`). An exact match silently returns a fraction of the data the moment the storage layout differs from what you assumed — the classic silent-wrong-result bug.
- **Never call a rewrite "done" until its row counts match a benchmark.** Re-deriving an extraction must reproduce the known total and per-period counts (prior run, or a published table) — "it parses / looks right" is not evidence. Emit the counts and compare.
- **Never proceed past a data quality issue without flagging it.** An outlier, a merge failure, a suspicious pattern — raise it immediately.
- **Never overwrite raw data.** All transformations produce new files in `working/` or `output/`.
- **Never silently drop observations.** Every `drop if` or `keep if` must be logged with counts.
- **Default: do not run Stata.** Claude writes `.do` files; the user executes them — unless the project's CLAUDE.md defines a mixed-workflow exception (e.g. small self-contained batch runs), in which case that protocol governs. R and Python may be run directly.
- **Never mix language syntax.** Do not use R functions (`sprintf`, `paste`, `c()`) in Stata code, or Stata syntax (`di`, `gen`, `replace`) in R code. Know which language you are writing and use its idioms correctly.
