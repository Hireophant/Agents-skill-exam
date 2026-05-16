# Classical Probability SA Playbook

Use this file when writing, repairing, or reviewing SP/xac-suat/xac-suat-co-dien short-answer questions. The local SA bank includes digit arrangements, "at least one" complements, repeated independent trials, color/number assignment, envelopes chosen with replacement, and finite combinatorial casework.

## Core Arc

1. Define the sample space.
2. Define the favorable event.
3. Choose the safest count: direct count, complement, cases, or geometric series.
4. Count with exact integers or Sympy rationals.
5. Reduce the probability fraction.
6. Compute the requested final expression such as `a+b`, `ma+nb`, or a rounded probability.

Never round a probability before using it in later algebra.

## Common Models

### Arrangement With Restrictions

Use for digits, colors, boards, or objects placed in positions.

- Count total arrangements first.
- For "no two even digits adjacent", arrange odd digits as separators, then choose slots for even digits.
- For colors/labels on geometric faces, split the structure into natural groups and count cases carefully.
- Explain why cases are exhaustive and disjoint.

### At Least One / Complement

Use the complement when the favorable event is "at least one" or "opens within at most k tries".

```latex
P(A)=1-P(\overline A)
```

For repeated trials, only use independence if the statement says attempts are independent or the model implies replacement.

### Repeated Turns And Infinite Series

Use for games where players repeat until someone succeeds.

- Define success and failure probabilities for each player.
- Compute one-cycle failure probability `q`.
- Write the desired win probability as first-cycle win times `1+q+q^2+...`.
- Check `0<q<1` before using the infinite geometric sum.

### Envelope / Set Selection With Replacement

If each participant chooses and then items are returned, sample space is usually:

```latex
n(\Omega)=\left(C_n^k\right)^r
```

For union-size constraints, introduce counts for items chosen by exactly 1, exactly 2, and exactly 3 participants, then solve the small system before multiplying choices.

### Optimization By Distribution

For box/ball distribution probability questions:

- Write probability as a function of the distribution.
- Justify the structural choice, such as "sacrifice one box" to maximize white probability.
- Check all boxes are nonempty if the story requires it.

## Randomization Guardrails

- Counts must be nonnegative integers.
- Required selections cannot exceed available objects.
- Fractions should reduce cleanly when the answer asks for numerator/denominator.
- Final `a`, `b`, `m`, `n`, or rounded values should be positive and pass `kiem_tra_lam_tron`.
- Do not create ambiguous "same object" situations: if items have colors and numbers, state whether cards are identified by both color and number.
- For real-world stories, keep quantities reasonable: number of questions, envelopes, balls, digits, keys, or attempts should be classroom-sized.

## LaTeX And Presentation

Use clear counting lines:

```latex
n(\Omega)=...
n(A)=...
P(A)=\dfrac{n(A)}{n(\Omega)}=...
```

For longer casework, use `\bullet`, `\begin{itemize}`, or named cases `TH1`, `TH2`, ... but keep each case short.

For answer expressions:

- reduce `P=\dfrac{a}{b}` before computing `S`
- display substitution, e.g. `S=3a-2b=...`
- if final answer is rounded, state the rounding rule in the stem and use `lam_tron(value, digits)`

## Red Flags

Fix the generator if:

- cases overlap
- a complement omits a possible case
- independence is assumed without replacement
- event counts are multiplied when the choices are not independent
- geometric series uses a ratio outside `(0,1)`
- a probability exceeds `1` or is negative
- the final SA answer is a fraction when the prompt asks for an integer expression
