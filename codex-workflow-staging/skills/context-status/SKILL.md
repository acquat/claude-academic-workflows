---
name: context-status
description: Report Codex session health, active work state, and what has been preserved to disk. Use when checking progress, session hygiene, or whether a task needs summarization before continuing.
---

# Context Status

## Purpose

This is the Codex-safe counterpart to Claude's context-monitoring workflow.

## What to report

1. Current task boundary
2. Active plan or working memo
3. Files recently changed or reviewed
4. Any pending verification or deferred permission request

## Constraint

Do not inspect external session folders unless the user explicitly authorizes that path.
