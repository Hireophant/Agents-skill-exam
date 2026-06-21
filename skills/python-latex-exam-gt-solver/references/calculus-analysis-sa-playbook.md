# Calculus/Analysis SA Playbook

Use this file when writing, repairing, or reviewing GT short-answer questions. GT SA items often model real situations, so correctness includes the mathematical model, the practical domain, units, and final rounding.

## Core Arc

Write the problem and solution around this chain:

1. Define the variable and unit.
2. State the domain or interval from the story.
3. Build the function, integral, or exponential/logarithmic equation.
4. Differentiate, integrate, or solve the equation on the valid domain.
5. Check endpoints or practical constraints when needed.
6. Convert units and round only the final result.
7. Conclude in one sentence with the requested answer format.

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

## Red Flags

Pause and fix the generator if:

- the optimizer is outside the stated interval
- area is negative because the curve order is reversed
- a volume formula forgot `pi` or squared radius
- a physical quantity becomes negative
- a threshold statement could flip after rounding
- the solution says "maximum/minimum" without derivative sign, variation table, AM-GM equality, or endpoint comparison
- the final answer has no unit while the stem asks for a practical quantity
