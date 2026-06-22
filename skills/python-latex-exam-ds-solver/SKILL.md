---
name: python-latex-exam-ds-solver
description: DS algebra/discrete-math solver for Python-LaTeX exam questions. Use with python-latex-exam-master when the user sends an image, question stem, code file, or file name indicating DS, dai so, algebra, logarithmic inequalities, domains, sequences, feasible regions, linear programming, investment/finance word problems, combinatorial games, MC DS, or SA DS. Read only this solver's local references for DS strategy.
---

# Python Latex Exam DS Solver

## Required Pairing

Always pair this solver with `python-latex-exam-master` for common LaTeX, presentation, randomization, house-style rules, and the mandatory formula/notation standard from `trinh-bay-cong-thuc-full.md`.

## Use When

Use this skill for DS algebra/discrete math exam items. The current local bank supports DS MC and DS SA; do not invent a DS TF workflow unless real examples are added.

## Workflow

1. Decide whether the item is MC or SA from the prompt, image, or file name.
2. Read only the matching local playbook:
   - MC: [algebra-discrete-mc-playbook.md](./references/algebra-discrete-mc-playbook.md)
   - SA: [algebra-discrete-sa-playbook.md](./references/algebra-discrete-sa-playbook.md)
3. Apply the common rules from `python-latex-exam-master`, including the mandatory formula/notation standard.
4. Lock domains, integer constraints, financial timing, and feasibility before writing options or final answers.
5. Build the solution as a human-readable chain, not hidden scratch work.

## DS Guardrails

- Check log arguments and log bases before transforming inequalities.
- Flip inequality direction only when the logarithm base is between `0` and `1`.
- Intersect algebraic results with the original domain.
- Keep interval endpoints and bracket types exact.
- For sequences, verify index shifts and signs.
- For word problems, enforce integer counts, nonempty feasible regions, positive quantities, and realistic money/percentage values.
- For MC, build distractors from real student mistakes and verify all choices stay distinct after formatting.
