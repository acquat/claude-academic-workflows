# MEMORY — Coding with SNDS

Append-only `[LEARN]` log. `[LEARN:category] wrong → right (why)`. Loads every session — keep it short.

## Seed lessons (transferable; keep or replace)

- `[LEARN:snds]` Filter claims tables on `FLX_DIS_DTD` (indexed partition key), not `EXE_SOI_DTD` → wrong field triggers a full table scan and wastes portal queue time.
- `[LEARN:snds]` Composite SNDS joins need the full key set (e.g. 9 keys for `ER_PRS_F ↔ ER_BIO_F`) → omitting any key silently duplicates rows; catch it with `count(distinct id)`.
- `[LEARN:security]` Never let `BEN_NIR_*` / `BEN_IDT_ANO` reach a flat file or `.log`; disclosure-check every export → confidentiality breach, not a style issue.
- `[LEARN:pattern]` **Provisioning-gate pattern** (reusable for any tool/resource that isn't auto-available in a constrained environment): make the gate fire on its own through three layers — (1) an always-loaded `CLAUDE.md` instruction (the guaranteed trigger; fires even before any relevant file exists, e.g. "write me an R script"), (2) a path-scoped `rules/` doc holding the full procedure, (3) a `PreToolUse` hook that injects the gate into context on the matching edit/write. → A documented procedure nobody reads is not a gate; the always-loaded line + the hook are what make it *automatic*. Here: R-on-the-SNDS-portal ([`rules/snds-r-portal.md`](rules/snds-r-portal.md), [`hooks/snds-r-rules.py`](hooks/snds-r-rules.py)). The same PreToolUse context-injection layer also enforces *conventions* (not just gates): [`hooks/sas-rules.py`](hooks/sas-rules.py) fires the SAS/Oracle rules on every `.sas` edit so `sas-sql-conventions.md` is applied, not merely documented.
- `[LEARN:pattern]` **Build→document reminder**: a `PostToolUse(Write)` hook on `skills/*/SKILL.md` ([`hooks/skill-website-reminder.py`](hooks/skill-website-reminder.py)) fires when a new skill is created and prompts updating public-facing website materials (offers to do it now or spawn a separate session). → Generalizes: tie any "thing built" event to its downstream "must-document" chore so it is not forgotten; a hook can't open a new app window, but it can surface a `systemMessage` + tell Claude to spawn a task.
- `[LEARN:r-portal]` The portal is air-gapped: a locally-edited script/helper is STALE there until re-pasted; `source()` loads the old copy (symptom: only the NEWLY-added function is "introuvable"). Refresh helpers before every run; make scripts self-contained so a killed session costs nothing → [`rules/snds-r-portal.md`](rules/snds-r-portal.md) §4.
- `[LEARN:r-portal]` R saves at Home root (`~/`) land in the shared CITRIX space, not user space — saturation has blocked the portal-wide import/export tool. Write to `~/sasdata1`/`~/rdata` (quota-limited: a disk error = request an extension, not a bug) → `rules/snds-r-portal.md` §2.
- `[LEARN:snds]` Oracle code columns read back as CHAR (sometimes zero-padded): integer `==` silently mismatches and tie-breaks sort lexicographically (`"13" < "2"`) → normalize `as.integer(trimws(as.character(x)))` + fail-fast `stopifnot` right after any filter that could go empty.
- `[LEARN:snds]` Nomenclature code lists mix real assays/procedures with « cotations supplémentaires » (billing supplements) that fire mechanically with care setting/acuity → audit each code's libellé before it enters an indicator/instrument ([`references/snds-data.md`](references/snds-data.md)).

## Project-specific lessons

<!-- add as you confirm: code lists, table grains, the disclosure threshold, instrument construction gotchas -->
