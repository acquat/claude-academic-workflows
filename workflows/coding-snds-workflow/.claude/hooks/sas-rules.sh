#!/usr/bin/env bash
# PreToolUse hook -- fires the SAS/SNDS coding rules into context whenever a .sas
# file is about to be edited/written, so the conventions in
# rules/sas-sql-conventions.md are ACTUALLY APPLIED (not just documented).
# Non-blocking: emits PreToolUse additionalContext on a .sas target, else nothing.
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
  *.sas)
    read -r -d '' RULES <<'EOF'
SAS/SNDS coding rules -- APPLY NOW before editing this .sas file (rules/sas-sql-conventions.md):
(0) ORACLE TABLE *AND COLUMN* NAMES MUST START WITH A LETTER. Any ORAUSER/ORAVUE table OR column name beginning with "_" (or a digit) is ILLEGAL in Oracle -> ORA-00911 "caractere non valide", the CREATE fails, SAS flips to OBS=0/NOEXEC and the WHOLE step cascades. SAS WORK allows leading "_"; Oracle does NOT. So when you move/stage a WORK table into ORAUSER, rename BOTH the leading-underscore table name AND any leading-underscore COLUMN alias (e.g. `_pp`->`tmp_pp`; `0 AS _dummy_end`->`0 AS dummy_end`; `CASE ... AS _HAS_DEATH`->`AS HAS_DEATH`). Beware `SELECT * FROM WORK.x` into ORAUSER -- if WORK.x has a `_col`, that column becomes an illegal Oracle column. Allowed Oracle chars: letters, digits, _, $, # (but never leading _/digit); keep <=30 chars. Leave WORK._x names/cols alone. Guard: `grep -rniE '(orauser|oravue)\._' *.sas` (tables) AND `grep -rniE 'AS +_[a-z]' *.sas` (column aliases) must be empty.
(1) JOINS MUST BE HOMOGENEOUS -- ALL-WORK or ALL-Oracle (CNAM bonnes pratiques SAS, doc 7: "il est indispensable de deplacer une table personnelle SAS dans Oracle ... avant de la joindre avec une autre table Oracle"; FAQ "jointures homogenes"). To join a WORK table to an Oracle (ORAUSER/ORAVUE) table, either (a) move/copy the WORK table INTO ORAUSER (letter-led name, rule 0) so the join is all-Oracle, or (b) pull the relevant Oracle slice INTO WORK and join all-WORK (the right choice when you need SAS-side funcs like DATEPART). If you move one partner to ORAUSER, move ALL partners. (A read-one-write-one SET / CREATE-AS-SELECT from ONE table is NOT a merge -- allowed across libs.) STORAGE: SASDATA1/WORK has PER-USER QUOTAS; ORAUSER has NO individual quota but is a SHARED, CONSTRAINED space that saturates -- CNAM emails users to delete, and ORAUSER tables are NOT preserved. So both spaces are limited: stage for HOMOGENEITY (not size), keep footprints small, and ALWAYS delete ORAUSER intermediaries at end (proc datasets lib=ORAUSER; delete ...).
(2) PRE-FLIGHT before any DROP: row-touch each required input (select count(*) from t(obs=1)); %abort cancel if unreachable/empty. NOT %sysfunc(exist) (a VPD outage makes exist() lie).
(3) FAIL-FAST: %if &SQLRC >= 8 %then %abort cancel; after every CREATE/INSERT.
(4) %put: exactly ONE terminating semicolon, NONE inside the text (recurring ERROR 180).
(5) ORACLE: filter FLX_DIS_DTD (partition key, not EXE_SOI_DTD); half-open RANGE, never = "01JANyyyy"d; VERIFY column TYPE (FLX_DIS_DTD/EXE_SOI_DTD are DATETIME, EXE_SOI_AMD is CHAR $6); GROUP BY raw columns only (an expression vs an Oracle table triggers a remerge that pulls the whole table into WORK).
(6) BATCH: outpath ABSOLUTE (your sasdata1 output dir, e.g. /home/sas/<id>/sasdata/sasdata1/sasuser/output); NO proc printto (async auto-creates the .log).
(7) SAFE-REPLACE final tables: build _v2 -> verify rows>0 & exist() -> drop original -> rename. Verify after each CREATE (proc contents + count(*)).
(8) FRESHNESS != existence: a table can exist but be stale (old schema/arm). When reading a rebuilt project table, confirm it is THIS run's (arm/version suffix matches; schema has the new columns).
EOF
    python3 -c "
import json, sys
print(json.dumps({'hookSpecificOutput': {'hookEventName': 'PreToolUse', 'additionalContext': sys.argv[1]}}))
" "$RULES"
    ;;
esac
exit 0
