---
name: empirical-coding-discipline
description: Enforces careful empirical coding: confirm units of observation, verify identifiers, audit merges, report counts, and never brute-force or silently drop observations.
---

# Empirical Coding Discipline

## Before coding

1. Verify the unit of observation.
2. Verify the identifiers and their uniqueness.
3. Confirm the upstream source data and script dependencies.
4. Ask before making consequential design choices.

## During coding

1. Check variable names against the actual data, not memory.
2. Audit every merge and report match rates.
3. Log counts, ranges, and missingness at each major stage.
4. Never use unexplained constants.

## After coding

1. Read the logs.
2. Sanity-check derived variables.
3. Compare against known benchmarks where available.

## Safety interaction

If the needed data or upstream scripts live outside the current local repo, ask before reading them.
