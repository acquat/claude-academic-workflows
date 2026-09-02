# Codex Workflow for Academic Work

This folder is the Codex-native counterpart to the Claude academic workflows in this repository.

The design priorities for this version are:

- Safety first
- Explicit user permission before leaving the local project repo
- No edits unless the user explicitly authorizes them
- Skills that map cleanly onto Codex's native `SKILL.md` mechanism

## Structure

- `skills/` contains Codex-native skills
- `references/` contains migration notes and external-dependency placeholders

## Safety policy

The governing rule for every skill in this bundle is:

1. Do not inspect folders outside the current local project repo unless the user explicitly authorizes it.
2. Do not edit files unless the user explicitly authorizes the edit.
3. If the task would cross repo boundaries, pause and ask.
4. Prefer read-only diagnosis, plans, and diffs before mutation.

## Migration status

This first pass ports the workflow architecture and core protocols into Codex form.
Exact external logic from Pedro Sant'Anna's `lit-review` workflow and Michael Ewens'
hook pattern is represented as safe placeholders unless it already existed locally.
