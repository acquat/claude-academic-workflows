# Coding with Stata

Claude as an empirical-analysis assistant for **Stata**, on local or institutional data. Claude writes `.do` files; you run them — so the discipline is *correctness before running*: verified syntax, audited merges, reproducible paths.

## What's inside

```
.claude/
├── CLAUDE.md                       # role, mixed-workflow protocol, merge discipline
├── rules/
│   ├── stata-conventions.md        # header, version/clear/seed, logging, paths, labeling, output
│   ├── verification-protocol.md    # _merge inspection, count/isid, summarize, fresh-session run
│   ├── quality-gates.md            # Stata rubric (m:m merge / unmatched / abs paths = critical)
│   ├── replication-protocol.md     # reproduce published numbers to tolerance before extending
│   └── plan-first-workflow.md · orchestrator-protocol.md · session-logging.md
├── agents/  stata-reviewer         # merge discipline, estimand checks, output capture — read-only
├── skills/
│   └── stata-syntax/               # verify syntax vs. the official PDF manuals; growing syntax-reference.md
├── templates/ · hooks/ · settings.json
```

Plus `/rigor` and `/empirical-coding-discipline` from this repo's `skills/` library. For R-side analysis tooling, see **[Other helpful resources](../../ATTRIBUTIONS.md)**. Related work: [dylantmoore/stata-skill](https://github.com/dylantmoore/stata-skill) takes a pre-built-reference approach to the same "Claude can't run Stata" problem; `/stata-syntax` instead verifies against the official manuals on disk and grows a per-project verified reference.

## How to use it

1. **Copy** `.claude/` into your project.
2. **Fill** `CLAUDE.md` placeholders (name, institution, project, data).
3. **Set your Stata docs path** in the `/stata-syntax` skill (Step 2) if the macOS default doesn't match your install.
4. Decide the project-root `global` and your `do/` numbering scheme.

## The loop

`/stata-syntax` before writing any Stata → generate a `.do` with built-in `_merge`/`count`/`summarize` checks → you run it (or Claude runs a small one via `stata -b do`) → `stata-reviewer` reviews → estimates exported via `esttab`/`outreg2`. As you confirm new command syntax, it accretes in `skills/stata-syntax/syntax-reference.md` for next time.
