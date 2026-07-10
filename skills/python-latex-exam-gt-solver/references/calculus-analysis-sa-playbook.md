# Calculus/Analysis SA Playbook
## Mandatory notation standard

This playbook controls mathematical strategy only. For every displayed formula, symbol, unit, interval, system, probability/combinatorics notation, vector, integral, variation table, list, and aligned solution chain, obey `python-latex-exam-master/references/trinh-bay-cong-thuc-full.md`. Do not let shorthand examples in this playbook override that standard.

Use this file when writing, repairing, or reviewing GT short-answer questions. GT SA items often model real situations, so correctness includes the mathematical model, the practical domain, units, and final rounding.

## Core Arc

Write the problem and solution around this chain:

1. Analyze the target and state the method: derivative, integral, equation, inequality, or comparison.
2. Define the variable with unit and state the domain or interval from the story.
3. Build the function, integral, or exponential/logarithmic equation, then differentiate, integrate, or solve on the valid domain.
4. Check endpoints or practical constraints, convert units, round only the final result when required, and conclude in one sentence with a boxed answer.

## Applied Optimization

For cost, profit, material, speed, or production questions:

- Define revenue, each cost component, and profit/cost separately before combining.
- If time is `distance/speed`, convert power and hourly costs before building the total cost.
- If optimizing on a closed interval, compare endpoint values and critical points.
- If the generator intends an integer optimum, construct the coefficients so `f'(x)=0` has that root exactly; then do not present it as a random approximation.
- Use a variation table when it matches the bank style, but direct endpoint comparison is acceptable for longer real-world stories.

Random guardrails:

- positive speed, time, passenger count, production count, distance, and price
- optimum strictly inside the stated interval unless the problem is designed as endpoint optimization
- final cost/profit positive and plausible
- derivative root real and unique in the practical interval
- displayed answer passes `kiem_tra_lam_tron(lam_tron(...))`

## Integral Area And Volume

For area or volume generated from curves:

- Derive every curve from the stated points or continuity conditions.
- Use one canonical coordinate system and reuse it in statement, figure, solution, and integral bounds.
- For area, integrate upper minus lower on the actual interval; multiply by symmetry only after naming the symmetry.
- For volume of revolution, use `V=\pi\int r(x)^2 dx`; split the integral by physical pieces.
- If the stem figure is decorative, say it is illustrative and keep labels consistent with the data.

Use this integral style in solution text:

```latex
\displaystyle \int \limits_a^b f(x)\,\mathrm{d}x
```

## Growth, Decay, Logarithms

For Newton cooling, population growth, radioactive decay, or exponential models:

- Choose the time origin explicitly.
- Find the constant from the initial measurement.
- Use the second measurement to get the decay/growth factor.
- Check ratios are positive before taking logarithms.
- Interpret negative time carefully: if `t0<0`, the requested time before the origin is `-t0`.
- Keep minutes/hours conversion explicit.

Avoid physically odd data: cooling should move toward ambient temperature, populations should be positive and bounded if the model says so, and requested times should be reasonable.

For logistic growth items:

- Choose carrying capacity, initial value, and time scale in realistic units for the story. For plant-height models, heights in centimeters and month-based times should stay believable for a crop/plant over the stated number of months.
- When the question asks for the value of the modeled quantity at the time of maximum growth rate, solve the maximum of `f'(t)` but answer with `f(t)`, not with the time or the maximum rate unless explicitly asked.
- The logistic inflection condition can be shown by AM-GM/Cauchy or derivative analysis; preserve the reference solution route if the user supplies one.
- If `f(t*)` is exact, conclude with `=`. If the final requested value needs rounding, add a separate `\approx lam_tron(..., digits)` display only at the end.

## LaTeX And Human Presentation

The solution should read like a teacher explaining to a student:

- `Goi ... la ...`
- `Khi do ...`
- `Ta co ...`
- `Xet ... tren doan ...`
- `Suy ra ...`
- `Vay ...`

Use displayed equations for long expressions and short inline math for substitutions. Do not hide the model in code-style algebra.

For figure-heavy SA items, the stem figure may stay clean while the solution figure adds axes, coordinates, helper curves, or highlighted regions. Keep this separation explicit.

## Rounding And Units

For real-world SA answers, include the house wording in the stem when rounding matters:

```latex
\textit{\textbf{(khong lam tron ket qua trung gian, chi lam tron ket qua cuoi cung den ...)}}
```

Then in code:

- compute with exact Sympy or floats only for final numerical evaluation
- use `lam_tron(value, digits)` for display
- do not reuse decimal-comma strings in later arithmetic
- do not wrap a one-decimal answer in `int`
- convert units before final rounding, not after

For whole-number practical requirements, such as number of containers, trips, products, or workers, do not use ordinary rounding. Make the stem ask for the minimum count and compute with `ceil`; show the exact/approximate continuous value first, then conclude the minimum integer.

## Red Flags

Pause and fix the generator if:

- the optimizer is outside the stated interval
- area is negative because the curve order is reversed
- a volume formula forgot `pi` or squared radius
- a physical quantity becomes negative
- a threshold statement could flip after rounding
- the solution says "maximum/minimum" without derivative sign, variation table, AM-GM equality, or endpoint comparison
- the final answer has no unit while the stem asks for a practical quantity

## Lessons from KTL3.py (GT153SA021, GT153SA023, GT154SA034)

When implementing applied optimization question generators:
1. **Predefined Parameter Families**:
   - For travel time optimization across boundaries (e.g., road construction): Design the relationship between speeds (e.g. `v2 = 2 * v1` or `v2 = 3 * v1`) and dimensions beforehand so that the critical point $x$ solving $t'(x)=0$ is an exact integer.
   - For trachea diameter optimization: Select diameter $D$ from a discrete list of decimals divisible by 3 (e.g. `[0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7]`) so that the optimal radius $r = D/3$ resolves to a clean terminating decimal.
   - For cage/walkway area minimization: Choose configurations where $x_{opt} = \sqrt{\dfrac{w_x \cdot S_{water}}{w_y}}$ evaluates exactly to an integer.
2. **Pedagogical 4-Step Solution Structure**:
   Structure worked solutions using bold circle numbers:
   - `\textcolor{blue}{\textbf{\ding{172} Phân tích, định hướng tìm lời giải}}\\`
   - `\textcolor{blue}{\textbf{\ding{173} Đặt ẩn và lập hàm số}}\\`
   - `\textcolor{blue}{\textbf{\ding{174} Giải phương trình đạo hàm tìm cực trị}}\\`
   - `\textcolor{blue}{\textbf{\ding{175} Kết luận, so sánh với điều kiện}}\\`

## Lessons from KTL4.py (GT223SA011, GT224SA005)

When generating Calculus/Analysis short answer questions involving cooling models or piecewise integration:
1. **Cooling/Decay Model Decimal Precision**:
   - For temperature decay models ($f(t) = A_0 \cdot \left(\dfrac{a}{b}\right)^t$): Choose initial temperature $A_0$ and ratio $\dfrac{a}{b}$ (from exact terminating decimals such as `(4, 5)`, `(3, 4)`, `(7, 10)`, `(9, 10)`) and integer hours $t_1, t_2 = t_1 + 1$ to guarantee that intermediate temperatures $T_1, T_2$ are terminating decimals (validated via `abs(T - T_rounded) < 1e-9`).
2. **Piecewise Integration Continuity**:
   - For piecewise functions representing continuous physical quantities (e.g., solar energy $E(t)$ over a day), enforce mathematical continuity at boundary points (e.g. at $t=9$ and $t=15$) by dynamically calculating constants (e.g., $D_2 = 3 C_1 + D_1$ and $D_3 = 36 C_2 + D_2$) in the generator loop.
3. **Photosynthesis Process TikZ Diagram**:
   - Draw clean, colorful diagrams representing biological processes (e.g. green leaves, yellow light arrows, gray CO2, blue O2) with readable tiny labels (`\node[font=\tiny\bfseries]`) to visually support real-world word problems.


