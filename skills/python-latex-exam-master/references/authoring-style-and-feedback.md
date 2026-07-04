# Authoring Style And Feedback

## Purpose

Use this file when a generator is mathematically close but still needs to match the approved classroom style: wording rhythm, solution depth, notation, layout, formula standards, and teacher-feedback fixes.

## Mandatory formula and notation standard

- Before writing or reviewing formulas, read [trinh-bay-cong-thuc-full.md](./trinh-bay-cong-thuc-full.md) and treat it as binding. The original source PDF is [TrinhBayCongThuc.pdf](./TrinhBayCongThuc.pdf).
- Put formulas and numbers in math mode, but keep sentence punctuation outside math except for approved cases such as `$S.ABC$`, `$A(2; 3)$`, or displayed formulas where the punctuation belongs inside.
- Use the prescribed symbols: `\mathscr{D}` for domain, `\varnothing` for empty set, `\setminus` for set difference, `\times`/`\cdot` for multiplication when needed, `\ldots` for listing and `\cdots` for operations.
- Use decimal commas as `{,}`, systems with aligned `&`, `\mathrm{C}_n^k`, `\mathrm{A}_n^k`, `\mathrm{P}_n`, `\mathrm{P}(A)`, upright `\mathrm{d}x`, `\mathrm{e}`, upright units with a space, `\parallel`, `\perp`, `^\circ`, and `\colon` for equations of lines/planes.
- Use `\dfrac` for standalone fractions and `\frac`/`\tfrac` in bases, exponents, or integral bounds.
- Do not introduce shorthand commands or new environments outside the project rules. Do not begin exercises/solutions with `\hfill`, and do not add extra `\\`, `\par`, or `\hfill` after list/minipage-style environments unless the sample explicitly requires it.

## Teacher-style solution flow

Prefer this order:

1. define variables and the model
2. write the main formula
3. state the domain, bound, derivative sign, or geometric condition
4. explain why that condition gives the selected case
5. substitute values
6. conclude in the requested unit and precision

Avoid ending with a bare formula when one short conclusion sentence would make the reasoning easier to read.

## SA four-step solution contract

For nontrivial SA questions, structure the worked solution around four visible moves unless the user's reference image locks a different order:

1. Analyze the problem and state the method or key reduction.
2. Set variables with conditions and units.
3. Solve the equation, system, inequality, optimization, or counting model with enough algebra to be teacher-readable; do not replace the reasoning with calculator-only steps.
4. Check conditions, interpret the result in context, and conclude with the final answer boxed, for example `\boxed{...}`.

For easy SA items, these moves may be compressed, but do not skip the condition check or the final contextual conclusion.

## Locked house style

When the user has corrected or approved a pattern, keep it.

- Keep discourse markers such as `Ta co`, `Ma`, `Do do`, `Suy ra`, `Vay` in the same rhythm.
- Keep short one-line explanations for easy TF subparts when the bank uses them.
- Preserve local notation such as `[I]`, coordinate tuple style, integral display style, and chosen object names.
- Do not add trailing punctuation to TF statements if the local style omits it.
- Use the requested substitution direction, for example `m.(...)^2 = ... => m = ...`.
- If the user asks for only `f` strings, do not introduce raw or `fr` strings nearby.
- If the bank uses plain money values such as `1300000`, do not add dot grouping.

## Optimization presentation

For optimization and economics, do not jump from the formula to the answer.

Use this classroom sequence when relevant:

1. define the variable and practical domain
2. write revenue, cost, tax, or profit components in order
3. differentiate or use the selected inequality
4. solve the critical condition
5. compare endpoints and critical points when the domain is bounded
6. conclude

Use `=` for exact values and `\approx` only for genuinely rounded values. If the generator intentionally makes a root exact, the solution should display it as exact.

## Generator metadata

In each Python generator docstring, keep metadata useful for future repairs:

- `TOM TAT DE BAI`: paste the original stem/prompt verbatim. Do not summarize, rewrite, shorten, or replace it with a generic description. If copied from LaTeX, remove only stray escape backslashes that are not part of meaningful notation.
- `HASHTAG`: use specific topic tags that match the actual problem type, not vague labels. Include the method when useful, such as `#toi_uu`, `#logistic`, `#hinh_lap_phuong`, `#xac_suat_co_dieu_kien`.

## Layout and figure roles

Treat approved screenshots and teacher corrections as layout contracts.

- If the sample places the figure below the stem, do not introduce `minipage`.
- If the sample places the figure beside the stem, keep the side-by-side layout.
- Keep stem figures clean; put helper points, red segments, or extra diagrams in the solution figure unless requested otherwise.
- If a figure must appear below an item label such as `d)`, inspect the generated `.tex` inside the list environment.
- Prefer `\par\noindent` over unsafe standalone `\\` for figure-below-text layout.
- Prefer `\centering` inside a `minipage` instead of nesting a `center` environment.

## Feedback-driven edits

Treat teacher feedback as a regression test.

- Patch the named issue first; do not rewrite the whole generator unless needed.
- Preserve the teacher's requested presentation level. If feedback says to keep the old presentation or "trinh bay nhu cu", restore the old calculation rhythm and line structure, not only the mathematical conclusion.
- Do not over-compress a solution after a wording QC unless the teacher explicitly asks for a shortcut. A "nhan xet" request may still expect the same algebraic presentation with a shorter conclusion.
- When a QC suggests an example number such as `40/41`, decide whether it is a fixed requirement or a pattern (`L/L+1`) from the random model before changing randomization.
- Run the generator after nontrivial edits.
- Inspect the generated `.tex` around the edited block, especially for `itemchoice`, `minipage`, TikZ blocks, and forced line breaks.
- Compile when possible before reporting completion.
