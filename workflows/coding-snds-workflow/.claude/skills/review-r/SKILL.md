---
name: review-r
description: Run the R code review protocol on SNDS downstream analysis scripts (merges, models, tables, figures). Checks code quality, reproducibility, Oracle-from-R correctness, figure standards, and export-disclosure discipline. Produces a report without editing files.
argument-hint: "[filename or directory or 'all']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Task"]
---

# Review R Scripts

Run the R code review protocol calibrated for SNDS downstream analysis.

## Steps

1. **Identify scripts:**
   - A specific `.R` file → review that file.
   - A directory → review every `.R` under it (recursive).
   - `all` → review every `.R` under your analysis scripts directory (and any `R/` dir).
   - Empty → ask which scripts to review.
2. **For each script, launch the `r-reviewer` agent**, instructing it to:
   - Follow the full protocol in `.claude/agents/r-reviewer.md`.
   - Read `.claude/rules/r-code-conventions.md` (standards) and `.claude/rules/snds-r-portal.md`
     (provisioning, package prod-list, Oracle-from-R, hybrid).
   - Read `.claude/rules/snds-data-security.md` / `export-compliance.md` if the script exports anything.
   - Save its report to `.claude/quality_reports/[script_name]_r_review.md`.
3. **Consolidated summary** after all reviews: issues per script (Critical/High/Medium/Low), the top
   issues across the batch, cross-script patterns (e.g. "date funcs pushed into Oracle in A, C"), and
   a pointer to each report.
4. **Do NOT edit any R source file.** Reports only. Fixes are applied only after explicit user
   approval, and never in a read-only RA pipeline folder — only in your writable working folder.

## When to invoke

- After writing or modifying an R analysis/figure script.
- Before R output is incorporated into a manuscript table/figure.
- Before any reproducibility audit of paper numbers, when the underlying scripts are R.

## Cross-references

- `.claude/agents/r-reviewer.md` · `.claude/rules/r-code-conventions.md` · `.claude/rules/snds-r-portal.md` · `.claude/rules/snds-data-security.md`.
