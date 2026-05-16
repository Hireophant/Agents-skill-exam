# Classical Probability TF Playbook

Use this file when writing, repairing, or reviewing SP/xac-suat/xac-suat-co-dien true-false questions. The current local sample is a finite card-selection model with two events, so do not use this as a conditional-probability or statistics playbook.

## Core Pattern

A good classical-probability TF item uses one sample space and four linked checks:

- sample space and one simple event
- a second event counted by a clear rule
- the intersection or complement of events
- a final logical property such as independence or a comparison

Keep all four statements stylistically parallel and use the same event names throughout.

## Counting Workflow

1. Define `n(Omega)` first.
2. Define events using short symbols such as `A`, `B`.
3. Count `n(A)`, `n(B)`, and `n(A cap B)` using integer counts, not rounded probabilities.
4. Convert counts to fractions with `phanso(...)` or exact rational logic.
5. For independence, compare `P(A cap B)` with `P(A)P(B)` exactly.

For two-box/card models:

- sample space is usually product count: `n(Omega)=n_1 n_2`
- "sum equals fixed value" often gives one valid partner for each first-card value
- "product is odd" means both selected numbers are odd
- intersection should satisfy both conditions simultaneously; do not multiply event counts unless independence is already known

## False Statements

False variants should be near-miss counts:

- using the second box count instead of the first for `n(A)`
- using reciprocal or product of odd counts incorrectly
- treating `A cap B` as `A` times `B`
- flipping "independent" and "not independent"

Avoid impossible-looking random fractions. The false statement should look like a plausible student miscount.

## Code Guardrails

- Use `while True` when parity, equality, or independence status must be controlled.
- Keep counts as integers and exact fractions until display.
- Avoid float comparison for independence when exact fractions are available; compare cross-products or Sympy rationals.
- Ensure false and true statements differ after simplification.
- If a statement says "two events are independent", verify both `P(A)`, `P(B)` are nonzero and compare exactly.

## Solution Style

Each `LGPAtrue` should explain only the relevant statement but may reuse earlier counts:

```latex
n(\Omega)=...
Suy ra n(A)=...
P(A)=...
```

For independence:

```latex
Ta co:
\left\{\begin{array}{l}
P(A\cap B)=...\\
P(A)\cdot P(B)=...
\end{array}\right.
```

Then conclude `A` and `B` are independent or not independent. Do not assert independence from wording alone.
