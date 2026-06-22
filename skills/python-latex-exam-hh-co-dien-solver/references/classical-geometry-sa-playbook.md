# Classical Geometry SA Playbook
## Mandatory notation standard

This playbook controls mathematical strategy only. For every displayed formula, symbol, unit, interval, system, probability/combinatorics notation, vector, integral, variation table, list, and aligned solution chain, obey `python-latex-exam-master/references/trinh-bay-cong-thuc-full.md`. Do not let shorthand examples in this playbook override that standard.

## Purpose

Use this file when writing, repairing, or reviewing a classical geometry short-answer problem from the HH co dien bank.

## Core observation

These SA problems begin by creating the right auxiliary object, then converting the 3D target into a standard 2D or scalar target.

Common reductions:

- dihedral angle -> angle in a perpendicular section
- skew-line distance -> point-plane distance or common perpendicular
- volume -> base area times true height
- painted area -> sum of standard faces
- practical viewing or geometry maximum -> one-variable model

## Solve-the-stem algorithm

1. Identify the final target: angle, distance, area, volume, length, or extremum.
2. Choose the standard reduction and briefly explain the direction of the solution.
3. Introduce only the auxiliary points or planes needed for that reduction, with any required conditions.
4. Convert the spatial target to a 2D angle, right triangle, distance-to-plane, area sum, or one-variable model, then solve in a strict chain.
5. Check the result against the original geometry, return to the requested target, and conclude with a boxed answer.

## Human-style presentation

SA solutions may be longer than MC, but each line should unlock the next step.

Common rhythm:

- "Goi ..."
- "Dung ..."
- "Ta co ..."
- "Do ... nen ..."
- "Suy ra ..."
- "Vay ..."

Open with the construction, not the arithmetic. State why a line is perpendicular or why a plane is parallel before using the consequence.

## Canonical moves

- Dihedral angle: build a perpendicular section, expose a right triangle, then use one trig ratio.
- Skew-line distance: build a parallel plane or common perpendicular, then reduce to a point-plane distance.
- Hidden height or frustum volume: identify the true height first, compute the base area separately, then use the formula.
- Painted area: split into base, top, and lateral faces; compute one lateral face and multiply by symmetry.
- Box or prism intersection: locate the key point with parallelism, orthogonality, or Thales before computing the requested length.
- Practical extremum: set one geometric variable, express the objective, and maximize with a clean inequality or derivative.
- Practical whole-count results, such as number of tiles, paint cans, or pieces needed, require a "toi thieu" stem and `ceil`, not ordinary rounding.

## Red flags

- calculating before the section or auxiliary object is identified
- declaring perpendicular or parallel relations without a reason
- jumping from a spatial target directly to a trig formula
- rounding an intermediate value and reusing it
- introducing helper points that do no work
