#!/usr/bin/env bash
# PreToolUse hook -- fires the SNDS R-portal provisioning gate + conventions into
# context whenever a .R/.r file is about to be edited/written, so the user is
# AUTOMATICALLY prompted through the RStudio access procedure (rules/snds-r-portal.md)
# instead of it just being documented.
# Non-blocking: emits PreToolUse additionalContext on a .R target, else nothing.
input=$(cat)
fp=$(printf '%s' "$input" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print(d.get('tool_input', {}).get('file_path', ''))
except Exception:
    print('')
" 2>/dev/null)

case "$fp" in
  *.R|*.r)
    read -r -d '' RULES <<'EOF'
SNDS R-PORTAL GATE -- surface to the user BEFORE producing runnable R (rules/snds-r-portal.md):
(0) PROVISIONING: R is NOT auto-provisioned on the CNAM portal -- a new habilitation has SAS Guide ONLY. Before writing/running R meant for the portal, CONFIRM the user has RStudio Workbench. If not: email support-national@assurance-maladie.fr, subject must contain [Création Habilitation RStudio], with portal login id(s) + portal connection email + région/profil(s); ~1-2 weeks; then the RStudio Workbench icon appears beside SASGuide 8; use R 4.4.3. (CNAM "Procedures d'acces a R sur le portail SNDS", 04/03/2026.) R can be AUTHORED locally now, but say plainly it cannot RUN on the portal until habilitation lands.
(1) PACKAGES: personal install.packages() is BLOCKED; request via subject [Création Demande de package RSTUDIO] (not immediate). Already in prod: fixest, brglm2, ROracle, DBI, data.table, dplyr, dbplyr, ggplot2, sandwich, lmtest, modelsummary, broom, glue, lubridate, haven, tidyverse. NOT in prod (flag if used): marginaleffects, survey, binsreg, logistf.
(2) MEMORY capped per user -> CNAM prescribes the hybrid: datamanagement in SAS, modelisation/graphique in R, push to the Oracle engine maximally; keep large claims tables server-side, pull only the small aggregated/cohort-level result into R; gc()/data.table when tight.
(3) STORAGE shared SAS<->R (ORAUSER/sasdata1/project) -> read SAS-built ORAUSER tables directly. Home RStudio tiny: NEVER save there (use sasdata1/project). ORAUSER is not storage: drop *_R tables after use. Max 3 sessions.
(4) ORACLE-from-R: connect dbname="IPIAMPR2.WORLD" (TZ/ORA_SDTZ=Europe/Paris); UPPERCASE Oracle names; pure ASCII; two-step date rule (all-Oracle filter -> pull small -> DATEPART in R, never push date funcs into Oracle); filter FLX_DIS_DTD; GROUP BY raw cols only. Same disclosure discipline as SAS on anything R exports. Reuse a shared R/ helpers module if the project has one.
EOF
    python3 -c "
import json, sys
print(json.dumps({'hookSpecificOutput': {'hookEventName': 'PreToolUse', 'additionalContext': sys.argv[1]}}))
" "$RULES"
    ;;
esac
exit 0
