---
name: validate-bib
description: Validate bibliography structure, missing keys, unused entries, drift, and optionally DOI consistency. Use for lecture decks, papers, or bibliography cleanup.
---

# Validate Bibliography

## Safety rules

1. Do not edit the bibliography unless explicitly authorized.
2. Verify citations before accusing an entry of being wrong.
3. If web DOI checks are needed, label that network verification was used.

## Workflow

1. Extract cited keys from project files.
2. Cross-check against bibliography entries.
3. Flag missing, unused, malformed, or duplicate entries.
4. Optionally run deeper semantic or DOI checks.
