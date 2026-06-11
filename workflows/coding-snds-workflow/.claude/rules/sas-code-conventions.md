---
paths:
  - "**/*.sas"
---

# SAS Code Conventions (SNDS)

The standards the `sas-reviewer` checks against. Companion to [`sas-sql-conventions.md`](sas-sql-conventions.md) (Oracle/SQL query rules).

## Script header (every script)

```sas
/****************************************************************
 Title:        <what this script does>
 Author:       <name>            Date: <YYYY-MM-DD>
 Prerequisite: <upstream scripts that must run first>
 Inputs:       <table>  (rows, keys)
 Outputs:      <table>  (rows, keys)
 Est. runtime: <minutes on the portal>
****************************************************************/
```

## Parameters & paths

- **All study parameters as `%let` at the top** — never hardcoded inline. The secure portal has no interactive editing; the header must be auditable. Prefer `%include "_config/libnames.sas"` for library declarations.
- **No user-local mount paths** in step code (`~/sasdata/...`, `/Citrix.../...`). Parameterize the output dir (`%let outpath = …`).
- `proc product_status; run;` (or equivalent) near the top to capture the SAS/Oracle version.

## Data discipline

- **Sentinel dates** (`'01JAN1600'dt`, `'31DEC9999'dt`) → set to missing before any date arithmetic.
- **Row-count audit after every major step:** `proc sql; select count(*), count(distinct <id>) from <table>; quit;`.
- **Structural zero vs. missing** — encode and document the distinction for every constructed outcome.
- **Every code list documented** (drug ATC, procedure CCAM, biology NABM, specialty, outcome claim codes) — what's in, what's out, with a source.

## Joins & filters

- Explicit `on a.key = b.key` joins only. Use the full composite key for SNDS table joins (see `sas-sql-conventions.md`).
- Filter claims tables on the partition key (`FLX_DIS_DTD`); inner-join to a cohort id-bridge — never full-population scans without justification.
- Every restricting `where` has a comment; every threshold has a citation or `[CHOICE]` tag.

## Estimation & output

- Capture estimates with `ods output Name=work.ds` — never console-only.
- Export tables/figures to a documented `_outputs/` directory.
- IV: report the first-stage F; acknowledge LATE vs. ATE for heterogeneous effects.

## Macro hygiene

- `%local` for internal vars; named (not positional) args; no `%global` clobbering; guard or remove debug `%put`s.

## Security

- See [`snds-data-security.md`](snds-data-security.md). In brief: no identifiers in logs, in flat files, or on shared mounts; respect disclosure-control on any exported aggregate.
