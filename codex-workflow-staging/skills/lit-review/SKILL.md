---
name: lit-review
description: Literature-review workflow for academic projects in Codex. Use when the user wants a literature search, synthesis, paper logging, citation-grounded notes, or a manuscript-positioning memo. Safe placeholder for Pedro Sant'Anna compatibility.
---

# Literature Review

This is the Codex-native counterpart to the literature-review layer referenced by the Claude workflows.

## Safety first

1. Do not search external folders for PDFs unless the user explicitly authorizes those paths.
2. Do not claim a paper says something unless the paper or user-provided notes were actually read.
3. Do not add citations or bibliography entries unless the user explicitly authorizes the edit.

## Workflow

1. Clarify the review target:
   - question
   - field
   - paper set or folder
   - output format
2. Build a structured note for each paper:
   - citation
   - question
   - data or theory
   - identification or mechanism
   - main findings
   - limitations
   - load-bearing claims with page anchors when available
3. Synthesize across papers:
   - common result
   - disagreement
   - methodological fault lines
   - gap for the user's project
4. If the project maintains `lit_review.md`, prepare proposed additions before editing.

## Pedro compatibility note

This skill is intentionally compatible in purpose with Pedro Sant'Anna's `lit-review` pattern,
but the exact external source logic is not bundled here. Use this as the safe native baseline.
