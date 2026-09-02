# Migration Map

This folder translates the Claude-specific setup into Codex-native concepts.

## Claude -> Codex mapping

- `.claude/CLAUDE.md` -> one or more Codex skills plus reference files
- `.claude/rules/*.md` -> reference files consumed by the relevant Codex skill
- `.claude/skills/*/SKILL.md` -> Codex skills, often with simplified frontmatter
- `.claude/agents/*.md` -> either:
  - embedded procedure inside a Codex skill
  - a dedicated supporting skill
  - a future subagent implementation if needed
- `.claude/hooks/*.py` -> explicit checklists and safety gates inside Codex skills
- `.claude/settings.json` -> not portable; replaced by skill instructions and Codex policy

## Mandatory Codex differences

Codex does not auto-run the Claude hook events used in the original workflows.
So the Codex version treats those behaviors as deliberate procedural steps:

- session-start rigor reminder
- verify-after-edit reminder
- session-log reminder
- context-size awareness

## External dependencies to recreate later

- Pedro Sant'Anna's `lit-review` skill:
  - this bundle includes a native Codex placeholder and integration points
  - exact behavior should be imported or reconstructed from the source workflow if desired
- Michael Ewens' logging-hook pattern:
  - this bundle includes a Codex session-discipline skill
  - exact automation semantics should be reconstructed if desired
