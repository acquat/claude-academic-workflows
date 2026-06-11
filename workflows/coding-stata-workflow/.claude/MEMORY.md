# MEMORY — Coding with Stata

Append-only `[LEARN]` log. `[LEARN:category] wrong → right (why)`. Loads every session — keep it short.

## Seed lessons (transferable; keep or replace)

- `[LEARN:stata]` Always declare merge kind (`1:1`/`m:1`/`1:m`) and inspect `_merge` → an accidental `m:m` is a Cartesian blow-up and a silent data-quality bug.
- `[LEARN:stata]` Verify command syntax against the manuals before writing (`/stata-syntax`) → syntax can't be cheaply trial-and-errored, so a guessed option wastes a run.
- `[LEARN:repro]` Paths via a top `global` + relative refs, never machine-specific absolute → the do-file must run on any machine.

## Project-specific lessons

<!-- add as you go: package syntax confirmed, merge keys, variable coding, estimation choices -->
