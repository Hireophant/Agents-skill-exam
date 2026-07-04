---
name: python-latex-exam-master
description: Common Python-to-LaTeX exam authoring style for generated math questions. Always use this common skill together with exactly one domain solver skill when Codex writes, repairs, reviews, or converts exam questions from an image, prompt, code file name, solution-reference image, or Python generator and must preserve LaTeX/TikZ layout, mandatory formula/notation standards, house style, teacher-readable worked solutions, exact sample-solution formatting, randomization guardrails, answer consistency, helper usage, and practical realism.
---

# Python Latex Exam Master

## Role

This is the default common skill. It contains only shared presentation, LaTeX, randomization, and generator-quality rules.

For mathematical strategy, also load exactly one domain solver skill:

- `python-latex-exam-ds-solver` for DS/dai so/algebra/discrete math.
- `python-latex-exam-gt-solver` for GT/giai tich/calculus/analysis.
- `python-latex-exam-hh-co-dien-solver` for HH co dien/synthetic geometry.
- `python-latex-exam-hh-gan-truc-solver` for HH gan truc/Oxyz/coordinate geometry.
- `python-latex-exam-sp-xac-suat-co-dien-solver` for SP xac suat co dien/classical probability.
- `python-latex-exam-sp-xac-suat-co-dieu-kien-solver` for SP xac suat co dieu kien/conditional probability.

Do not load multiple domain solvers unless the user explicitly asks to compare or classify multiple mixed questions.

## Choosing The Domain Solver

When the user sends an image, a question stem, a code file, or only a file name, first infer the domain from the strongest signal:

1. Path or folder names such as `DS`, `GT`, `HH`, `hinh-hoc-co-dien`, `hinh-hoc-gan-truc`, `Oxyz`, `SP`, `xac-suat-co-dien`, `xac-suat-co-dieu-kien`.
2. File/code names such as `DS...MC`, `GT...TF`, `HH...SA`, `SP...TF`.
3. Problem vocabulary in the image/stem:
   - DS: logarithms, inequalities, sequences, feasible regions, investment, compound interest, algebraic/discrete constraints.
   - GT: function graphs, derivatives, monotonicity, extrema, integrals, exponential/log models, optimization, motion/economics.
   - HH co dien: pyramids, prisms, tetrahedra, projections, section points, synthetic solid geometry without coordinates.
   - HH gan truc/Oxyz: coordinates, vectors, planes, lines, spheres, distances/angles in `Oxyz`, practical 3D coordinate models.
   - SP co dien: finite sample spaces, cards, dice, balls, counting favorable outcomes, combinations, independence.
   - SP co dieu kien: `P(A|B)`, probability trees, Bayes, total probability, tests/diagnostics, sensitivity/specificity, conditional counting.

After choosing the solver, read only that solver's `SKILL.md` and its local `references/` file matching MC/TF/SA. Do not read unrelated solver folders.

## Common Workflow

1. Classify the output type: MC, TF, SA, or another fixed structure.
2. Choose the single domain solver from the signals above.
3. Read the matching domain playbook from that solver folder.
4. Read only the common reference files below that are needed for the task.
5. Extract any user-specific overrides, such as which numbers to randomize, which values to keep fixed, required ranges, rounding, wording, figure layout, or solution-reference formatting.
6. Apply user-specific overrides first for the exact parts the user specified; use the skill only as the fallback for unspecified parts.
7. Preserve generator metadata before coding: in the Python docstring, under `TOM TAT DE BAI`, paste the original problem statement/stem verbatim, only removing stray escape backslashes if copied from LaTeX; do not summarize, paraphrase, shorten, or replace it with a generic description. Under `HASHTAG`, use the exact relevant topic names for the question, not broad filler tags.
8. Lock mathematical model, units, answer format, rounding rule, and layout contract before coding.
9. Separate exact computation values from display strings.
10. Add randomization guardrails before composing the statement.
11. Generate statement, answer key, worked solution, and figures from the same canonical variables.
12. Inspect generated `.tex` after nontrivial edits, especially around `itemchoice`, `minipage`, TikZ, and forced line breaks.
13. After generating the required 100 randomized `.tex` samples, use `python-latex-exam-qc` to audit the output and keep fixing/rerunning until QC is clean.

## Common References

- Read [question-types-and-templates.md](./references/question-types-and-templates.md) for MC, TF, SA output skeletons and local helper patterns.
- Read [generator-randomization-and-consistency.md](./references/generator-randomization-and-consistency.md) for random parameters, exact-vs-display values, rounding, answer consistency, and hidden constraints.
- Read [authoring-style-and-feedback.md](./references/authoring-style-and-feedback.md) for teacher-style explanation, house wording, layout fidelity, and handling user/teacher feedback.
- Read [latex-tikz-output-checklist.md](./references/latex-tikz-output-checklist.md) for LaTeX/TikZ compile errors, generated `.tex` inspection, `minipage`, integral notation, and figure placement.
- Always read and obey [trinh-bay-cong-thuc-full.md](./references/trinh-bay-cong-thuc-full.md) when the task contains mathematical formulas, notation, units, systems, intervals, integrals, variation tables, aligned equations, lists, or solution presentation. The source PDF is preserved at [TrinhBayCongThuc.pdf](./references/TrinhBayCongThuc.pdf).

## Non-Negotiables

- User instructions override the skill for the exact parts the user specifies. If the user says which numbers to randomize, which values to keep fixed, what range to use, how to round, or what format/style to follow, obey that local instruction first. Use the skill rules only for parts the user did not specify.
- Never reuse a formatted display string as a numeric input.
- Follow `trinh-bay-cong-thuc-full.md` exactly for mathematical typography: all formulas/numbers in math mode, punctuation outside math where required, decimal commas as `{,}`, upright units, `\mathrm{d}x`, `\mathrm{P}(A)`, `\mathrm{C}_n^k`, `\parallel`, `\perp`, degree symbols, interval delimiters, systems, variation tables, and aligned solution chains.
- Never trust a Python diff alone for a layout fix; inspect generated `.tex`.
- Keep statement, answer, solution, and figure labels tied to one source of truth.
- Every authored question generator must include docstring metadata with `TOM TAT DE BAI` containing the verbatim original stem/prompt, with stray LaTeX escape backslashes removed when needed, and `HASHTAG` containing specific topic tags that match the actual question.
- Keep TF false statements plausible and parallel, not cartoonishly wrong.
- Keep SA final answers aligned with the requested precision and unit.
- For SA worked solutions, follow the four-step teacher arc when the problem is nontrivial: analyze/orient the method, set variables with conditions, solve the equation/system/inequality/model without overusing calculator shortcuts, then check conditions and conclude with a boxed final answer.
- Do not round intermediate values unless the statement explicitly allows it.
- Do not use `int(...)` to fake a one-decimal answer; use the local display helper such as `lam_tron(value, digits)`.
- For practical count questions where the answer is a number of objects, trips, boxes, paint cans, workers, months, etc., do not treat this as ordinary rounding. Word the stem as "toi thieu" when appropriate and compute with `ceil`; if the prompt only says "lam tron" but the context requires a minimum count, flag or ask before coding.
- Add `while True` guardrails for invalid domains, ugly values, repeated options, impossible figures, non-realistic units, and wrong answers that collapse to the correct one after rounding.
- For practical contexts, reject physically silly outputs unless the story explicitly supports them.

## House Style

Preserve the user's approved rhythm. If a sample uses `Ta co`, `Ma`, `Do do`, `Suy ra`, `Vay`, bracket labels, specific integral notation, or no trailing punctuation in TF statements, keep that pattern. For formula and notation details, the mandatory standard in `trinh-bay-cong-thuc-full.md` is the default contract.

If the user provides a solution-reference image, treat it as a strict formatting contract. Reproduce the same presentation order, line breaks, calculation steps, notation, alignment style, wording rhythm, and conclusion style as closely as LaTeX allows. Do not add extra explanations, delete intermediate steps, reorder calculations, simplify the solution structure, change the solving route, or "improve" the presentation unless the user explicitly asks for that. If the reference solution contains a mathematical error, state the error clearly and then preserve the same presentation style while correcting only the necessary mathematical content.

Use concise teacher chains. For easy subparts, one clean line is often better than a long derivation. For harder SA/optimization/geometry items, include the reason that makes the chosen case valid.

For figures, do not change the layout contract. Use `minipage` only when the sample places the figure beside the text. For figure-below-text layouts, prefer paragraph breaks such as `\par\noindent` over unsafe standalone `\\`.

## Recent QC Lessons

- Treat user/teacher QC as a narrow patch unless the model is wrong. If the QC says "chi sua phan tren hinh", "de giu nhu cu", or "trinh bay nhu cu", edit only that region and keep the old solving route, line breaks, and calculation depth.
- When a reference image is supplied, match wording additions exactly in the stem rather than replacing the old sentence; for example add clarifying phrases such as "nhu hinh ve" while preserving the randomized angle or data.
- For SA rounding text, use the local house wording from the templates and round only the final requested quantity. In the solution, use `=` for exact integer/exact symbolic results and `\approx` only when a rounded display is genuinely needed.
- For practical SA count answers, distinguish "round to nearest" from "minimum required". If the computed value is `3.3` cans/trips/containers, the final required count is `4`, and the stem should say "can toi thieu bao nhieu ..." rather than ordinary "lam tron".
- For midpoint/vector-coordinate notation already approved by the user, preserve bracket style such as `[I]=\dfrac{[M]+[N]}{2}` instead of silently switching to tuple-only notation.
- For visual tasks, make a stem figure and a solution figure serve different roles: the stem figure should stay clean and close to the sample; the solution figure may add axes, projections, helper labels, or calculation marks.

## Helper Habits

- Use `tinh_latex(expr)` for Sympy expressions.
- By default, display algebraic expressions in expanded classroom form unless the user explicitly asks for factored, simplified, or compact form. Prefer `tinh_latex(expr, Expand=True)` and, for rational models, build `\dfrac{expanded numerator}{expanded denominator}` from the canonical numerator and denominator instead of letting Sympy factor common constants.
- For TF generators, do not assume the false-statement solution is just the true-statement solution with the final label changed. If a false variant changes a threshold, value, condition, or conclusion, write a separate false solution for that variant or implement local TF assembly instead of relying on a helper that only accepts `LGtrue`.
- Treat `lam_tron()` output as display-first.
- Pair rounded-answer generation with `kiem_tra_lam_tron(...)` when the local bank expects compact formatting.
- Keep money, units, coordinates, and decimal commas consistent with the existing file.
- Prefer small formatting helpers over repeated nested f-strings for sensitive solution lines.

## Final Check

Before finishing, verify:

- math logic is valid on the actual domain
- random values satisfy every hidden constraint
- displayed units match computed units
- all options/statements remain distinct after formatting
- true/false statement variants use the same mathematical side of the threshold as their worked solutions
- LaTeX compiles or the generated `.tex` block is inspected
- figure labels, bounds, answers, and explanations match
