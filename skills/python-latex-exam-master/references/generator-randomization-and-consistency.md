# Generator Randomization And Consistency

## Purpose

Use this file when random values, helper output, rounding, units, figures, formula display, or answers can silently drift apart. Pair display checks with [trinh-bay-cong-thuc-full.md](./trinh-bay-cong-thuc-full.md).

## Core randomization pattern

Filter invalid samples before composing the final statement:

```python
while True:
    # randomize numeric values
    # reject invalid or ugly cases
    if not condition:
        continue
    break
```

Add guards for:

- nonnegative physical or economic quantities
- capacity and feasibility bounds
- extrema lying inside the stated domain
- wrong answers staying distinct after final formatting
- realistic classroom ranges for practical stories
- geometry constraints such as a projection foot lying on the intended segment
- piecewise joins using one canonical shared point
- rounded final answers passing the requested precision check
- practical count answers using `ceil` when the context asks for a minimum whole number of objects, containers, trips, workers, products, months, or similar discrete units

## Compute values versus display values

Keep numeric values and LaTeX display strings separate.

- Treat `lam_tron(value, digits)` as display-first unless explicitly reconverted.
- Do not wrap `lam_tron(...)` with `int()` when the stem asks for one decimal place.
- Decimal-comma strings such as `1,7` should not be reused for arithmetic.
- Use `tinh_latex(expr)` for Sympy expressions, not already-formatted strings.
- Create display variables only after numeric values are finalized.
- Format display values according to `trinh-bay-cong-thuc-full.md`: decimal commas as `{,}` in LaTeX, numbers/formulas in math mode, units upright with a space, and exact-vs-rounded signs chosen correctly.

Safe pattern:

```python
mass_display = lam_tron(float(sp.N(mass)), 1)
mass_numeric = float(str(mass_display).replace(",", "."))
```

## Practical rounding versus minimum counts

Do not confuse ordinary rounding with minimum-count interpretation.

- If the stem asks for a decimal or says "lam tron den ...", use `lam_tron(value, digits)` only on the final displayed quantity.
- If the story asks how many whole objects are needed, such as paint cans, boxes, trips, workers, or containers, formulate the stem as "can toi thieu bao nhieu ..." and compute `math.ceil(exact_value)`.
- If an existing prompt says ordinary rounding but the real context requires a minimum whole count, flag the ambiguity and ask or revise the wording before coding.
- Keep both values when explaining: show the exact/approximate demand first, then conclude the minimum integer count.

## Shared source of truth

Derive each important quantity once and reuse it everywhere:

- statement
- answer key
- worked solution
- figure labels
- integral bounds
- units and rounding statements
- assertions and validity checks

If one value appears in multiple places, do not manually rewrite it in separate branches.

## Piecewise joins and glued figures

For functions, curves, or geometric objects joined at a point:

- define the join point once, for example `C = (t, yC)`
- reuse it in every branch, label, bound, and solution line
- reject samples unless all branches pass through that point
- recompute line coefficients from true endpoints, not display-only surrogates

Useful debug checks:

```python
assert sp.simplify(f_at_t - yC) == 0
assert sp.simplify(g_at_t - yC) == 0
```

## Final consistency pass

Before returning:

1. read the statement as a student would
2. read the figure as a student would
3. recompute the answer from stated quantities only
4. compare the worked solution against that recomputation
5. verify final formatting, units, and rounding
6. inspect the generated `.tex` near the edited region
