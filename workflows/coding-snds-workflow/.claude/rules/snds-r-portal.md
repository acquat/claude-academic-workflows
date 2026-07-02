---
paths:
  - "**/*.R"
  - "**/*.r"
  - "R/**"
---

# SNDS R Portal — Provisioning Gate + Conventions

**Trigger this whenever the user asks to write, run, port, or debug ANY R for an SNDS project.**

---

## 0. PROVISIONING GATE (surface this FIRST, before writing/running R)

R is **not** provisioned automatically on the CNAM SNDS portal. A new habilitation gets **only
SAS Guide** — R/RStudio must be requested separately. **Before producing R that is meant to run on
the portal, confirm the user has RStudio Workbench provisioned.** If it is not confirmed, surface
this procedure and offer to help draft the request:

> **Request RStudio Workbench** — email **support-national@assurance-maladie.fr**, subject must
> contain **`[Création Habilitation RStudio]`**, providing: portal login id(s), portal connection
> email, and the **région + profil(s)** for R access (one request can batch several users of an
> institution; internal Assurance-Maladie users go via the S@M app). Habilitation lands in **~1–2
> weeks**; the **RStudio Workbench** icon then appears beside SASGuide 8. Use R **4.4.3**.

Authoritative source: CNAM communiqué *"Procédures d'accès à R sur le portail SNDS"* (04/03/2026).
Writing R *code* locally with Claude Code is fine before provisioning — but say plainly that it
**cannot be run on the portal** until the habilitation lands, so we don't imply it's runnable.

## 1. Packages — gated; request before you depend on one

Personal `install.packages()` is **BLOCKED** on the portal. New packages are requested via
support-national, subject **`[Création Demande de package RSTUDIO]`** (security-reviewed; NOT
installed immediately). The live list is on the portal Accueil → "Pour votre information".

Already in CNAM prod (`Packages_R_prod_17112025.xlsx`, verified 2026-06-18): **fixest**, **brglm2**
(Firth), ROracle, DBI, data.table, dplyr, dbplyr, ggplot2, sandwich, lmtest, modelsummary, broom,
glue, lubridate, haven, tidyverse. **Not** in prod (request first, or flag before using):
`marginaleffects`, `survey`, `binsreg`, `logistf`. → Don't write code that depends on an
un-provisioned package without flagging it to the user.

⚠️ **A prod package can differ from CRAN in which functions it EXPORTS.** Observed: CNAM-prod
`lubridate` does **not** export `months()` (`lubridate::months(n)` → *"'months' n'est un objet
exporté…"*) — use the core constructor `lubridate::period(n, units = "month")` instead. Prefer the
most-core constructor over convenience aliases (`months()`, `days()`, `years()`) in portal code.

## 2. Operational constraints (CNAM Accès-à-R guide)

- **Per-user memory is capped** ("Cannot allocate memory" is common). CNAM's own prescription is a
  **hybrid**: **datamanagement in SAS, modélisation/graphique in R, push work to the Oracle engine
  maximally.** Keep the large claims tables server-side; pull only the small aggregated /
  cohort-level result (the analysis-ready extract) into R. **Aggregate a tens-of-millions-row table
  to the analysis grain IN Oracle (a raw-column `GROUP BY`, pushed down) and pull only the reduced
  result — never `dbGetQuery("SELECT * FROM <huge table>")`** (OOM). When a job holds several big
  intermediates, free each with `rm()` + `gc()` before the next (a loop that keeps every fit's
  design matrix alive is the classic OOM). Use `data.table` when tight.
- **Storage is shared SAS↔R** (sasdata1, project spaces, ORAUSER) → SAS-built ORAUSER tables can be
  read directly from R, no re-export.
- 🔴 **Home root is the shared CITRIX space, NOT your user space** (CNAM communiqué 17/03/2025,
  *"Espace saturé → Déplacement des tables R vers Rdata"*). Files R saves at `~/` **or in any
  user-created Home subfolder** fill the shared Citrix space (normally only
  `Citrix_documents`/`Citrix_PARTAGE-xx`), whose saturation has actually **blocked the portal-wide
  import/export tool.** So: **never** `saveRDS`/`ggsave`/`fwrite`/`dir.create` at `~/` or a Home
  subfolder — write to **`~/sasdata1/…`** or **`~/rdata/`** (a sasdata1 subfolder with a Home
  shortcut): `saveRDS(t, "~/rdata/x.RDS")`. Move strays with `file.copy("~/<f>", "~/rdata/<f>")`
  (folders: `+ recursive=TRUE`, destination must exist) then `file.remove("~/<f>")`.
- ⚠️ **`sasdata1`/`rdata` are quota-limited (default ~1 MB at account opening).** A disk/quota error
  on a big `saveRDS`/`ggsave`/`fwrite` means **request an extension** (externals email
  support-national, subject `[CREATION] Extension de Quota`, body = SNDS id + profil + région; AM
  internals via s@m national), **not** a code bug.
- **ORAUSER is not storage — drop any temp (`*_R`) table after use.** Max 3 simultaneous sessions.
- **Figures:** don't `print()` many ggplots to the RStudio Plots pane (portal render crash) —
  `ggsave` to `~/sasdata1`, then view via `rstudioapi::viewer()` on a `tempdir()` copy (or the Files
  pane → View File). One deliberate `print()` is fine; a loop of them is the hazard.

## 3. Conventions for R that hits Oracle (mirror the SAS discipline)

- Connect: `Sys.setenv(TZ="Europe/Paris", ORA_SDTZ="Europe/Paris"); DBI::dbConnect(DBI::dbDriver("Oracle"), dbname="IPIAMPR2.WORLD")`.
  Query with `DBI::dbGetQuery` (SQL) or `dplyr`/`dbplyr`.
- **Oracle table names UPPERCASE**, start with a letter. **Pure ASCII** in scripts (the portal is
  Latin-1).
- 🔴 **From R, your ORAUSER tables live in YOUR OWN Oracle schema (named after your portal id) —
  reference them UNQUALIFIED.** SAS's `ORAUSER` libname is just an alias for that personal schema;
  there is no Oracle schema literally called `ORAUSER`, so `SELECT … FROM ORAUSER.MY_TABLE` from R →
  **ORA-00942 "table inexistante"**. Use `SELECT … FROM MY_TABLE` (Oracle resolves unqualified names
  to your schema by default; no `ALTER SESSION` needed). A table R creates unqualified lands in your
  schema and SAS then sees it as `ORAUSER.<name>` (round-trips).
- ⚠️ **Oracle empty string `''` IS NULL.** A SAS blank-id filter translated literally →
  `TRIM(x) NOT IN ('','00000000')` expands to `… <> NULL …` = never true → **silently 0 rows**. Use
  `TRIM(x) IS NOT NULL` to drop blanks (plus `TRIM(x) <> '00000000'` for the placeholder); never
  `x <> ''` / `NOT IN ('' …)` in Oracle.
- **Two-step date rule:** do all-Oracle filtering with translatable predicates → pull the small
  result → derive DATEPART / year / interval expressions **in R**. Never push R/SAS date functions
  into Oracle SQL (they translate to a **silent NULL**). Filter on the **partition key**
  (`FLX_DIS_DTD`); **GROUP BY raw columns only**.
- ⚠️ **Code columns can read back as CHAR (and may be zero-padded) — normalize before comparing.**
  A nomenclature/specialty/type code pulled from Oracle is often character even when it "looks"
  numeric: `x == 13L` coerces and silently mismatches padded values (`"13"` vs `"013"`), and any
  sort/tie-break on the char column is **lexicographic** (`"13" < "2"`). Normalize once —
  `as.integer(trimws(as.character(x)))` — then compare/sort numerically. And put a fail-fast
  `stopifnot(nrow(sub) > 0)` **immediately after** building any filtered subset that could come
  back empty, so a mismatch aborts at the filter (minutes in), not at the model fit (hours in).
- Same disclosure discipline as SAS applies to anything R exports — identifier-class variables stay
  in the enclave and every export passes the ≥ 11 gate (see cross-references below).
- If your project has a shared `R/` helpers module (connect / query / export-gate wrappers), reuse
  it rather than re-rolling these per script.

## 4. The air-gapped run loop (paste-to-portal discipline)

The portal is air-gapped: local files don't reach it; code arrives by **pasting into the RStudio
editor**. Three consequences, each learned the hard way:

- **A locally-edited script or helper is STALE on the portal until re-pasted.** `source()` happily
  loads the old copy. Telltale symptom: a **newly added** function errors "could not find function"
  / *"fonction introuvable"* while long-standing functions from the same file work fine. Rule:
  **refresh every shared helper file on the portal before each run** that follows a local edit; in
  a live session, the quick recovery is pasting just the missing function into the console.
- **Make analysis scripts SELF-CONTAINED:** one `source()` must rebuild all state from the
  database — no dependence on objects left in the workspace by earlier console work. Portal
  sessions get killed (idle timeouts, Citrix drops, OOM); if the script is self-contained, a
  kicked session costs only the re-run time. Corollary: when console exploration produces
  something worth keeping (a new outcome, a figure), **fold it back into the script** rather than
  letting it live only in the session.
- **Top-level `on.exit()` is a footgun under `source()`:** each top-level statement is evaluated
  in its own function context, so the handler fires **immediately** after that one statement — an
  `on.exit(dbDisconnect(conn))` placed at the top kills the connection before the first query.
  Use an explicit disconnect at the end of the script, or wrap the pipeline in a function and put
  `on.exit()` inside it.

## 5. Cross-references
Generic R style (palette, ggsave dims, RDS pattern, checklist): [`r-code-conventions.md`](r-code-conventions.md) ·
Security + PII: [`snds-data-security.md`](snds-data-security.md) · Export gate (≥ 11, annex):
[`export-compliance.md`](export-compliance.md) · Oracle/SQL discipline (partition key, joins,
safe-replace): [`sas-sql-conventions.md`](sas-sql-conventions.md) · Project tables / code lists /
DUA threshold: [`references/snds-data.md`](../references/snds-data.md).
CNAM bonnes pratiques R: documentation-snds.health-data-hub.fr/snds/CNAM/bonnes_pratiques_r/.
