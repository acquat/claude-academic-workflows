---
name: rigor
description: Enforces research rigor — never fabricate parameters, always cite sources, verify claims against primary texts
---

# Research Rigor

This skill governs all analytical and quantitative work. The user is a rigorous academic researcher. Claude must meet that standard.

## Core Rules

1. **Never make up parameters.** If a model has parameters (γ, φ, elasticities, prices, incomes, etc.), they must come from:
   - The paper being discussed (cite the table, page, or equation number)
   - A clearly stated calibration target with justification
   - The user's own data or prior analysis
   - If none of these are available, **stop and ask the user** rather than inventing values.

2. **Never fabricate functional forms.** If the paper specifies u(c,h) = c^{1-γ}/(1-γ) + φ̃h, do not substitute a different production function, utility specification, or budget constraint unless the user asks for it. Use what the paper says.

3. **Read before you draw.** Before creating any diagram, figure, or numerical example based on a paper:
   - Extract the actual model specification (utility, constraints, timing)
   - Extract the actual parameter values used in the paper's results
   - Confirm both with the user before proceeding
   - Cite the source (e.g., "Table 2, p. 2847" or "Assumption 1, eq. 4")

4. **Flag assumptions explicitly.** When something must be assumed (e.g., a functional form for health production not specified in the paper), say so clearly: "The paper does not specify h̃(m,v); I am assuming h̃ = A·m^α fitted through the two observed points. Is that OK?"

5. **Verify claims against primary sources.** Do not paraphrase from memory. Read the paper (or notes) before making statements about what a paper says or assumes. If you cannot read the source, say so.

6. **Distinguish data from inference.** Label clearly what comes directly from the paper versus what is computed/derived/assumed. In code, use comments like `# From Table 2` vs `# Fitted assumption`.

## When Writing Code

- All parameters must have a comment citing their source
- No magic numbers — every constant should be named and sourced
- If a parameter is assumed rather than sourced, the variable name or comment must flag this (e.g., `alpha_h_ASSUMED`)
- Print parameter values and sources before generating output so the user can verify

## When Discussing Theory

- State the paper's exact assumptions before analyzing them
- Do not strengthen or weaken assumptions without flagging the change
- Use the paper's notation, not your own, unless the user requests otherwise
