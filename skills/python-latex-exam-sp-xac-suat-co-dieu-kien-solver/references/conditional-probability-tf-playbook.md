# Conditional Probability TF Playbook
## Mandatory notation standard

This playbook controls mathematical strategy only. For every displayed formula, symbol, unit, interval, system, probability/combinatorics notation, vector, integral, variation table, list, and aligned solution chain, obey `python-latex-exam-master/references/trinh-bay-cong-thuc-full.md`. Do not let shorthand examples in this playbook override that standard.

Use this file when writing, repairing, or reviewing SP/xac-suat/xac-suat-co-dieu-kien true-false questions. The local bank has TF samples for drawing without replacement, source/quality inspection, medical or AI diagnosis, total probability, Bayes, and threshold decisions. Do not use this as a classical-probability-only or statistics playbook.

## Core Four-Statement Pattern

A strong conditional-probability TF item usually follows this order:

- Statement 1: a base probability or complement, such as `P(A)`, `P(\bar A)`, or a branch probability.
- Statement 2: a conditional probability, such as `P(B|A)` or a total-probability component.
- Statement 3: total probability, intersection, complement of an intersection, or `P(B)`.
- Statement 4: Bayes probability, independence/relationship, or a practical threshold conclusion.

The four statements should use the same event symbols as the stem and solution.

## Event Notation Discipline

Define events before calculating:

- `A`: source, disease, first draw, first person detects, or target condition.
- `B`: result, second draw, positive test, defect, or observed outcome.
- complements with `\overline{A}`, `\overline{B}`.

Do not swap the meaning of `A` and `B` between statement and solution. This is the most common source of wrong TF logic.

## Main Formulas

Use exact formulas:

```latex
P(A\cap B)=P(A)P(B|A)
```

```latex
P(B)=P(A)P(B|A)+P(\overline A)P(B|\overline A)
```

```latex
P(A|B)=\dfrac{P(A)P(B|A)}{P(B)}
```

For multi-branch cases, extend total probability across all branches.

## Common Models

- Without replacement: update the denominator and counts after the first draw.
- Source selection: condition on the route/source first, then defect/quality within that source.
- Medical/AI diagnosis: distinguish sensitivity `P(+|disease)` from posterior probability `P(disease|+)`.
- Detection/complement: `at least one detects = 1 - P(no one detects)`.
- Practical threshold: compare the exact posterior or risk with a nearby threshold after computing it.

## Lessons from KTL4.py (SP233TF016)

When generating conditional and total probability True/False questions (especially in medical or real-world statistics):
1. **Terminating Decimal Probabilities**:
   - Choose initial parameters (percentages) in multiples of 5 (e.g., `p1_pct = [30, 35, 40, 45, 50]` and `p2_pct = [60, 65, 70, 75, 80]`) so that total probability calculations ($P(B) = P(A)P(B|A) + P(\overline{A})P(B|\overline{A})$) resolve to exact, terminating decimals.
2. **Plausible Distractors (Wrong Statements)**:
   - Construct distractors by shifting the correct values by a fixed offset (e.g. `+ 0.1` or `- 0.15`).
   - Validate inside the `while True` loop that distractors are strictly distinct from the correct probabilities (`P_B_nhieu != P_B`) to prevent overlapping answers.
3. **Quotation Mark Escaping**:
   - Use `\\lq\\lq` and `\\rq\\rq` when declaring event text strings (e.g., `\\lq\\lq Người được chọn bị bệnh tiểu đường\\rq\\rq`) to ensure correct LaTeX quotation marks.

## False Statement Design

Good false statements are close mistakes:

- using `P(B|A)` in place of `P(A|B)`
- forgetting the false-positive branch in `P(B)`
- treating draws without replacement as if replacement happened
- using `P(A)P(B)` instead of `P(A)P(B|A)`
- comparing a rounded display value against a threshold on the wrong side

Avoid values that are obviously impossible, such as probabilities below `0` or above `1`, unless the false statement is meant to test impossibility directly.

## Code Guardrails

- Keep probabilities as `sp.Rational` or exact fractions until the final display.
- Check conditioning denominators are nonzero.
- Use `while True` to keep rates in realistic ranges and thresholds on the intended side.
- For percentages, convert once: `sp.Rational(percent, 100)`.
- Use display helpers for decimal comma output, but never reuse decimal-comma strings in computation.
- If a statement says "larger than" or "smaller than", choose thresholds safely away from rounding ambiguity.

## Solution Style

For each `LGPAtrue`, show the formula before substitution:

```latex
P(B)=P(A)P(B|A)+P(\overline A)P(B|\overline A)
```

For Bayes:

```latex
Theo cong thuc Bayes, ta co ...
```

If the problem includes a probability tree, insert it once in the first or most explanatory sub-solution, then reuse the branch values later.
