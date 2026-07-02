# Plan — fold 2026-07-02 session lessons into coding-snds template

**Status:** APPROVED (user-directed) · **Branch:** `snds-session-lessons-20260702` (off
`snds-r-portal-workflow`) · **PR target:** `main` (no merge)

## Source
A live SNDS project session (portal R runs, an OOM, a kicked session, an export-gate review, a
code-list audit). Only SNDS-GENERAL lessons enter the template; all cohort/table/estimate
specifics stay in the project repo.

## Already on the parent branch (commit aeeb9ff, same harvest)
sas-sql-conventions §14 (pre-2013 live-vs-archive DCIR tables) + §15 (push the reduction to
Oracle); snds-r-portal: lubridate-exports quirk, Home-root=Citrix + quota, ORAUSER-unqualified,
`''` IS NULL, rm()+gc(), Plots-pane loop-print.

## This commit — lesson → home
1. **Air-gapped run loop** (new snds-r-portal §4): re-paste locally-edited scripts/helpers before
   every run (stale `source()` symptom: "fonction introuvable" for the NEW function only); make
   analysis scripts SELF-CONTAINED (one `source()` rebuilds all state from Oracle — a kicked
   session then costs nothing); fold console explorations back into the script.
2. **Top-level `on.exit` fires immediately under `source()`** (r-code-conventions §6 pitfalls):
   kills a DB connection before first use; explicit teardown at end, or wrap in a function.
3. **Post-OOM / debugger recovery** (r-code-conventions §6): `Browse[1]` frames pin objects → gc
   can't free; `Q`, `rm()` leftovers, `gc()`; prefer a full restart after an OOM; find hogs with
   `object.size` over `ls()`.
4. **Char-coded Oracle code columns** (snds-r-portal §3): codes read back CHAR (possibly
   zero-padded) → integer `==` silently mismatches; lexicographic tie-breaks ("13" < "2");
   normalize `as.integer(trimws(as.character(x)))`; fail-fast `stopifnot` right after any filter
   that could go empty.
5. **Export gates: complement arm + continuous/EUR outcomes** (export-compliance rules 1 & 7):
   binary gate needs N−events ≥ 11 too (near-saturated bin leaks its non-events); for EUR/
   continuous outcomes the events-gate is meaningless → gate N + dominance; the RAW max-share
   never enters an exportable annex (share × cell total = the top contributor's exact amount, an
   individual-scale MAX) — boolean DOM_OK in the annex, raw share in the enclave log only.
6. **Billing supplements vs assays in code lists** (references/snds-data.md): audit each
   nomenclature code for "cotation supplémentaire"/billing-supplement status — supplements track
   care setting/acuity mechanically and poison indicators/instruments built from the list.
7. **MEMORY.md seeds:** short [LEARN] lines for 1, 4, 6 + Home-root=Citrix.

## Verification
settings.json untouched → `json.load` smoke anyway; no hook edits; grep the diff for project
specifics (cohort names, row counts, estimates, NABM code lists as *defaults*); relative
cross-links resolve; commit; `gh pr create` against main; DO NOT merge.
