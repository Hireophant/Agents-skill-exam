---
name: python-latex-exam-hh-gan-truc-solver
description: HH gan truc/Oxyz coordinate-geometry solver for Python-LaTeX exam questions. Use with python-latex-exam-master when the user sends an image, question stem, code file, or file name indicating HH gan truc, Oxyz, coordinate geometry, vectors, points, lines, planes, spheres, distances, angles, real-world 3D coordinate models, motion, optimization, costs, MC Oxyz, TF Oxyz, or SA Oxyz. Read only this solver's local references for coordinate geometry strategy.
---

# Python Latex Exam HH Gan Truc Solver

## Required Pairing

Always pair this solver with `python-latex-exam-master` for common LaTeX, presentation, randomization, and figure-style rules.

## Use When

Use this skill for geometry problems where a coordinate system, Oxyz model, vector formula, line/plane/sphere equation, or practical 3D coordinate model is the intended method.

## Workflow

1. Decide whether the item is MC, TF, or SA from the prompt, image, or file name.
2. Read only the matching local playbook:
   - MC: [coordinate-geometry-mc-playbook.md](./references/coordinate-geometry-mc-playbook.md)
   - TF: [coordinate-geometry-tf-playbook.md](./references/coordinate-geometry-tf-playbook.md)
   - SA: [coordinate-geometry-sa-playbook.md](./references/coordinate-geometry-sa-playbook.md)
3. Apply the common rules from `python-latex-exam-master`.
4. Choose coordinates that make the real object simple and mathematically valid.
5. Keep the same coordinate assumptions in the statement, figure, formulas, answer, and solution.

## Oxyz Guardrails

- State or imply the coordinate unit clearly.
- Verify positive height/depth/time/cost and practical ranges.
- Check whether a foot point lies on the intended segment, not only the infinite line.
- Check sphere/line or plane intersections on the stated physical object, not just the algebraic extension.
- Keep line, plane, vector, and distance formulas tied to one canonical set of points.
- For TF, make four statements test different layers: coordinates, equation, distance/angle, and practical conclusion.
- For SA, justify the coordinate setup before optimizing or rounding.
