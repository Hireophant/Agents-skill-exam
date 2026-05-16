# Conditional Probability SA Playbook

Use this file when writing, repairing, or reviewing SP/xac-suat/xac-suat-co-dieu-kien short-answer questions. The local SA bank includes drawing without replacement, medical testing, and conditioned combinatorial counting such as lucky license plates containing a required digit.

## Core Arc

1. Define events clearly.
2. Identify what is known or conditioned on.
3. Compute the denominator of the conditional probability.
4. Compute the numerator, usually an intersection.
5. Use `P(A|B)=n(A cap B)/n(B)` or `P(A|B)=P(A cap B)/P(B)`.
6. Reduce the fraction or round the final requested probability.
7. Substitute into the requested expression.

Do not compute `P(A|B)` by intuition; always name both numerator and denominator.

## Without-Replacement Draws

Use for bottles, balls, prizes, and similar draws.

- First draw changes both total count and favorable count.
- Write `P(A)` and `P(B|A)` explicitly.
- For "both are favorable", use `P(A cap B)=P(A)P(B|A)`.
- Generate `total > favorable >= number_drawn` and avoid zero denominators.

For SA answers asking `m/n`, reduce the fraction before computing `T=cm+dn`.

## Medical / Diagnostic Bayes

Use for tests, disease prevalence, sensitivity, specificity, and false positives.

- Let `A` be the real condition and `B` the observed positive result unless the existing file uses a locked convention.
- Sensitivity: `P(B|A)`.
- Specificity: `P(\overline B|\overline A)`.
- False-positive rate: `P(B|\overline A)=1-P(\overline B|\overline A)`.
- Posterior probability:

```latex
P(A|B)=\dfrac{P(A)P(B|A)}
{P(A)P(B|A)+P(\overline A)P(B|\overline A)}
```

Rates must be plausible: prevalence small for screening stories, sensitivity and specificity between `0` and `1`, and final posterior within `[0,1]`.

## Conditioned Counting

Use for license plates or arrangements with known included digits/objects.

- Define `B` as the condition, e.g. "plate contains digit mid".
- Count `n(B)` first.
- Count `n(A cap B)` by disjoint cases.
- Then use `P(A|B)=n(A cap B)/n(B)`.

For pair-sum restrictions, group digits into singleton and paired sets. If a required digit is fixed, count the remaining positions by choosing compatible groups, then multiply by permutations.

## Randomization Guardrails

- Conditioning count/probability must be positive.
- Required object or digit must be available.
- Case counts must be disjoint and exhaustive.
- Probability fraction should be reduced before extracting numerator and denominator.
- Final expression should be positive unless the stem explicitly allows negative values.
- For rounded percent answers, use `lam_tron(value, digits)` and state the rounding rule in the stem.

## LaTeX And Presentation

Use a direct teacher rhythm:

```latex
Goi A la bien co ...
Goi B la bien co ...
Ta can tinh P(A|B).
Ta co ...
Theo cong thuc Bayes ...
Vay ...
```

For counting:

```latex
n(B)=...
n(A\cap B)=...
P(A|B)=\dfrac{n(A\cap B)}{n(B)}=...
```

If using a tree diagram helper, make sure branch labels match the event notation in the text.

## Red Flags

Fix the generator if:

- `P(A|B)` is accidentally replaced by `P(B|A)`
- replacement status is unstated or inconsistent
- denominator after conditioning is zero
- a diagnostic problem uses specificity as if it were false-positive rate
- a branch probability is rounded before Bayes
- a conditioned counting problem counts arrangements that violate the given condition
