# Other Helpful Resources & Credits

Everything in this repository was written or adapted by its author. It did not appear in a vacuum: the
projects below shaped how it works, solve neighboring problems, or provide the general-purpose
layer this repo deliberately does **not** reinvent. Use them — they're excellent.

## The general academic toolkit

- **[claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** — Pedro H. C.
  Sant'Anna's comprehensive, MIT-licensed foundation for AI-assisted academic work: lecture and
  slide production, literature review, paper review, data analysis, TikZ tooling, and the
  plan→verify→review working discipline. **My own setup was originally bootstrapped from this kit,
  and these workflows are designed to install alongside it** — wherever a workflow here says
  "general manuscript/slide/R tooling," this is the recommended source. **A concrete pairing:
  download his [`/lit-review`](https://github.com/pedrohcgs/claude-code-my-workflow/tree/main/.claude/skills/lit-review) skill to use with the academic-writing workflow here** — his skill
  searches and synthesizes the literature; this repo's `lit-review-protocol` rule then makes sure
  every paper it reads is logged (pages read, load-bearing claims) before it can be cited. His kit
  also includes a simulated peer-review pipeline (`/review-paper --peer` — an editor agent plus
  referee agents calibrated to journal profiles, itself adapted from Hugo Sant'Anna's *clo-author*
  with permission) that pairs well with the academic-writing workflow here. The contractor-style
  working pattern these workflows follow (plan first, verify after, quality gates) follows his
  approach; this repo's implementations of those core rules are its own.

## Neighboring tools worth knowing

- **[stata-skill](https://github.com/dylantmoore/stata-skill)** — Dylan Moore's Stata reference
  skill, motivated by the same "Claude can't run Stata" problem as this repo's `/stata-syntax`;
  his takes a pre-built-reference approach, mine verifies against the official manuals and grows a
  per-project reference. Try both.
- **[strategic-revision](https://github.com/jusi-aalto/strategic-revision)** — a DAG-validated
  revision planner for revise-and-resubmits (by GitHub user `jusi-aalto`). I use it privately;
  it pairs naturally with the academic-writing workflow's R&R stage.
- **["Automatic" logging in Claude Code](https://gist.github.com/michaelewens/9a1bc5a97f3f9bbb79453e5b682df462)**
  — Michael Ewens' session-log reminder hook, which inspired the logging discipline here.

## A note on lineage

Reviewer-style agents structured as "persona + checklist + severity-graded report" and quality
gates on an 80/90/95 scale are patterns popularized in the academic Claude community by Pedro
Sant'Anna's kit; this repo's `sas-reviewer`, `stata-reviewer`, and per-workflow quality gates apply
that *format* — including the reviewer persona and mission framing adapted from his `r-reviewer` —
to domains of their own (SNDS disclosure law, Stata merge discipline, expense-policy
compliance, student-work integrity).

## Platform

Built for **[Claude Code](https://docs.claude.com/en/docs/claude-code)** by Anthropic. Independent
project; not affiliated with or endorsed by Anthropic.
