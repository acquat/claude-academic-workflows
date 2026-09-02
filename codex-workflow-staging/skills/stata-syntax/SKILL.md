---
name: stata-syntax
description: Stata-writing protocol for Codex. Use before writing or editing Stata code. Read the local syntax reference first, then targeted official documentation if needed, and never guess syntax.
---

# Stata Syntax

## Safety rules

1. Do not inspect Stata docs outside the local project repo unless the user authorizes the docs path.
2. Do not edit `.do` files unless the user explicitly authorizes the edit.
3. Never guess Stata syntax.

## Protocol

1. Read the local syntax reference if the project has one.
2. If the reference is incomplete, ask for the official docs path or the relevant help-file output.
3. Verify the exact command syntax before writing code.
4. If the project keeps a syntax reference, prepare a proposed append before editing it.

## Writing rule

Every non-trivial Stata block should be grounded in a verified reference, not recollection.
