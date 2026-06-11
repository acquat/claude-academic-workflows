# CLAUDE.md — Coding with Stata (empirical analysis)

> **ROLE.** Claude is an empirical analysis assistant for **Stata** work — data cleaning, merges, estimation, and output — on local or institutional datasets (not the SNDS enclave; for that, use the SNDS template). **R** is the optional companion for figures/tables. Claude writes and edits `.do` files; **you run Stata** (Claude does not), so correctness-before-running is the whole discipline.

**User:** [YOUR NAME] · **Institution:** [YOUR INSTITUTION]
**Project:** [SHORT DESCRIPTION — data + question]
**Data:** [source(s); location] — note any access/licensing constraints.

---

## Core Principles

- **Verify syntax before writing** — invoke [`/stata-syntax`](skills/stata-syntax/SKILL.md) whenever producing Stata code; consult the internal reference, then the manuals, then ask. Never guess (a syntax error wastes a run).
- **Merge is a two-person job** — always declare `1:1`/`m:1`/`1:m` (never accidental `m:m`); inspect `_merge`; drop it before the next merge. See [verification-protocol](rules/verification-protocol.md).
- **Reproducible by construction** — `version`, `clear all`, `set seed`, a top `global` for paths (relative, never machine-specific absolute), a log opened and closed. See [stata-conventions](rules/stata-conventions.md).
- **Rigor always** — [`/rigor`] + [no fabrication]; every threshold/sample choice documented; estimates captured to file, never console-only.
- **Plan first** · **Verify after** · **Quality gates** (nothing ships below 80/100).
- **`[LEARN]` tags** — append Stata lessons (merge gotchas, command syntax, package quirks) to [MEMORY.md](MEMORY.md).

---

## Mixed-Workflow Protocol

- **Claude generates and edits `.do` files**, with built-in `_merge`/`count`/`isid`/`summarize` checks (see verification-protocol).
- **Claude may run small, self-contained scripts** via CLI: `stata-mp -b do script.do` (or `stata -b do …`), then read the `.log`.
- **You run major analyses** in the Stata GUI (large datasets, long loops, interactive review).
- When in doubt: generate the `.do` and ask you to run it, then verify against the returned log.

---

## Folder Structure

```
[YOUR-PROJECT]/
├── do/            # .do files (numbered: 01_clean → 02_merge → 03_analyze → 04_tables)
├── data/
│   ├── raw/       # never modified in place
│   └── clean/     # derived .dta
├── output/
│   ├── tables/    # esttab/outreg2 → .tex/.csv
│   └── figures/   # graph export → .png/.pdf
├── logs/
└── .claude/
    ├── CLAUDE.md · MEMORY.md · settings.json
    ├── rules/  agents/  skills/  hooks/  templates/
    └── quality_reports/{plans,session_logs,completions}/
```

---

## Skills Quick Reference

| Command | What it does |
|---|---|
| `/stata-syntax` | Verify Stata syntax against the internal reference + manuals before writing (this template's key skill) |
| `/empirical-coding-discipline` | Audit-every-step rigor (verify units/identifiers, never brute-force) |
| `/rigor` | The research-rigor standard (auto-loaded each session) |

The `stata-reviewer` agent (bundled) reviews `.do` files via the patterns above. For R-side review and general analysis tooling that pairs well with this workflow, see **Other helpful resources** in the repo README.

---

## Quality Thresholds

| Score | Gate | Meaning |
|---|---|---|
| 80 | Save | Runs clean from a fresh session |
| 90 | Handoff | Merges audited, variables labeled, estimates exported |
| 95 | Replication-grade | — |

See [`.claude/rules/quality-gates.md`](rules/quality-gates.md).

## Setup checklist (do once)

1. Fill the placeholders above.
2. Confirm your Stata docs path for `/stata-syntax` (Step 2 of the skill) — adjust the default if needed.
3. Decide the project root `global` and the `do/` numbering scheme.
