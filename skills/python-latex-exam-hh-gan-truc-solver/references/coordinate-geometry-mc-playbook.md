# Coordinate Geometry MC Playbook

## Purpose

Use this file when writing, repairing, or reviewing HH gan-truc-giai multiple-choice questions in Oxyz. The bank's MC style is short, formula-driven, and distractor-sensitive.

## Core pattern from the bank

Oxyz MC questions usually ask for one narrow object:

- one coordinate of a point or vector
- a midpoint, centroid, or special point
- a vector expression converted into a point
- a normal vector or plane-related coordinate
- cosine of an angle between a vector and an axis/unit vector

The solution should not become a long proof. It should identify the formula, substitute, and conclude.

## Solve-the-stem algorithm

1. Identify the target object exactly: coordinate, point, vector, centroid, normal, or cosine.
2. Convert all given geometric language into coordinate data.
3. Apply one canonical formula.
4. Build distractors from common nearby mistakes.
5. Check that all options remain distinct after formatting or rounding.

## Canonical formulas

- Point from vector: if `OC = (a;0;c)` then `C(a;0;c)`; if `CO = (-a;0;-c)`, still recover `C(a;0;c)`.
- Midpoint: `M = (A+B)/2`.
- Centroid: `G = (A+B+C)/3`.
- Vector from points: `AB = B-A`.
- Triangle validity: reject collinear or repeated points before asking for a centroid or plane.
- Plane normal from three points: `n = AB x AC`, then reduce or scale only after checking it is nonzero.
- Cosine with `i`: `cos(u,i)=u_x/|u|`; distractors can use `u_y/|u|`, `u_z/|u|`, or `sin`.

## MC distractor design

Good distractors should look like real student mistakes:

- sign flip from reading `OC` versus `CO`
- swapping y and z coordinates
- using `A+B-C` instead of `A+B+C`
- forgetting division by 2 or 3
- using the wrong coordinate in a cosine
- using an unreduced or wrong normal-vector component

Reject a sample if distractors collapse after `lam_tron(...)` or if two coordinate triples become identical.

## Code guardrails

- Use `while True` plus `continue` for repeated points, zero vectors, collinear triples, and duplicate answers.
- Keep numeric coordinate lists separate from display strings.
- Use helpers such as `kiemtrakhacnhau`, `kiemtrabadinhtamgiac`, `toado_tex`, `phanso`, and `tinh_latex` when the local file already uses them.
- Do not compute from a LaTeX string.
- For rounded MC answers, compare the final displayed options, not only raw values.

## Presentation style

Prefer a compact human explanation:

- "Ta co ..."
- "Suy ra ..."
- "Vay ..."

For MC, one or two displayed formulas are usually enough. Do not add a long coordinate-system justification unless the stem is a practical model rather than a pure coordinate item.

