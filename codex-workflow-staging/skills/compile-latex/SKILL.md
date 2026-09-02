---
name: compile-latex
description: Compile a LaTeX or Beamer document with the project's required engine and pass structure, then report warnings, unresolved citations, and obvious compile issues.
---

# Compile LaTex

## Safety rules

1. Only compile within the active repo unless the user authorizes another path.
2. Do not edit TeX sources unless the user explicitly asks.
3. If compilation would require external resources or unusual paths, pause and ask.

## Protocol

1. Identify the authoritative `.tex` file and expected engine.
2. Run the minimum reliable compile sequence for the project.
3. Check warnings, unresolved citations, and reference churn.
4. Report the result and any likely fixes.

## Default stance

Compilation is verification, not permission to rewrite the document.
