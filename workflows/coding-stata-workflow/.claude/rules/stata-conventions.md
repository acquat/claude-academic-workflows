---
paths:
  - "**/*.do"
---

# Stata Conventions

## File Header (Required)

Every .do file must start with:

```stata
/*=============================================================================
Project:    [PROJECT NAME]
Script:     [script_name.do]
Author:     [YOUR NAME]
Date:       [YYYY-MM-DD]
Purpose:    [One sentence: what this script does]
Inputs:     [List data inputs]
Outputs:    [List outputs: figures, tables, estimates]
=============================================================================*/

version 16
set more off
clear all
```

## Logging

```stata
log using "script_name.log", text replace
* ... analysis ...
log close
```

Every script must open a log at the top and close it at the end. No exceptions.

## Seeds

When randomization is involved:
```stata
set seed 12345
```
Place immediately after `clear all`.

## Paths

- Use **relative paths** from the script's location or the project root
- Never hardcode absolute paths (e.g., no machine-specific absolute paths)
- Reference data with paths like: `"../../data/file.dta"` or use a `global` at the top:

```stata
global root "/path/to/your/project"
global data "$root/DataWork/prospectiveness_OPPS"
```

If using globals, define them at the top of every script (not assumed from prior runs).

## Output

- Estimation tables: use `esttab` or `outreg2`; save to `.tex` or `.csv`
- Figures: `graph export "filename.png", replace width(1200)`
- Estimates: `estimates save "filename.ster", replace`

## Variable Naming

- Lowercase, underscores (e.g., `cost_charge_ratio`, `mgmt_score`)
- Label all variables: `label variable cost_charge_ratio "Cost-to-Charge Ratio"`
- Label values for categorical vars

## Comments

```stata
// Inline comment
/* Block comment */
*--- Section header ---*
```

## Mixed Workflow Protocol

- **Claude generates and edits .do files**
- **Claude runs small, self-contained scripts via CLI:** `stata-mp -b do script.do`
- **User runs major analyses in Stata GUI** (anything involving large datasets, loops >1000 obs, or interactive review)
- When in doubt: generate the .do file and ask user to run it
