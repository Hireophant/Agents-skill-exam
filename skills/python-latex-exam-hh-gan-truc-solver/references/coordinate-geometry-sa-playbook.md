# Coordinate Geometry SA Playbook
## Mandatory notation standard

This playbook controls mathematical strategy only. For every displayed formula, symbol, unit, interval, system, probability/combinatorics notation, vector, integral, variation table, list, and aligned solution chain, obey `python-latex-exam-master/references/trinh-bay-cong-thuc-full.md`. Do not let shorthand examples in this playbook override that standard.

## Purpose

Use this file when writing, repairing, or reviewing HH gan-truc-giai short-answer questions in Oxyz. This family often models real objects, so the solution must be mathematically correct and physically believable.

## Core pattern from the bank

Good SA items follow this arc:

1. analyze why a coordinate setup or geometric model is useful
2. choose or explain the coordinate system and set variables with conditions
3. translate the object into points, vectors, planes, or spheres, then derive the target quantity on the valid domain
4. check the conditions, apply the real-world unit conversion or cost/time interpretation, round only the final answer, and conclude with a boxed answer

Examples include roof thickness and cost, radar coverage, Earth great-circle distance, ants moving on a pyramid, distance from a point to a plane, and volume after assigning coordinates.

## Choose the coordinate system

A good coordinate setup should simplify the proof:

- Put the origin at a center, midpoint, or natural symmetry point.
- Align axes with edges, motion directions, or horizontal/vertical directions.
- In a regular pyramid, use the base center as origin and put the apex on the z-axis.
- In roof or floor problems, if two surfaces are perpendicular to `Oz`, use equations `z=c`.
- In motion problems, parameterize position by time only after fixing the valid time interval.

Do not introduce Oxyz only as decoration. The coordinate system should make at least one formula shorter.

## Real-world guardrails

Reject random samples that make the story implausible or ambiguous:

- lengths, radii, heights, depths, speeds, and costs must be positive
- a lateral edge must be long enough to produce a real height
- an optimum time must lie in the movement interval, or the endpoint case must be handled explicitly
- segment-sphere intersection must check the segment, not only the infinite line
- a radar/coverage problem should distinguish inside, outside, and boundary cases
- roof thickness, concrete volume, and total cost should stay in a believable range
- great-circle distances should use reasonable Earth radius and angle ranges
- rounded answers should pass `kiem_tra_lam_tron(...)`

For practical problems, prefer moderate numbers over dramatic values unless the story explains them.

## Common solution algorithms

### Distance to plane

1. Compute two direction vectors in the plane.
2. Compute `n = AB x AC`.
3. Write the plane equation.
4. Apply point-plane distance.
5. Round the final value only.

### Moving points

1. Define the valid time interval.
2. Write each position as a function of `t`.
3. Compute `d^2(t)` instead of `d(t)`.
4. Minimize the quadratic on the interval, not on all real numbers.
5. Convert the minimum back to the requested unit.

### Sphere or coverage

1. Write the center and radius.
2. Compute distance or intersection using exact values.
3. Check whether the relevant point or foot lies in the practical domain.
4. State the practical conclusion clearly.

### Cost or volume

1. Derive the geometric thickness, area, or volume first.
2. Convert units before money computation.
3. Compute each cost component separately.
4. Add and round in the requested unit, such as million dong.

## LaTeX presentation

- Show the figure in the stem only if it helps the reader understand the real object.
- If the solution needs axes or helper marks, use a separate solution figure.
- Use `\left(...\right)` for coordinate triples when the file already uses that style.
- Use `\cdot` for multiplication in algebraic cost/volume lines when matching the local style.
- Keep one displayed formula per major transition.
- End with a sentence that answers the exact question and unit.
- For real-object figures such as a crane, car frame, tank, or logo, prioritize the reference silhouette and mathematically important labels over decorative details. Remove clutter such as fences or extra fills if they make the target object harder to read.
- If the solution uses an abstracted geometric model, draw the clean model there and keep it consistent with the force/coordinate notation in the calculation.
- When final answers are rounded, include the stem's requested rounding phrase and use `\approx` only in the final rounded line; keep exact expressions earlier.
- When the final real-world answer is a whole count, such as number of units, sheets, cans, or trips, word the stem as a minimum-count question and use `ceil` rather than ordinary rounding.

## Code habits

- Keep symbolic expressions exact until the final `lam_tron`.
- Store display strings separately from numeric values.
- Use `tinh_latex` for Sympy expressions and direct strings for final display values.
- Build helper functions for repeated formatting such as money, coordinates, or degree-minute parsing.
- Run sample generation after edits and inspect the generated `.tex`.

## Lessons from KTL4.py (HH254SA014)

When generating Oxyz coordinate geometry short answer questions involving movement vectors (e.g., tunnel drilling towards a meetup point $E$):
1. **Collinear Motion & Coordinate Ratios**:
   - Define exact integer vector direction candidates `AB_dirs` (lengths like 3, 9, 6) to ensure the first path length is an integer.
   - Solve for meeting point coordinates $E$ based on the vector ratio $k = AE / AB$.
   - Format coordinates dynamically to avoid `+ -` sign issues in f-strings: `x_E_expr = f"{xA} - {abs(k * dx1)}" if k * dx1 < 0 else f"{xA} + {k * dx1}"`.
2. **Non-collinear Vector Search Spaces**:
   - Programmatically search for the second starting point $C$ using direction candidates `CE` that are not collinear with $AB$ (cross product `cross_x != 0 or cross_y != 0 or cross_z != 0`).
   - Validate that the computed velocity $v_2 = (L_2 \times 100) / t$ is an exact integer in a realistic range (e.g. `3 <= v2 <= 30` and `v2 != v1`).
3. **Mountain and Tunnel TikZ Diagram**:
   - Use bezier curves to draw illustrative backgrounds (e.g. `\draw[fill=gray!8] (-0.5,-0.5) to[out=30,in=150] (2.2,2.5) ...`), dashed lines for tunnels (`line width=2.5pt, dashed`), and coordinate vectors with arrows (`\draw[->, ultra thick]`) to help students visualize Oxyz real-world problems.

