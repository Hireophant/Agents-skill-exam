---
name: python-latex-exam-gt-solver
description: GT calculus/analysis solver for Python-LaTeX exam questions. Use with python-latex-exam-master when the user sends an image, question stem, code file, or file name indicating GT, giai tich, ham so, derivatives, monotonicity, extrema, variation tables, integrals, logarithmic/exponential models, optimization, economics, motion, area/volume, MC GT, TF GT, or SA GT. Read only this solver's local references for GT strategy.
---

# Python Latex Exam GT Solver

## Required Pairing

Always pair this solver with `python-latex-exam-master` for common LaTeX, presentation, randomization, house-style rules, and the mandatory formula/notation standard from `trinh-bay-cong-thuc-full.md`.

## Use When

Use this skill for GT calculus/analysis items involving functions, derivatives, integrals, optimization, growth/decay, applied models, and graph/table reasoning.

## Workflow

1. Decide whether the item is MC, TF, or SA from the prompt, image, or file name.
2. Read only the matching local playbook:
   - MC: [calculus-analysis-mc-playbook.md](./references/calculus-analysis-mc-playbook.md)
   - TF: [calculus-analysis-tf-playbook.md](./references/calculus-analysis-tf-playbook.md)
   - SA: [calculus-analysis-sa-playbook.md](./references/calculus-analysis-sa-playbook.md)
3. Apply the common rules from `python-latex-exam-master`, including the mandatory formula/notation standard.
4. Lock the domain, unit, interval, rounding rule, and final requested quantity.
5. Use one canonical model for statement, computation, answer, and solution.

## GT Guardrails

- Do not claim monotonicity across excluded points or vertical asymptotes.
- For optimization, prove the valid domain and show why the chosen critical point or endpoint is optimal.
- For integrals, match bounds, variable, units, and figure region exactly.
- For growth/decay, keep signs and monotonic direction realistic.
- For applied money/cost problems, keep totals plausible and rounding explicit.
- For TF, make the four statements test different layers: setup, computation, domain/logic, and conclusion.
- For SA, do not round intermediate results unless the problem says so.
