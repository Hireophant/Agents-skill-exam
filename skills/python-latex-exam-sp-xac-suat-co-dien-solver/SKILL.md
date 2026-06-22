---
name: python-latex-exam-sp-xac-suat-co-dien-solver
description: SP xac suat co dien solver for Python-LaTeX exam questions. Use with python-latex-exam-master when the user sends an image, question stem, code file, or file name indicating SP, xac suat co dien, finite sample spaces, cards, dice, balls, combinatorial counting, complements, intersections, independence, repeated trials, reduced fractions, TF probability, or SA probability. Read only this solver's local references for classical probability strategy.
---

# Python Latex Exam SP Xac Suat Co Dien Solver

## Required Pairing

Always pair this solver with `python-latex-exam-master` for common LaTeX, presentation, randomization, house-style rules, and the mandatory formula/notation standard from `trinh-bay-cong-thuc-full.md`.

## Use When

Use this skill for classical probability items based on finite sample spaces and counting. The current local examples support TF and SA; do not invent an MC workflow unless real examples are added.

## Workflow

1. Decide whether the item is TF or SA from the prompt, image, or file name.
2. Read only the matching local playbook:
   - TF: [classical-probability-tf-playbook.md](./references/classical-probability-tf-playbook.md)
   - SA: [classical-probability-sa-playbook.md](./references/classical-probability-sa-playbook.md)
3. Apply the common rules from `python-latex-exam-master`, including the mandatory formula/notation standard.
4. State the sample space and favorable event before computing.
5. Count by cases or complement only when the cases are disjoint and complete.

## SP Co Dien Guardrails

- Keep counts positive and the sample space finite/clear.
- Avoid overcounting when splitting into cases.
- Use independence only when stated or proved.
- Reduce fractions before forming requested expressions.
- For repeated trials, separate one-trial probability from binomial/multiple-trial probability.
- For TF, progress from simple count to intersection/complement/independence/practical conclusion.
