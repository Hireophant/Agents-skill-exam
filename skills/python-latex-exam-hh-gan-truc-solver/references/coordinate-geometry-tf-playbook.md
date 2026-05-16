# Coordinate Geometry TF Playbook

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

