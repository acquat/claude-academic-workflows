---
name: intake
description: Classify a new receipt or claim-related document and propose where it belongs, while preserving the drop zone and surfacing policy red flags.
---

# Intake

## Safety rules

1. The intake folder is read-only unless the user explicitly authorizes a move.
2. Flag policy blockers rather than routing around them.
3. Do not silently classify low-confidence documents.

## Workflow

1. Resolve the target file.
2. Extract vendor, date, amount, currency, and category hints.
3. Check for duplicate risk and policy red flags.
4. Recommend the next step without moving the file.
