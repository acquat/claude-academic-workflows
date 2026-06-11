# Installing & using these workflows

You need **[Claude Code](https://docs.claude.com/en/docs/claude-code)** installed. No other dependencies — these are plain Markdown configs plus a few small Python hooks. (One exception: the administrative workflow's form-filling uses the `openpyxl` package — `pip install openpyxl`.)

## 1. Make the shared skills available (once per machine)

The `skills/` folder holds the two cross-cutting rigor skills (`/rigor`, `/empirical-coding-discipline`) used across these workflows. Put them in Claude Code's **personal skills directory**, `~/.claude/skills`, so they're available in any project (a general academic toolkit — lit review, paper review, slide production — installs the same way; see [Other helpful resources](ATTRIBUTIONS.md)):

```bash
# Option A — copy (simple):
mkdir -p ~/.claude/skills
cp -R skills/* ~/.claude/skills/

# Option B — symlink (one source of truth; updates when you `git pull`):
ln -s "$PWD/skills" ~/.claude/skills      # only if ~/.claude/skills doesn't already exist
```

Verify: `ls ~/.claude/skills` should list the skill folders.

## 2. Add a workflow to a project

Pick the workflow that matches the job (see the table in the [README](README.md)) and copy its `.claude/` into your project root:

```bash
cp -R workflows/coding-stata-workflow/.claude /path/to/your/project/.claude
```

Each workflow bundles the **agents** its skills need (they ship inside the workflow's `.claude/agents/`, so they travel with the project), its rules, hooks, and a `CLAUDE.md`. Open Claude Code in the project and it loads automatically.

## 3. Fill in the placeholders

Open `.claude/CLAUDE.md` and replace every `[YOUR …]` / `[…]` token (name, institution, project, paths, etc.). Each workflow's own `README.md` lists its setup steps — some have a one-time step worth doing first:

- **administrative** — drop your reimbursement-policy PDF in and run `/ingest-policy` to generate the rulebook; declare any maintained documents (CV) in `references/document-sources.md`.
- **academic-writing** — create `lit_review.md` + `references.bib`; pin notation in `paper-writing-conventions.md` for theory papers.
- **coding-snds** — record your tables, code lists, and your data-access agreement's disclosure threshold in `references/snds-data.md`.
- **coding-stata** — confirm your Stata manuals path in the `/stata-syntax` skill.

## Permissions

The workflows ship **without a permissions block** in `settings.json`, so Claude Code uses its standard prompting — it asks before editing files or running commands. Sensible when trying out someone else's config. If you want the agent to act more autonomously, add a `permissions` block (e.g. `"defaultMode": "acceptEdits"` or an allow-list) per the Claude Code settings docs.

## Updating

`git pull` to get changes. If you symlinked `skills/` (Option B), skills update automatically; if you copied them, re-copy. Workflows you've already dropped into projects are independent copies — re-copy a workflow's `.claude/` if you want its latest version (you'll re-apply your placeholder edits).
