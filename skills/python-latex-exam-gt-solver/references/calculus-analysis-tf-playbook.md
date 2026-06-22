# Calculus/Analysis TF Playbook
## Mandatory notation standard

This playbook controls mathematical strategy only. For every displayed formula, symbol, unit, interval, system, probability/combinatorics notation, vector, integral, variation table, list, and aligned solution chain, obey `python-latex-exam-master/references/trinh-bay-cong-thuc-full.md`. Do not let shorthand examples in this playbook override that standard.

Use this file when writing, repairing, or reviewing GT true-false questions. A good GT TF item feels like one coherent model with four checkpoints, not four unrelated exercises.

## Four-Statement Structure

Build the four statements from easy to hard:

- Statement 1: setup, domain, initial value, coefficient, equation, or a direct reading.
- Statement 2: a computed value at a given input, an integral, or a simple unit conversion.
- Statement 3: the full model, derivative, area, volume, asymptote, or monotonic interval.
- Statement 4: the applied conclusion: minimum cost, maximum profit, required time, threshold, volume, mass, or practical comparison.

Each statement should have a true and false version that are close in wording and difficulty. The false version should be a realistic near-miss, not an obviously fake sentence.

## Common GT Models

- Cost with speed: define time per unit distance, cost per hour, then convert to cost per distance before optimizing.
- Profit: revenue minus fixed cost and variable cost; optimize only on the stated interval.
- Cooling/growth: use the initial value to find the constant, use a second measurement to find the decay/growth factor, then solve the requested time.
- Area between curves: derive the line/parabola/curve equation from points, integrate upper minus lower on the correct interval, and multiply by symmetry only when justified.
- Volume of revolution: use `pi int r(x)^2 dx` and split the integral when the shape is piecewise.
- Graph or variation-table items: separate domain, derivative signs, extrema, and conclusion.

## Practical Guardrails

Random data must make the story believable.

- Speeds, times, temperatures, populations, radii, costs, and dimensions must be positive and in a natural range.
- If optimizing on `[a;b]`, check the candidate root lies inside the interval and compare endpoints when needed.
- If using AM-GM/Cauchy for a minimum, all terms must be positive and equality must occur at the generated answer.
- For piecewise geometry, integral bounds must match each physical part, not one global coordinate by accident.
- If a statement compares with a threshold, choose the threshold on the correct side of the exact value and far enough from rounding ambiguity.
- For real money, if the exact value is not an integer, state the practical rounded/ceiling value explicitly.

## Limit And Threshold Statements

For applied concentration, production, temperature, or long-run GT questions, separate the limiting value from finite-time values.

- If `f(t)` is increasing and `f(t) -> L` from below, then a rule "khong vuot qua L" can still allow long-run production; the statement "khong the san xuat lien tuc" is false at `L` or above.
- To make a true "khong the san xuat lien tuc" statement, use a threshold strictly below the limit.
- To make a false "khong the san xuat lien tuc" statement, use `L` or preferably `L+1` when values are integer and the wording should be unambiguous.
- If the user asks the true statement to use exactly the limiting value, change the conclusion to "co the san xuat lien tuc" and keep the false statement as `L+1` with the wrong "khong the" conclusion.
- In the worked solution, avoid vague `Vi threshold < L` wording when the conclusion depends on a limit convention; write `Khi t -> +infty ... Vay voi tieu chuan ...` so the conclusion matches the statement exactly.
- For concentration models, define concentration in the statement before using the function: mention that dissolved sugar does not significantly change the water volume when that assumption matters, then write `f(t)=...` with the intended domain.
- Order concentration TF statements as setup/model first, then function behavior, then applied threshold conclusion. Do not test monotonicity before defining the concentration function.
- Avoid vague phrases such as "thoi gian dai"; use a concrete production/process phrase such as "trong thoi gian san xuat" or "trong suot qua trinh ...".
- Keep thresholds randomized from the model: use the generated limit `L` for the true "luon nho hon L" conclusion and `L+1` for a false "co thoi diem dat hon L+1" conclusion when `L` is an integer.
- If an earlier statement has already proved monotonicity on `t>0`, cite it in the later threshold solution (`Theo y c...`) instead of repeating the derivative calculation.

## Code Pattern

Use named statement variables:

```python
PAtrue1 = f"\\True {st1_true}"
PAfalse1 = f"{st1_false}"
LGPAtrue1 = (...)
```

Then return:

```python
format_output_TFquestion(
    PAtrue=[PAtrue1, PAtrue2, PAtrue3, PAtrue4],
    PAfalse=[PAfalse1, PAfalse2, PAfalse3, PAfalse4],
    LGtrue=[LGPAtrue1, LGPAtrue2, LGPAtrue3, LGPAtrue4],
    debai=debai,
    QC=QC,
    for_moodle=for_moodle,
)
```

Keep `LGPAtrue` solutions ordered the same way as the statements. If later statements reuse work from earlier statements, either repeat the needed formula briefly or say `Tu y tren`.

## False Statement Patterns

Use one local mistake per false statement:

- wrong unit conversion, such as per hour instead of per kilometer
- missing `pi` in a surface or volume formula
- integrating a whole curve instead of one physical piece
- using lower minus upper for area
- using `v^3` instead of `v^2` after converting hourly cost to cost per distance
- changing a threshold across the exact value
- forgetting the domain restriction when solving a logarithm or derivative equation

Do not make all false statements simple sign flips. Mix algebraic, modeling, unit, and conclusion errors.

## Solution Style

For easy checks, one or two lines are enough. For applied checks, write the model clearly:

```latex
Goi v la ...
Thoi gian ...
Suy ra C(v)=...
Xet C'(v)=0 ...
Vay ...
```

For integral applications, use the house style:

```latex
\displaystyle \int \limits_a^b f(x)\,\mathrm{d}x
```

Use `=` for exact generated values and `\approx` only for genuine numerical approximations.
