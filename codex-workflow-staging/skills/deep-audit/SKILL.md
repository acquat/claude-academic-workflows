---
name: deep-audit
description: Run a repository-wide consistency audit covering documentation, code, counts, links, and cross-file claims. Use after broad changes, before releases, or when the user wants a whole-repo audit.
---

# Deep Audit

## Safety rules

1. Stay inside the active repo unless the user authorizes broader scope.
2. Audit first; do not auto-fix without explicit authorization.
3. Report findings with file references and severity.

## Audit surfaces

- documentation accuracy
- script and hook quality
- skill and rule consistency
- cross-document counts, names, and links

## Output

- prioritized findings
- open questions
- optional repair plan
