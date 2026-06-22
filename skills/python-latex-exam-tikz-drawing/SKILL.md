---
name: python-latex-exam-tikz-drawing
description: Exam-ready LaTeX TikZ drawing workflow for Vietnamese math generators. Use when Codex must create, repair, review, or preserve figures in a Python-LaTeX exam problem, including figures in the stem or solution, geometry diagrams, coordinate axes, function graphs, shaded regions, variation tables drawn with TikZ/tkz-tab, or when a user provides an image/PDF/DOCX prompt and asks to draw the figure exactly in TikZ.
---

# Python Latex Exam Tikz Drawing

## Role

Use this skill whenever an exam problem has a figure that must be drawn or preserved with TikZ. Pair it with `python-latex-exam-master` and the relevant domain solver when the drawing is part of a generated Python-LaTeX question.

This skill is not only about making compilable TikZ. It is about reproducing the user's visual contract: placement, proportions, labels, hidden/visible edges, helper marks, shading, and the level of detail shown in the stem or solution.

## Required Reference Routing

Before drawing, repairing, or reviewing a figure, read the relevant references below. Do not rely on this `SKILL.md` alone.

- Read [output-contract.md](./references/output-contract.md) for the strict TikZ output contract copied from the user's DOCX prompt.
- Read [drawing-workflow.md](./references/drawing-workflow.md) for the required step-by-step workflow from image/sample to final TikZ.
- Read [tikz-techniques.md](./references/tikz-techniques.md) for point declarations, intersections, perpendiculars, curves, solids, fills, axes, graphs, and tables distilled from the user's PDF.
- Read [exam-style-checklist.md](./references/exam-style-checklist.md) before finishing to catch layout and house-style mistakes.
- When labels contain mathematical notation, units, intervals, probabilities, vectors, distances, or function symbols, obey the master standard [trinh-bay-cong-thuc-full.md](../python-latex-exam-master/references/trinh-bay-cong-thuc-full.md).

If the task is a Python generator, also inspect `old_file_new/` for a same-code or same-type sample before writing the figure function. Preserve the old layout rhythm unless the user explicitly asks to change it.

## Workflow

1. Identify whether the figure belongs under the stem, inside the solution, or beside text. Use `minipage` only when the sample places the figure beside text.
2. Treat any reference image as the source of truth. Match its orientation, proportions, spacing, visible/hidden edges, labels, and helper marks before optimizing anything.
3. Sketch the coordinate model mentally first: declare named points, then draw fills/hidden parts, visible outlines, helper lines, points, and labels in that order.
4. Keep mathematical data separate from display labels in Python generators. Randomized labels may change, but the geometry must remain visually stable unless the user asks for scaled drawing.
5. Use explicit `\coordinate` declarations for important points. Use TikZ calc ratios only for real midpoints/projections/ratios.
6. For 3D solids, choose a projection that keeps helper points readable. If a label is important, move geometry slightly rather than masking it with white backgrounds unless the user requests that.
7. For graph/axis figures, choose domain, samples, scale, and dashed guide lines deliberately; do not let plots overflow the exam layout.
8. Compile or inspect generated `.tex` after nontrivial figure edits. Fix TikZ syntax before finalizing.

## Non-Negotiables

- Do not stylize, simplify, or "improve" a reference figure against the sample.
- Do not add extra mathematical objects not present in the sample or required by the solution.
- Do not use white label backgrounds or visual hacks unless the user explicitly approves them.
- Do not delete and rewrite an entire problem file just to fix one figure.
- Keep labels in math mode and keep Vietnamese exam style clean and uncluttered.
- Keep stem figures clean; solution figures may add helper lines/points only when the sample solution does so.
