---
name: python-latex-exam-hh-co-dien-solver
description: HH hinh hoc co dien solver for Python-LaTeX exam questions. Use with python-latex-exam-master when the user sends an image, question stem, code file, or file name indicating HH co dien, classical synthetic geometry, solids, pyramids, prisms, tetrahedra, projections, auxiliary points, section ratios, regular solids, MC HH co dien, or SA HH co dien without coordinate setup. Read only this solver's local references for classical geometry strategy.
---

# Python Latex Exam HH Co Dien Solver

## Required Pairing

Always pair this solver with `python-latex-exam-master` for common LaTeX, presentation, randomization, and figure-style rules.

## Use When

Use this skill for classical geometry items solved by synthetic properties rather than assigning coordinates. The current local bank supports HH co dien MC and SA; do not invent a HH co dien TF workflow unless examples are added.

## Workflow

1. Decide whether the item is MC or SA from the prompt, image, or file name.
2. Read only the matching local playbook:
   - MC: [classical-geometry-mc-playbook.md](./references/classical-geometry-mc-playbook.md)
   - SA: [classical-geometry-sa-playbook.md](./references/classical-geometry-sa-playbook.md)
3. Apply the common rules from `python-latex-exam-master`.
4. Identify the canonical structure before calculating: projection, parallel replacement, centroid, midpoint, section ratio, regular-solid symmetry, or 2D reduction.
5. Present the shortest defensible teacher chain.

## HH Co Dien Guardrails

- Add an auxiliary point only when it unlocks a theorem or a clean reduction.
- Explain why a 3D target reduces to a 2D triangle, segment, or angle.
- Keep figure labels visually credible and consistent with the solution.
- For MC, make distractors nearby geometry mistakes, not random numbers.
- For SA, show the reduction step before substituting values.
- For vector statements in regular solids, keep midpoint/parallel-vector arguments explicit before computing dot products or angles.
- Match the reference figure's visible/hidden edges deliberately. Do not leave an edge dashed from an old template if the reference or QC requires it to be solid.
- When a teacher supplies handwritten solution steps, preserve that order of reasoning instead of replacing it with a coordinate or overly compressed proof.
