---
name: audit-reproducibility
description: Cross-check manuscript numeric claims against actual analysis outputs and report pass or fail by tolerance. Use before submission, replication-package release, or after major analytical revisions.
---

# Audit Reproducibility

## Safety rules

1. Stay inside the active repo unless the user authorizes another outputs path.
2. Do not edit the manuscript or outputs unless the user explicitly asks.
3. If the outputs look stale, stop and ask before relying on them.

## Workflow

1. Read the local replication protocol or tolerance rules.
2. Extract numeric claims from the manuscript.
3. Extract matching results from the actual output files.
4. Match claim to result conservatively.
5. Apply tolerance checks and write a pass or fail audit memo.

## Output

- claim inventory
- unmatched claims list
- reproducibility audit report
- explicit note of any stale or missing outputs
