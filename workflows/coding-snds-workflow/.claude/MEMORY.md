# MEMORY — Coding with SNDS

Append-only `[LEARN]` log. `[LEARN:category] wrong → right (why)`. Loads every session — keep it short.

## Seed lessons (transferable; keep or replace)

- `[LEARN:snds]` Filter claims tables on `FLX_DIS_DTD` (indexed partition key), not `EXE_SOI_DTD` → wrong field triggers a full table scan and wastes portal queue time.
- `[LEARN:snds]` Composite SNDS joins need the full key set (e.g. 9 keys for `ER_PRS_F ↔ ER_BIO_F`) → omitting any key silently duplicates rows; catch it with `count(distinct id)`.
- `[LEARN:security]` Never let `BEN_NIR_*` / `BEN_IDT_ANO` reach a flat file or `.log`; disclosure-check every export → confidentiality breach, not a style issue.

## Project-specific lessons

<!-- add as you confirm: code lists, table grains, the disclosure threshold, instrument construction gotchas -->
