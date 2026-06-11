---
paths:
  - "**/*.do"
  - "**/*.R"
---

# Verification Protocol (Stata pipeline)

**Claude writes `.do` files; you run them. So Claude must build in the checks that catch errors when you run.** Never declare a step done on assumption.

## Build these checks into every `.do`

1. **After every `merge`:**
   ```stata
   merge m:1 id using "using.dta"
   tab _merge
   assert _merge != 2        // or document expected unmatched
   drop _merge
   ```
   Flag if >5% unmatched without a documented reason.
2. **After `keep`/`drop`/sample restriction:** `count` (compare to the expected N); `describe`/`codebook` the key variables.
3. **Claimed key uniqueness:** `isid <keyvars>` after a `reshape`/`collapse`/dedup.
4. **Before final output:** `summarize` the key variables (check ranges, unexpected missing); confirm the estimand and sample.
5. **Reproducibility:** the do-file opens a log, sets the seed (if random), defines its paths via a top `global`, and runs clean from a fresh `clear all`.

## When Claude can run it

For small, self-contained scripts Claude may run `stata-mp -b do script.do` (or `stata -b do …`) and read the `.log`. For large datasets, long loops, or interactive review, **generate the `.do` and ask the user to run it** — then verify against the log they return.

## Common pitfalls

- **`m:m` merges** — almost always a mistake; declare `1:1`/`m:1`/`1:m`.
- **Silent missing propagation** — `.` is treated as large in comparisons; guard `if` conditions.
- **Absolute paths** — break on every other machine; use a top `global` + relative paths.
- **Lost estimates** — console-only results vanish; `eststo`/`estimates save` then `esttab`/`outreg2`.

## Checklist

```
[ ] Every merge: kind declared, _merge inspected, dropped
[ ] count / isid after restrictions & reshapes
[ ] summarize key vars before output
[ ] log opened+closed; seed set; paths via global
[ ] estimates stored & exported (not console-only)
[ ] Reported results to user (or asked user to run + returned log checked)
```
