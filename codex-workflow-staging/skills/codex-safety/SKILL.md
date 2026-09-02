---
name: codex-safety
description: Mandatory safety protocol for this academic Codex workflow. Use whenever a task may inspect folders, read files outside the current repo, or edit anything. Enforces ask-before-leaving-repo and ask-before-editing behavior.
---

# Codex Safety

This is the governing skill for the entire bundle.

## Non-negotiables

1. Treat the current local project repository as the default boundary.
2. Do not inspect folders outside that repo unless the user explicitly authorizes it.
3. Do not edit files unless the user explicitly authorizes the edit.
4. When a request is ambiguous about scope, stay read-only and ask before crossing boundaries.
5. Prefer plans, diagnostics, and proposed diffs before mutation.

## Boundary rule

If a task would touch any path outside the active project repo:

- stop
- state which path would be accessed
- ask for permission first

Having filesystem capability is not the same thing as having workflow permission.

## Edit rule

Unless the user explicitly asks for edits, remain in one of these modes:

- explain
- review
- audit
- outline
- prepare a patch without applying it

## Default stance

- Read local project files only
- Do not browse sibling folders
- Do not infer consent from convenience
- If unsure, ask

## How other skills should use this

Every skill in this bundle should assume `codex-safety` is active.
If another skill's instructions conflict with this one, this skill wins.
