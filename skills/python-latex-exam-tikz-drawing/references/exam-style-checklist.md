# Exam Figure Style Checklist

Read this before finalizing a figure.

## Layout

- Figure below statement: do not use `minipage`; place with `\begin{center}` or the file's existing pattern.
- Figure beside statement: use `minipage` only if the sample actually places figure beside text.
- Do not add extra vertical/horizontal whitespace unless the sample needs it.
- Keep stem figure clean and solution figure explanatory.

## Fidelity

- Match the sample's proportions before trying to make the figure mathematically prettier.
- Keep helper points exactly where the solution needs them.
- Keep dashed lines dashed, visible edges solid, and fills behind outlines.
- Do not add white backgrounds to labels unless the user approves.
- For decorative figures, such as leaves or real-world objects, trace the user's shape closely rather than drawing a generic version.

## Python Generator Rules

- Write a dedicated `ve_hinh_...(...)` helper when the figure is nontrivial.
- Keep randomized display labels separate from coordinates if the user wants a stable drawing.
- Use local helpers already present in the project for LaTeX display, such as `tinh_latex(...)` and `lam_tron(...)`; do not invent duplicate formatters.
- Patch only the requested part of an existing figure when doing revisions.
- Avoid nested f-strings in sensitive TikZ/Python strings; prepare intermediate display variables first.

## Notation Check

- Labels and annotations must obey [trinh-bay-cong-thuc-full.md](../../python-latex-exam-master/references/trinh-bay-cong-thuc-full.md): math mode, upright units, decimal commas, vector symbols, distance notation, `\parallel`, `\perp`, and `^\circ`.
- Do not use `//`, `90^0`, raw `dx`, or ad hoc probability/combinatorics notation in figure labels.

## TikZ Syntax Check

- Every `\begin{tikzpicture}` has an `\end{tikzpicture}`.
- Every command ends with `;`.
- Braces, parentheses, and TikZ calc delimiters are balanced.
- Labels use math mode.
- Coordinates with primes are named safely if the local compiler dislikes `(A')`; prefer `(Ap)` while displaying `$A'$` if needed.
- Required libraries are already loaded by the project; if a figure needs `patterns`, `intersections`, or `angles`, verify the project preamble supports it.
