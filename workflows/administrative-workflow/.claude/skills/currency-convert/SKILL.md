---
name: currency-convert
description: Fetch a reference exchange rate for a non-home currency on a specific date and convert an amount. Use when filing non-home-currency receipts, or when the user asks "what's the rate for [date]", "convert [amount] [currency]".
argument-hint: "[YYYY-MM-DD] [amount] [CCY]"
allowed-tools: ["Bash", "WebFetch"]
---

# /currency-convert

Fetch an official reference rate for a date and apply it. Default source: the **European Central Bank** daily reference rates. *(Swap for your own central bank / institution-mandated source if required — many institutions specify which rate to use.)*

## Instructions

1. **Parse args.** Required: `date` (YYYY-MM-DD). Optional: `amount`, `currency` (3-letter ISO, default per your home currency).
2. **Fetch the rate** for that date via WebFetch from the reference source. ECB historical reference rates are published per currency; for a non-business-day (weekend/holiday) **fall back to the prior business day** and note it.
3. **Compute the converted amount** if `amount` was provided. Be explicit about direction (e.g. "1 EUR = 1.0834 USD" → `EUR = USD_amount / 1.0834`).
4. **Output:**

```
Reference rate — <date> (<actual-rate-date> if fallback)
1 <home> = <rate> <currency>
Conversion: <amount> <currency> = <home> <converted>
Source: <url>
```

5. **If used during a claim, suggest pasting the rate row into the folder README:**
   `| <date> | <ccy>/<home> | <rate> | <url> |`

## Troubleshooting

- **No published rate for the date** — weekend/holiday: use the prior business day and document it.
- **Can't fetch** — note the source URL; ask the user to read the rate manually and record it in the folder README.
