# Algebra / Discrete Math SA Playbook

Use this file when writing, repairing, or reviewing DS short-answer questions. The current DS SA bank includes linear programming, practical investment/production, geometric sums, compound interest, and logarithmic sound-level models.

## Core Arc

1. Define variables with units.
2. Translate every real-world condition into an equation, inequality, sequence, or logarithmic relation.
3. Solve only inside the valid practical domain.
4. Use exact algebra as long as possible.
5. Convert units and round only the final answer.
6. Conclude with the requested numeric answer and unit.

## Linear Programming Models

Use for investment funds, farms, vehicle sales, and production constraints.

- Define `x,y` in the same unit used by the constraints, such as billion VND, hectares, or number of vehicles.
- Put all constraints in a clean system.
- Generate a nonempty feasible polygon and avoid nearly coincident vertices.
- Use `ve_mien_bpt_TikZ(...)` or the local feasible-region helper to draw the region.
- Evaluate the objective function at every vertex returned by the helper.
- If the variable is a count of vehicles/items, ensure candidate vertices are integral or make the statement allow continuous planning.
- Keep axis units readable; scale large money values instead of drawing million-unit coordinates directly.

Typical solution rhythm:

```latex
Goi x,y lan luot la ...
Tu de bai, ta co he BPT ...
Mien nghiem la mien da giac co cac dinh ...
Xet T(x,y)=...
Tinh T tai cac dinh ...
Vay ...
```

## Geometric Sum And Game Models

Use for candy, rewards, staged payments, or repeated halving.

- Name the original total `x`.
- Write the first few terms so the rule is visible.
- Then compress with `...` and a geometric-sum formula.
- Make sure the final remaining amount and the winning-round amount are counted on the correct side of the equation.
- Since candies/items are discrete, generate parameters so the final answer is an integer.

For repeated halving, guard with exact fractions rather than floats. Verify the final count using integer arithmetic, not only formatted display.

## Compound Interest And Savings

Use for monthly deposits, salary percentages, and purchase goals.

- State whether deposits are at the beginning or end of each month.
- If the problem says "after the last deposit exactly one month", the first deposit accumulates one more month than a standard end-of-period annuity.
- Use a geometric sum for accumulated value.
- Keep salary, deposit percent, price, and interest rate in compatible units.
- Generate a practical percentage such as `1 <= a <= 80`; avoid impossible savings rates.

Do not cast the final percentage to `int` when the stem asks for one decimal place. Use `lam_tron(a_value, 1)`.

## Logarithmic Sound-Level Models

Use for sound intensity, distance ratios, and seat-position problems.

- Check all distances and log arguments are positive.
- If seats are equally spaced, express intermediate distances as a fraction of the total row distance.
- Use the identity

```latex
L_2-L_1=2\log\frac{R_1}{R_2}
```

- Make monotonic direction realistic: farther seats should not have higher sound level when the source and seats are collinear away from the source.
- Keep the requested seat strictly between the first and last seats.

## Trigonometric Application Models

Use for rotating wheels, buckets, periodic height/distance models, or first-time questions.

- If the stem asks for the first occurrence after a starting time, say it explicitly: "Ke tu thoi diem x=0 ... sau bao nhieu phut?"
- For `h=|y|`, solve both cases in the same presentation rhythm unless the user explicitly wants a geometric shortcut: `y=h` and `y=-h`.
- When the negative case is impossible but the expected style is computational, show the substitution through the sine equation, for example `sin(...)= -2d/R`, then conclude no solution because the value is outside `[-1,1]`.
- To find the first valid time, solve the general solution, impose `x>=0`, derive the integer condition on `k`, then choose the smallest integer `k`; do not rely on ad hoc listing unless the sample solution does.
- Keep the conclusion aligned with the stem: if the stem asks "sau bao nhieu phut", end with "sau ... phut", not only "vao thoi diem x=...".

## Randomization Guardrails

Use `while True` when any of these can fail:

- feasible region is empty or unbounded
- vertex list has too few points or duplicate points
- optimal value ties unintentionally
- item/candy/vehicle answer is not an integer
- investment or salary percentage is unrealistic
- log ratio is nonpositive
- displayed rounded value fails `kiem_tra_lam_tron`

## LaTeX And Formatting

- Use `\left\{\begin{array}{l}...\end{array}\right.` for systems.
- Use `\dfrac` for classroom fractions.
- Keep decimal commas only in final display strings; do not reuse them in computation.
- Use `\textit{\textbf{(...)}}` for rounding instructions when matching the local bank style.
- If a solution includes a figure, place the TikZ block after the system and before vertex evaluation.

## Red Flags

Fix the generator if:

- a problem about vehicles, people, candies, or items returns a fractional final count
- the objective maximum is claimed without evaluating vertices
- the savings timeline is off by one month
- the feasible-region graph uses units different from the statement
- a log model produces a physically reversed conclusion
- the final answer omits the unit requested in the stem
