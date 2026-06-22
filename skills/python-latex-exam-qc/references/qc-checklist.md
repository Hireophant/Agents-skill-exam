# QC Checklist

## Structure

- MC has exactly four options and one correct answer.
- TF has four statements, independent enough, with matched explanations.
- SA has one unique final answer and respects the requested answer format.
- If an exam bundle has multiple variants, do not merge comments across variants.

## Math Correctness

- Recompute every final answer from the generated statement.
- Check domains, excluded values, edge cases, endpoints, and units.
- Check exact-vs-rounded display: use `=` for exact values and `\approx` only when rounded.
- Check random values remain realistic for the story.
- Check distractors remain wrong after formatting/rounding.
- Check TF false statements are plausible and the solution does not accidentally prove the false statement.
- Check SA answer length, decimal comma, negative sign, and rounding rule.

## Presentation And Notation

Use `python-latex-exam-master/references/trinh-bay-cong-thuc-full.md` as binding.

- All formulas and numbers that function mathematically are in math mode.
- Sentence punctuation is outside `$...$` unless the standard allows otherwise.
- Decimal commas use `{,}` in LaTeX.
- Units are upright text with a space after the number.
- Use `\mathrm{P}(A)`, `\mathrm{C}_n^k`, `\mathrm{A}_n^k`, `\mathrm{P}_n`.
- Use `\mathrm{d}x`, `\mathrm{e}`, `\parallel`, `\perp`, `^\circ`.
- Use `\left(...\right)` or `\left[...\right]` for intervals when appropriate.
- Use `eqnarray*`/aligned style only in the approved bank rhythm.
- Do not add unapproved shorthand commands or new environments.

## LaTeX And TikZ

- No odd number of unescaped dollar signs.
- Every `\begin{...}` has a matching `\end{...}`.
- Braces are balanced enough for the emitted block.
- No raw `None`, `nan`, `inf`, unresolved placeholders, or debug text.
- No unsafe standalone `\\` after environments.
- TikZ commands end with semicolons.
- Named TikZ coordinates are defined before use.
- Figure labels are readable and match the solution.
- Stem figures stay clean; solution figures may add helper marks only when needed.

## Report Status

- `OK`: no action.
- `CAN_CHINH_NHE`: small wording/style issue that does not affect correctness.
- `CAN_SUA`: must fix before using.
- `KHONG_NEN_DUNG`: unreliable item; rewrite or discard.
