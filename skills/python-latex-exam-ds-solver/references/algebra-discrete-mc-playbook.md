# Algebra / Discrete Math MC Playbook

Use this file when writing, repairing, or reviewing DS multiple-choice questions. The current DS MC bank contains log inequalities and geometric sequences, so this reference focuses on strict domain logic, interval formatting, and index-sensitive sequence formulas.

## Core Pattern

DS MC should test one clean algebraic decision:

- solve a logarithmic inequality and return the exact solution set
- combine log domain with a quadratic inequality
- compute one term of a geometric sequence from a known term and common ratio

Do the full algebra before writing options. MC options should be short and visually parallel.

## Log-Inequality Algorithm

1. Find the domain first, before using log monotonicity.
2. Decide whether the base is greater than `1` or between `0` and `1`.
3. Convert the logarithmic inequality to an algebraic inequality, flipping the inequality only when the base is `<1`.
4. Solve the algebraic inequality.
5. Intersect with the domain.
6. Encode strict endpoints with parentheses and equality endpoints with brackets.

For `log_{1/q}(a^x-a^L)>-m`, the local pattern is:

- domain: `a^x-a^L>0 => x>L`
- base `<1`, so the inequality direction flips
- solve `a^x-a^L<q^m`
- get the final interval `(L;R)`

For `log_a(f(x)) <= k` with `a>1`, combine:

- domain `f(x)>0`
- bound `f(x)<=a^k`
- final solution is the intersection, often a union such as `[r3;r1) cup (r2;r4]`

## Geometric Sequence Algorithm

For a geometric sequence:

```latex
u_n=u_m\cdot q^{n-m}
```

Guard against degenerate random values:

- `q` must not be `0`, `1`, or `-1` unless that is the intended lesson.
- the requested index must differ from the given index.
- if `q<0`, keep the sign changes intentional and ensure distractors remain distinct.

Good distractors are `q^{n-m+1}`, `q^{n-m-1}`, and sign mistakes, but check they do not collapse to the correct answer.

## Distractors

Build distractors from realistic student errors:

- ignoring the log domain
- forgetting to flip inequality when the log base is `<1`
- using closed brackets for strict log-domain endpoints
- taking the interval before intersecting with the domain
- merging two intervals into one interval
- using `u_n=u_m q^{m-n}` or shifting the exponent by one

Always verify the four displayed choices are different after `tinh_latex`, fraction formatting, and interval formatting.

## Code And LaTeX Habits

- Use `while True` to force clean powers, ordered roots, nonempty intersections, and distinct choices.
- Keep display strings separate from Sympy values.
- Use `tinh_latex(...)` for roots, powers, rational values, and sequence answers.
- Avoid output like `+ -5`; format negative constants as subtraction.
- Prefer `\dfrac{1}{q}` in worked solutions and `\tfrac{1}{q}` in compact problem statements if space is tight.

## Solution Style

Use a concise teacher chain:

```latex
Dieu kien xac dinh: ...
Vi co so ... nen ...
Ket hop voi dieu kien ...
Vay ...
```

For log questions, never start by exponentiating before stating the domain. For sequence questions, state the formula once, substitute, then conclude.
