---
name: administrative-reimbursements
description: Administrative workflow for reimbursements, policy extraction, receipt intake, and document maintenance in Codex. Safe counterpart to the Claude administrative workflow.
---

# Administrative Reimbursements

## Safety rules

1. Do not inspect receipt folders outside the active repo unless the user authorizes them.
2. Do not move, rename, or file receipts unless the user explicitly authorizes it.
3. Do not write forms, ledgers, or CV updates unless the user explicitly authorizes the edit.

## Core capabilities

- extract a reimbursement policy into a structured rulebook
- classify a receipt
- identify possible duplicates
- prepare a claim checklist
- update a source-grounded administrative document

## Policy-ingestion rule

If the policy is ambiguous, preserve uncertainty explicitly rather than inventing a rule.
