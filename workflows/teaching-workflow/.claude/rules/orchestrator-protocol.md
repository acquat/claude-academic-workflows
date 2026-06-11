# Orchestrator: After Approval, Work Autonomously

Once a plan is approved, execute it end-to-end. Don't check in at every step; check in when it's done or when you're genuinely blocked.

**The cycle:** implement → **verify** (compile / run / open the actual output) → **review** (run the matching review pass — the supervise-project lenses or the verification-protocol checklist) → **fix** what review found, worst first → verify again → **score** against [quality-gates.md](quality-gates.md).

- Score at or above the gate → present a summary and stop.
- Below the gate → another review-fix round, **up to 5 rounds**, then present honestly with what remains.
- Verification failing twice in a row → stop and surface the blocker. Don't thrash.

**"Just do it"** from the user removes the final approval pause — never the verification or the review.
