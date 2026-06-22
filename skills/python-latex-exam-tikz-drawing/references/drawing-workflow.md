# Drawing Workflow From Image Or Sample

Use this workflow for every figure in a stem or worked solution.

## 1. Read The Visual Contract

- Decide whether the figure is below the statement or beside it. Do not introduce `minipage` unless the sample places text and figure side-by-side.
- Separate stem-only elements from solution-only helper elements.
- List every point, segment, curve, shaded region, dashed guide, right-angle mark, axis tick, and label visible in the reference.
- Note which labels must stay readable. If a key label is cramped, adjust projection/coordinates so it is visible naturally.

## 2. Choose Coordinates Before Drawing

- Choose a simple coordinate system that matches the visual shape, not necessarily real scale.
- For randomized problems, keep one stable drawing model and randomize display labels if the user says the drawing should remain fixed.
- For real scaled diagrams, compute coordinates from canonical variables and keep display strings separate.
- Declare all main points first with `\coordinate`. Use uppercase names for mathematical points when the source uses uppercase labels.

## 3. Draw In This Order

1. Filled or shaded regions behind everything.
2. Hidden edges and dashed construction lines.
3. Main visible outlines and important segments.
4. Auxiliary lines, angle marks, perpendicular marks, ticks, arrows.
5. Points.
6. Labels.

This order avoids labels and helper lines being buried under fills.

## 4. Match House Style

- If the user already approved a TikZ helper function, preserve that layout exactly and patch only the requested region.
- Do not redraw a whole figure when the user asks to move one point, change one label, or fix one relation.
- If a sample has labels without white backgrounds, do not add white backgrounds just to hide collisions. Fix the geometry/anchor instead.
- Use comments sparingly inside TikZ to separate complex blocks such as `% Khoi lang tru`, `% Duong phu`, `% Nhan diem`.

## 5. Validate

- Check every coordinate used by `\draw`, `\fill`, `\node`, and `\path` was declared or is explicit.
- Check every TikZ calc expression has matching `$(`, `)!`, and `)$` syntax.
- Check all labels are math mode.
- Check hidden edges are dashed and visible edges are solid.
- Check figure placement follows the sample: below text, beside text, or inside solution.
- For Python files, generate/inspect the `.tex` output if available after a nontrivial figure edit.
