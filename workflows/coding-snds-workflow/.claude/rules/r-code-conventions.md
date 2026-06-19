---
paths:
  - "**/*.R"
  - "**/*.r"
  - "R/**"
---

# R Code Standards (SNDS downstream analysis)

**Standard:** Senior Principal Data Engineer + PhD researcher quality. Applies to the R that runs
*after* the SAS/Oracle datamanagement — merges, models, tables, figures. R that touches Oracle or
exports anything is also bound by [`snds-r-portal.md`](snds-r-portal.md) (provisioning, hybrid,
two-step date rule) and the disclosure rules in [`snds-data-security.md`](snds-data-security.md) /
[`export-compliance.md`](export-compliance.md).

---

## 1. Reproducibility

- `set.seed()` called ONCE at top (YYYYMMDD format).
- All packages loaded at top via `library()` (not `require()`) — and **all on the portal prod list**
  (see [`snds-r-portal.md`](snds-r-portal.md) §1; flag any package not yet provisioned).
- All paths relative to the project root; never the tiny RStudio Home — write RDS/outputs to
  sasdata1 or a project space.
- `dir.create(..., recursive = TRUE)` for output directories.

## 2. Function Design

- `snake_case` naming, verb-noun pattern.
- Roxygen-style documentation.
- Default parameters, no magic numbers.
- Named return values (lists or tibbles).

## 3. Domain Correctness

<!-- Customize for your project's known pitfalls -->
- Estimator implementations match the paper / specification formulas (cite the equation).
- Standard errors use the appropriate method (cluster/robust where the design calls for it).
- Treatment effects are the correct estimand (e.g. ATT vs ATE).
- Document known package bugs below in Common Pitfalls.

## 4. Visual Identity

```r
# --- Institution / project palette (REPLACE with yours) ---
primary_blue   <- "#012169"   # example values only
primary_gold   <- "#f2a900"
accent_gray    <- "#525252"
positive_green <- "#15803d"
negative_red   <- "#b91c1c"
```

### Custom Theme
```r
theme_custom <- function(base_size = 14) {
  theme_minimal(base_size = base_size) +
    theme(
      plot.title = element_text(face = "bold", color = primary_blue),
      legend.position = "bottom"
    )
}
```

### Figure dimensions
```r
ggsave(filepath, width = 8, height = 5)   # explicit dims; add bg = "transparent" if the
                                          # target background is not white
```

## 5. RDS Data Pattern

**Heavy computation (Oracle pulls, model fits) is saved as RDS; downstream steps (tables, figures,
the paper) load the pre-computed object** — never re-run the expensive pull. This is the R side of
the SNDS hybrid: keep the big work server-side, materialize the small result once.

```r
saveRDS(result, file.path(out_dir, "descriptive_name.rds"))
```

## 6. Common Pitfalls

<!-- Add your project-specific pitfalls here -->
| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Hardcoded / Home paths | Breaks on the portal; Home is system-reserved | Relative paths; write to sasdata1/project |
| Pushing R/SAS date funcs into Oracle SQL | Silent NULL | Two-step date rule (filter in Oracle, derive dates in R) |
| Package not on the prod list | Script can't run on the portal | Check `snds-r-portal.md` §1; request before depending on it |

## 7. Line Length & Mathematical Exceptions

**Standard:** keep lines <= 100 characters.

**Exception: mathematical formulas** — lines may exceed 100 chars **if and only if** (1) breaking
the line would harm readability of the math (influence functions, matrix ops, formula
implementations matching paper equations); (2) an inline comment explains the operation; (3) the
line is in a numerically intensive section (estimation/inference). Long lines in non-mathematical
code: minor penalty. Long lines in documented mathematical sections: no penalty.

## 8. Code Quality Checklist

```
[ ] Packages at top via library() — all on the portal prod list
[ ] set.seed() once at top
[ ] All paths relative; nothing written to Home
[ ] Functions documented (Roxygen)
[ ] Figures: explicit dimensions, consistent palette
[ ] RDS: every heavy result saved once, loaded downstream
[ ] Anything exported passes the disclosure gate (>= 11, no identifiers)
[ ] Comments explain WHY not WHAT
```
