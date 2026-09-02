---
name: currency-convert
description: Fetch a dated reference exchange rate and convert an amount for reimbursement or record-keeping tasks, while documenting the source and fallback date if needed.
---

# Currency Convert

## Safety rules

1. Do not write converted amounts into any form or ledger unless explicitly authorized.
2. If the institution mandates a rate source, use that source rather than guessing.
3. Note fallback dates for weekends or holidays explicitly.

## Workflow

1. Parse date, amount, and currency.
2. Fetch the reference rate from the required source.
3. Convert with direction stated explicitly.
4. Return a paste-ready record with source and effective date.
