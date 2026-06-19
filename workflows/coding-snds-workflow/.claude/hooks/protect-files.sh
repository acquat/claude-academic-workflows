#!/usr/bin/env bash
# PreToolUse hook -- block accidental Edit/Write to protected files (basename match).
# Primary use: enforce a read-only RA / co-analyst pipeline handoff (snds-data-security.md
# section 4) -- mark their pipeline files protected so all your edits land in your own writable
# folder, never in someone else's file in place.
# Exit 2 BLOCKS the edit (reason printed to stderr); exit 0 allows it.
input=$(cat)
fp=$(printf '%s' "$input" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print(d.get('tool_input', {}).get('file_path', ''))
except Exception:
    print('')
" 2>/dev/null)

# No file path -> not a file operation, allow.
[ -z "$fp" ] && exit 0

# ============================================================
# CUSTOMIZE: basenames (or full paths) to protect for this project.
# Basename matching by default -- add a full path for more precision.
# ============================================================
PROTECTED_PATTERNS=(
  "settings.json"
  # "Bibliography_base.bib"      # example: a shared bibliography
  # "01_extract_cohort.sas"      # example: an RA-owned pipeline file (read-only handoff)
)

base=$(basename "$fp")
for pat in "${PROTECTED_PATTERNS[@]}"; do
  if [[ "$base" == "$pat" ]]; then
    echo "Protected file: $base -- edit it manually, or remove it from PROTECTED_PATTERNS in .claude/hooks/protect-files.sh." >&2
    exit 2
  fi
done

exit 0
