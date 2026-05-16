# Authoring Style And Feedback

## Purpose

Use this file when a generator is mathematically close but still needs to match the approved classroom style: wording rhythm, solution depth, notation, layout, and teacher-feedback fixes.

## Teacher-style solution flow

Prefer this order:

1. define variables and the model
2. write the main formula
3. state the domain, bound, derivative sign, or geometric condition
4. explain why that condition gives the selected case
5. substitute values
6. conclude in the requested unit and precision

Avoid ending with a bare formula when one short conclusion sentence would make the reasoning easier to read.

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
- Run the generator after nontrivial edits.
- Inspect the generated `.tex` around the edited block, especially for `itemchoice`, `minipage`, TikZ blocks, and forced line breaks.
- Compile when possible before reporting completion.

