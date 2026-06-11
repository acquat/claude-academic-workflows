---
paths:
  - "**/*.tex"
---

# Paper Writing Conventions

> Fill this in per manuscript. The point is a **fixed notation registry** and consistent
> citation/theorem/figure conventions, so notation never drifts across sections or sessions.
> For theory papers especially, the notation registry is load-bearing — pin it here on day one.

## Notation Registry

The following notation is fixed. **Never introduce alternative symbols without author approval.**

| Symbol | LaTeX | Meaning |
|---|---|---|
| [e.g. θ] | `\theta` | [meaning; domain] |
| [e.g. α] | `\alpha` | [meaning; domain] |
| … | … | … |

**Critical conventions** (call out the easy-to-confuse ones): e.g. "the [X] parameter is **[symbol]**, never [other symbol] — never substitute."

## Citation Style

- Package: `natbib` with `authoryear` (or your journal's requirement).
- Textual: `\citet{key}` → "Author (Year)". Parenthetical: `\citep{key}` → "(Author, Year)".
- Never use bare `\cite{key}`.
- Bibliography file: `[path/to/references.bib]`.
- Style: `\bibliographystyle{[aer / econometrica / jeea / …]}`.

## Theorem Environments

Defined in the preamble; use exactly these names: `theorem`, `proposition`, `lemma`, `corollary`, `definition`, `assumption`, `proof`. Label everything (`\label{prop:name}`) and cross-reference (`\ref{prop:name}`).

## Journal Standards ([TARGET] target)

- Abstract: under [N] words.
- JEL codes / keywords: [required? current set?].
- Author affiliation + contact: [...].
- Acknowledgements: [title-page footnote, not abstract].

## Figure Conventions

- Format: PDF/PNG, 300+ DPI. Theory figures B/W with clear axis labels; empirical figures consistent palette, all axes labeled.
- Every figure: `\caption{}` + `\label{fig:name}`, referenced in text.
- Figures stored in `[path]`; `\graphicspath` set accordingly.

## Multi-File Structure

- Main file to compile: `[path/to/main.tex]`.
- Inputs / appendices: [`\input{}`-ed separately, or inline — state which].
- Compile sequence: see `verification-protocol.md` (3-pass LaTeX + bibtex).
