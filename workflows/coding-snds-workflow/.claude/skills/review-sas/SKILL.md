---
name: review-sas
description: Run the SAS code review protocol on SAS scripts that work with French SNDS data. Checks code quality, reproducibility, SNDS-specific anti-patterns (sentinel dates, PII handling, partition keys, claims-table cohort restrictions), disclosure control, and statistical pipeline integrity. Produces a report without editing files.
argument-hint: "[filename or directory or 'all']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Task"]
---

# Review SAS Scripts

Run the SAS code review protocol calibrated for SNDS workflows.

## Steps

1. **Identify scripts:**
   - A specific `.sas` file → review that file.
   - A directory → review every `.sas` under it (recursive).
   - `all` → review every `.sas` under your scripts directory.
   - Empty → ask which scripts to review.
2. **For each script, launch the `sas-reviewer` agent**, instructing it to:
   - Follow the full protocol in `.claude/agents/sas-reviewer.md`.
   - Read `.claude/rules/sas-code-conventions.md` and `.claude/rules/sas-sql-conventions.md` for standards.
   - Read `.claude/references/snds-data.md` for SNDS lookups.
   - Save its report to `.claude/quality_reports/[script_name]_sas_review.md`.
3. **Consolidated summary** after all reviews: issues per script (Critical/Major/Minor/Polish), the top 5 most critical across the batch, cross-script patterns (e.g. "sentinel-date handling missing in A, B, E2"), and a pointer to each report.
4. **Do NOT edit any SAS source file.** Reports only. Fixes are applied only after explicit user approval, and never in a read-only RA pipeline folder — only in your writable working folder.

## When to invoke

- After a co-analyst/RA modifies a `.sas` file.
- Before any SAS-side refactor (baseline review).
- Before pipeline output is incorporated into a manuscript table/figure.
- Before any reproducibility audit of paper numbers, when the underlying scripts are SAS.

## Cross-references

- `.claude/agents/sas-reviewer.md` · `.claude/rules/sas-code-conventions.md` · `.claude/rules/sas-sql-conventions.md` · `.claude/references/snds-data.md`.
