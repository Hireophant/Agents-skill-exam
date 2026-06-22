# Strict TikZ Output Contract

This reference comes from the user's `PROMPT CODE TIKZ LATEX.docx`. Follow it whenever the task is specifically to output a standalone TikZ figure or to write a TikZ helper function.

## Output Rules

- Output valid TikZ code only when the user asks for only the figure code.
- Start standalone output with `\begin{tikzpicture}` and end with `\end{tikzpicture}`.
- Do not include `\documentclass`, `\begin{document}`, prose, Markdown fences, or text before/after the figure when standalone TikZ is requested.
- In Python generators, return the TikZ block as a string in the existing file style instead of adding document wrappers.

## Style Conventions

- Use a compact option set such as `[scale=..., line join=round, line cap=round, >=stealth]`.
- Use `line width=1.0pt` or the local file's established width unless the sample needs thinner helper lines.
- Define important points with `\coordinate (A) at (...);`.
- Prefer explicit coordinates. Use `$(A)!t!(B)$` only for meaningful midpoints, ratios, projections, or interpolation.
- Use solid lines for visible edges and dashed lines for hidden edges, guide lines, projections, or construction lines.
- Draw points with `\fill` or `\filldraw` only when the sample shows marked points.
- Put labels in math mode: `$A$`, `$O$`, `$x$`, `$\alpha$`, and follow the master notation standard for symbols/units in labels.
- Default to black. Add colors, opacity, patterns, or fills only when the sample or mathematical meaning requires them.

## Geometry Rules

- Preserve relative proportions, orientation, symmetry, and alignment from the reference image.
- Maintain parallelism and perpendicularity shown in the sample.
- If the image is ambiguous, choose the simplest consistent geometry and keep it exam-readable.
- Do not invent extra elements, decorations, or hidden meanings.
- Avoid unnecessary styling, shadows, gradients, and decorative effects unless the original figure has them.

## Mathematical Typography

For any mathematical label or annotation, obey [trinh-bay-cong-thuc-full.md](../../python-latex-exam-master/references/trinh-bay-cong-thuc-full.md). This includes math mode, decimal commas, upright units, vector notation, `\parallel`, `\perp`, and degree notation.

- Use standard notation and consistent vector notation such as `\overrightarrow{AB}` when labels require it.
- Keep labels readable and avoid overlaps by moving the label anchor or nudging coordinates, not by changing the mathematics.
