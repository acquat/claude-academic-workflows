---
paths:
  - "**/*.sas"
  - "**/*.R"
---

# Verification Protocol (SNDS pipeline)

**You cannot iteratively debug on the portal. Verify defensively at every step; never declare a step done on assumption.**

## After every `CREATE TABLE` (mandatory — both steps)

```sas
proc contents data=ORAUSER.my_table; run;                /* structure + types */
proc sql;
  select count(*) as num_obs,
         count(distinct BEN_NIR_PSA) as n_patients       /* or the relevant id */
  from ORAUSER.my_table;
quit;
```

For derived rate/score tables, add a range check (`min`, `max`, `nmiss`) and confirm the values are in the expected support (e.g. a rate in `[0,1]`; missing only for the expected singletons).

## Before exporting anything from the enclave

1. **Disclosure check** — every cell respects the minimum-cell-size rule (see `snds-data-security.md`); no identifier columns present; complementary suppression applied. State the check in a comment.
2. **No PII in the artifact or in the `.log`.**

## For R scripts

1. Run the script; confirm output files were created with non-zero size.
2. **Validate merges** — `table(merge_indicator)`; flag if >5% unmatched.
3. Confirm panel balance / unit-of-analysis after each transformation.
4. Spot-check estimates for reasonable magnitude.

## Common pitfalls

- **Full table scan** — querying a claims table on `EXE_SOI_DTD` instead of the partition key `FLX_DIS_DTD`.
- **Silent duplicates** — a composite join missing a key; catch it with the distinct-id count.
- **Sentinel dates** — `'01JAN1600'dt` not cleaned before `intck`/`yrdif`.
- **Left-behind scratch** — intermediary `_v2` tables not dropped, eating the shared quota.

## Checklist

```
[ ] proc contents + count(*)/count(distinct id) after each CREATE TABLE
[ ] Partition-key filter (FLX_DIS_DTD) on claims queries
[ ] Composite joins use the full key set
[ ] Sentinel dates cleaned before arithmetic
[ ] No PII in logs / flat files / shared mounts
[ ] Disclosure check passed before any export
[ ] Intermediary tables dropped (quota)
[ ] Reported results to user
```
