# Coordinate Geometry TF Playbook
## Mandatory notation standard

This playbook controls mathematical strategy only. For every displayed formula, symbol, unit, interval, system, probability/combinatorics notation, vector, integral, variation table, list, and aligned solution chain, obey `python-latex-exam-master/references/trinh-bay-cong-thuc-full.md`. Do not let shorthand examples in this playbook override that standard.

## Purpose

Use this file when writing, repairing, or reviewing HH gan-truc-giai true-false questions in Oxyz. These questions should feel like one coherent model with four focused checks, not four unrelated mini-problems.

## Core pattern from the bank

The strong TF examples use one real or geometric setting, then test four layers:

- coordinate interpretation or vector from points
- line, plane, or sphere equation
- a distance, velocity, or parameter calculation
- a final logical conclusion in the story

Examples include a badminton shuttle crossing a net plane, an AUV route avoiding a sensitive sphere, a moving object under angle data, or a plane through points.

## Build the four statements

Use matched true/false variants:

1. Statement about coordinates or vector direction.
2. Statement about the equation of a line, plane, or sphere.
3. Statement about a computed value such as distance, height, velocity, or closest point.
4. Statement about the practical conclusion, such as blocked/not blocked or intersects/does not intersect.

Keep false statements plausible:

- change one sign in a direction vector
- use radius `R` instead of `R^2` in a sphere equation
- use the wrong coordinate plane such as `x=L/2+1`
- shift a rounded value by a small but visible amount
- reverse the practical conclusion only after the true calculation is clear

## Real-world guardrails

Add hidden constraints before composing statements:

- A and B must be distinct.
- Direction vectors used in symmetric form should have nonzero components.
- For a line-sphere route, avoid `d=R`; tangency makes the final conclusion ambiguous.
- For segment-sphere intersection, ensure the perpendicular foot parameter satisfies `0<t<1`; distance from the infinite line is not enough.
- For a moving object crossing a net or plane, intersection time must be positive and inside the meaningful interval.
- Heights and depths should be positive and plausible for the story.
- If a conclusion depends on a height interval, explicitly check membership in that interval.

## Solution style

Each `LGPAtrue` should justify the true version of its paired statement. Use the same order as the prompt.

Preferred rhythm:

- compute the vector or equation first
- show the formula
- substitute values
- state the story conclusion

For practical conclusions, name the condition:

- "Do d(K,AB) < R va chan vuong goc nam tren doan AB ..."
- "Vi z_H nam trong khoang [h0;h_top] ..."
- "Vi vec v nguoc huong vec u nen vec v = k vec u, k<0 ..."

For coordinate-midpoint or figure-reading statements:

- Use the user's approved bracket-coordinate rhythm when present, for example `[I]=\dfrac{[M']+[N']}{2}`.
- If the solution needs a supporting 2D cross-section sketch, draw only the relevant section and omit labels that are not used in the calculation.
- Keep helper point names consistent between the figure and solution. If a point is actually `M`, do not introduce an extra `H` just for a right-angle foot.

## Code structure

- Build `PAtrue1..4`, `PAfalse1..4`, and `LGPAtrue1..4` from the same canonical variables.
- If the truth of the fourth statement can flip, assign `PAtrue4` conditionally so `LGPAtrue4` always explains the true statement.
- Keep formatted equations in variables such as `line_true`, `line_false`, `sphere_true`, `sphere_false`.
- Use `QC` and `for_moodle` exactly as the local formatter expects.

## Red flags

- using line-sphere distance to decide a segment collision without checking the foot lies on the segment
- letting true and false statements differ too much in wording
- explaining the false statement instead of the true paired statement
- using a rounded value to decide a geometric inequality
- generating a story where the object crosses the plane behind the starting point

## Lessons from KTL3.py (HH194TF002)

When writing Oxyz coordinate geometry generators (especially for vector operations, trapezoids, and angle bisectors):
1. **Exact Vector Lengths**:
   - Use Pythagorean quadruples (`(2, 1, 2)`, `(2, 3, 6)`, `(4, 4, 2)`) to generate vectors that yield exact integer lengths, preventing float precision errors in distance checks.
2. **Preventing Collinearity & Division by Zero**:
   - Verify that vectors are not collinear by checking that their cross product is not the zero vector (`cross_x != 0 or cross_y != 0 or cross_z != 0`).
   - Check that any vector components used in the denominator of ratios (e.g. `\dfrac{a-x_C}{-u_x}`) are non-zero.
3. **Trapezoids & Plane Constraints**:
   - When solving for a point $D$ lying on the $Oxy$ plane ($D(a, b, 0)$) such that $ABCD$ is a trapezoid (either $BA \parallel CD$ or $AD \parallel BC$), ensure the calculated $D$ does not coincide with $A, B$, or $C$.
4. **Angle Bisector Theorem**:
   - When solving for the angle bisector foot $E$ using $\overrightarrow{EB} = -\dfrac{AB}{AC} \cdot \overrightarrow{EC}$, enforce $AB \neq AC$ to keep the triangle non-isosceles, ensuring that false distractors (like using the outer bisector formula $\overrightarrow{EB} = \dfrac{AB}{AC} \cdot \overrightarrow{EC}$) have a well-defined non-zero denominator.

