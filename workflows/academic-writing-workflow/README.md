# Academic Writing Workflow

Claude for **manuscript development** — theory papers, empirical papers, or both — through journal submission and R&R. The substance of this workflow is its **hard rules for rigor**: no fabricated claims, a verifiable literature trail, replication before extension.

## What's inside

```
.claude/
├── CLAUDE.md                       # role, hard rules, quality gates
├── rules/
│   ├── no-fabrication.md           # HARD RULE — verify every claim against source, with a mechanical self-check
│   ├── lit-review-protocol.md      # HARD RULE — every paper read updates lit_review.md before it may be cited
│   ├── replication-protocol.md     # reproduce published numbers to tolerance before extending
│   ├── paper-writing-conventions.md# notation registry + citation/theorem/figure conventions (theory)
│   ├── quality-gates.md · verification-protocol.md
│   └── plan-first-workflow.md · orchestrator-protocol.md · session-logging.md
├── templates/  session-log · quality-report · requirements-spec
├── hooks/  rigor-inject.py (auto-loads /rigor each session) · verify-reminder.py
├── settings.json
└── MEMORY.md · quality_reports/{plans,session_logs,completions}/
```

Plus `/rigor` and `/empirical-coding-discipline` from this repo's `skills/` library.

> **Pairs well with** a general manuscript toolkit (literature search, multi-pass paper review, bibliography validation) — see **[Other helpful resources](../../ATTRIBUTIONS.md)**. In particular, Pedro Sant'Anna's [`/lit-review`](https://github.com/pedrohcgs/claude-code-my-workflow/tree/main/.claude/skills/lit-review) skill is the natural companion to this workflow's `lit-review-protocol`: his skill finds and synthesizes the papers; the rule here makes sure everything it reads is logged before it can be cited.

## How to use it

1. **Copy** `.claude/` into your project: `cp -R "academic-writing-workflow/.claude" /path/to/paper/.claude`
2. **Fill placeholders** in `CLAUDE.md` (name, institution, paper title, target journal, main `.tex` path).
3. **Create** `lit_review.md` and `references.bib` at the project root; drop PDFs into `literature/`.
4. **Theory paper?** Pin your notation in `rules/paper-writing-conventions.md` on day one.

## The loop

Draft → log every paper you read in `lit_review.md` → write under the no-fabrication rule (verify each claim in the turn you write it) → compile 3-pass + bibtex → for empirical papers, replicate to tolerance before extending → revise.
