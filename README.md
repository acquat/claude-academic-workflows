# AI Tools for Academic Work

AI tools that have been very helpful to me as an academic — packaged so they may be helpful to others! Beyond the now-widespread uses on coding and writing, these [Claude Code](https://docs.claude.com/en/docs/claude-code) configurations can help on things specific to academic work: filing for reimbursements following the specifics of your institutional policies, updating your CV from your own records, supervising student projects, or coding inside a secure data enclave. If you find bugs or have suggestions on how to improve these tools, don't hesitate to reach out!

The main thing I found myself needing to build into these tools is **rigor** — each workflow pushes the agent to verify its output before asserting it: references are checked before they're cited, scripts are read end-to-end, institutional policy is followed rule by rule, and when the agent is unsure, it asks the user instead of resolving ambiguity on its own.

> Built by [Angelique Acquatella](https://angieacquatella.com) (Toulouse School of Economics). These workflows are *specialists* — for the general-purpose academic layer they pair with, see **[Other helpful resources](ATTRIBUTIONS.md)**.

---

## The five workflows

| Workflow | Use it when you're… | What's inside |
|---|---|---|
| **[administrative](workflows/administrative-workflow/)** | processing **reimbursements / receipts**, or keeping a **CV / bio** current from your records | `/ingest-policy` (drop your institution's policy PDF → an agent compiles a rule-by-rule compliance rulebook — portable across institutions); `/update-document` (update a CV/bio based on activity on your computer — e.g. a referee report for a new journal prompts you to add the journal under your Refereeing Service section); receipt-classifier · form-filler · compliance-reviewer · deadline-watcher agents |
| **[academic-writing](workflows/academic-writing-workflow/)** | writing a **paper** (theory or empirical) toward submission / R&R | the rigor hard-rules: `no-fabrication` (verify every claim in the turn you write it, with a mechanical self-check), `lit-review-protocol` (every paper read is logged before it's cited), `replication-protocol` (reproduce published numbers before extending), and a notation-registry convention for theory papers |
| **[coding-snds](workflows/coding-snds-workflow/)** | coding in the **French SNDS** secure health-data enclave (SAS/Oracle + R) | SAS/SQL conventions (partition keys, composite joins, safe-replace); DUA compliance checks through statistical-disclosure export gates built into every script, with cited legal basis; a `sas-reviewer` agent; `/sds-doc` never-guess lookup |
| **[coding-stata](workflows/coding-stata-workflow/)** | general empirical analysis in **Stata** | do-file conventions, merge discipline, a `stata-reviewer` agent, `/stata-syntax` (verify syntax against the official manuals before writing — and grow a per-project verified reference) |
| **[teaching](workflows/teaching-workflow/)** | **supervising and supporting students** | `/supervise-project` (per-student tracker: feedback given, content reviewed, advisor check-in timeline + due-check-in flags), `/tf-builder`, `/reading-list` — to keep supervision on schedule and point students to helpful/relevant resources |

Each workflow folder has its own README with the full file list and setup steps.

**To use a workflow:** copy-paste the pertinent workflow's `.claude/` folder into the specific project or task folder where you'll be working — the paper's folder, your reimbursements folder, your teaching folder. Claude Code loads it automatically when you open that folder.

---

## How it's organized

- **`workflows/`** — five self-contained `.claude/` configs. Each bundles its `CLAUDE.md` brain, its rules, any specialist agents its skills need, two small hooks (auto-load the rigor standard at session start; a verify-after-edit nudge), and a portable `settings.json`.
- **`skills/`** — the two cross-cutting rigor skills the workflows share: `/rigor` (never fabricate parameters; cite or stop — auto-loaded by every workflow's session-start hook) and `/empirical-coding-discipline` (audit every step; verify units and identifiers — used by the writing and coding workflows).
- A **shared working discipline** rides in every workflow: plan first (plans saved to disk), an orchestrator loop (implement → verify → review → fix → score), session logging at three moments, and 80/90/95 quality gates.

**Design choices:** rigor is first-class and on by default; the templates are LaTeX/Beamer + R/SAS/Stata oriented; nothing assumes git. This repo builds on top of the general academic toolkit (lecture production, literature review, generic paper review) — see [Other helpful resources](ATTRIBUTIONS.md) for kits that install alongside these workflows.

---

## Quickstart

```bash
# 1. Clone
git clone https://github.com/acquat/claude-academic-workflows.git
cd claude-academic-workflows

# 2. Make the rigor skills available to Claude Code (once per machine)
#    ~/.claude/skills is Claude Code's personal skills directory.
mkdir -p ~/.claude/skills
cp -R skills/* ~/.claude/skills/

# 3. Drop a workflow into a project
cp -R workflows/academic-writing-workflow/.claude /path/to/your/project/.claude
#    then open Claude Code in that project and fill the [YOUR …] placeholders.
```

Full details in **[INSTALL.md](INSTALL.md)**.

---

## What's next

A **Codex version** of these workflows coming soon!

## Other helpful resources, credits & license

- **[claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** — Pedro Sant'Anna's comprehensive academic kit (slides, literature review, paper review, data analysis), which my own setup grew out of. In particular, download his [`/lit-review`](https://github.com/pedrohcgs/claude-code-my-workflow/tree/main/.claude/skills/lit-review) skill — it pairs naturally with the academic-writing workflow here.
- **[stata-skill](https://github.com/dylantmoore/stata-skill)** — Dylan Moore's Stata reference skill; a complementary approach to `/stata-syntax`.
- **[strategic-revision](https://github.com/jusi-aalto/strategic-revision)** — a super useful revision planner for revise-and-resubmits, by GitHub user `jusi-aalto`.
- **["Automatic" logging in Claude Code](https://gist.github.com/michaelewens/9a1bc5a97f3f9bbb79453e5b682df462)** — Michael Ewens' session-logging hook.

Full credits in **[ATTRIBUTIONS.md](ATTRIBUTIONS.md)**. **[License](LICENSE).**

*Not affiliated with Anthropic. "Claude Code" is Anthropic's tool; this is an independent set of configurations for it.*
