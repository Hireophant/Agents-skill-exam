---
name: python-latex-exam-sp-xac-suat-co-dieu-kien-solver
description: SP xac suat co dieu kien solver for Python-LaTeX exam questions. Use with python-latex-exam-master when the user sends an image, question stem, code file, or file name indicating conditional probability, xac suat co dieu kien, P(A|B), probability trees, total probability, Bayes formula, sensitivity/specificity, false positives, without-replacement draws, conditioned counting, diagnostic tests, TF conditional probability, or SA conditional probability. Read only this solver's local references for conditional probability strategy.
---

# Python Latex Exam SP Xac Suat Co Dieu Kien Solver

## Required Pairing

Always pair this solver with `python-latex-exam-master` for common LaTeX, presentation, randomization, house-style rules, and the mandatory formula/notation standard from `trinh-bay-cong-thuc-full.md`.

## Use When

Use this skill for conditional-probability items. The current local examples support TF and SA; do not invent an MC workflow unless real examples are added.

## Workflow

1. Decide whether the item is TF or SA from the prompt, image, or file name.
2. Read only the matching local playbook:
   - TF: [conditional-probability-tf-playbook.md](./references/conditional-probability-tf-playbook.md)
   - SA: [conditional-probability-sa-playbook.md](./references/conditional-probability-sa-playbook.md)
3. Apply the common rules from `python-latex-exam-master`, including the mandatory formula/notation standard.
4. Define events before calculating and keep event meanings fixed.
5. Compute the conditioning denominator and verify it is nonzero.
6. Present Bayes or total-probability steps explicitly enough that `P(A|B)` is not confused with `P(B|A)`.

## SP Co Dieu Kien Guardrails

- State replacement status clearly for draws.
- Keep sensitivity, specificity, prevalence, and false-positive rates in `(0,1)`.
- Use `P(B)=P(A)P(B|A)+P(\overline A)P(B|\overline A)` when total probability is needed.
- Use `P(A|B)=P(A)P(B|A)/P(B)` for Bayes conclusions.
- For conditioned counting, count `n(B)` and `n(A cap B)` separately.
- For TF, make false statements plausible: reversed condition, missing branch, wrong complement, or threshold rounding.
