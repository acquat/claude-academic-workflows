# MEMORY — Coding with SNDS

Append-only `[LEARN]` log. `[LEARN:category] wrong → right (why)`. Loads every session — keep it short.

## Seed lessons (transferable; keep or replace)

- `[LEARN:snds]` Filter claims tables on `FLX_DIS_DTD` (indexed partition key), not `EXE_SOI_DTD` → wrong field triggers a full table scan and wastes portal queue time.
- `[LEARN:snds]` Composite SNDS joins need the full key set (e.g. 9 keys for `ER_PRS_F ↔ ER_BIO_F`) → omitting any key silently duplicates rows; catch it with `count(distinct id)`.
- `[LEARN:security]` Never let `BEN_NIR_*` / `BEN_IDT_ANO` reach a flat file or `.log`; disclosure-check every export → confidentiality breach, not a style issue.
- `[LEARN:pattern]` **Provisioning-gate pattern** (reusable for any tool/resource that isn't auto-available in a constrained environment): make the gate fire on its own through three layers — (1) an always-loaded `CLAUDE.md` instruction (the guaranteed trigger; fires even before any relevant file exists, e.g. "write me an R script"), (2) a path-scoped `rules/` doc holding the full procedure, (3) a `PreToolUse` hook that injects the gate into context on the matching edit/write. → A documented procedure nobody reads is not a gate; the always-loaded line + the hook are what make it *automatic*. Here: R-on-the-SNDS-portal ([`rules/snds-r-portal.md`](rules/snds-r-portal.md), [`hooks/snds-r-rules.sh`](hooks/snds-r-rules.sh)). The same PreToolUse context-injection layer also enforces *conventions* (not just gates): [`hooks/sas-rules.sh`](hooks/sas-rules.sh) fires the SAS/Oracle rules on every `.sas` edit so `sas-sql-conventions.md` is applied, not merely documented.

## Project-specific lessons

<!-- add as you confirm: code lists, table grains, the disclosure threshold, instrument construction gotchas -->
