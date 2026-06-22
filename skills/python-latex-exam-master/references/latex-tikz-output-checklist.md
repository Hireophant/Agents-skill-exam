# LaTeX TikZ Output Checklist

## Purpose

Use this file when LaTeX fails to compile, a TikZ drawing is malformed, or the generated `.tex` layout differs from the Python source.

## Formula-standard checks

Read [trinh-bay-cong-thuc-full.md](./trinh-bay-cong-thuc-full.md) before finalizing any formula-heavy statement or solution. In particular, verify math mode for formulas/numbers, punctuation placement around `$...$`, decimal comma `{,}`, upright units, prescribed probability/combinatorics symbols, `\mathrm{d}x`, interval delimiters with `\left...\right`, BBT settings, and aligned equation chains.

## LaTeX checks

1. Match every `$`, `\left`, `{`, and environment opening with a close.
2. Escape braces and backslashes correctly inside Python f-strings.
3. Ensure inserted strings are safe for the surrounding LaTeX context.
4. Avoid stray `\\` after display math or environment endings.
5. Inspect the emitted `.tex`, not just the Python source, for spacing and layout bugs.

Representative failures:

- "There's no line here to end"
- "Command \item invalid in math mode"
- "Display math should end with $$"
- missing TikZ semicolon
- decimal comma inserted where raw numeric parsing is expected

## Integral style

The default integral notation must follow `TrinhBayCongThuc.pdf`: use display style with limits and upright differential, for example `\displaystyle\int\limits_a^b f(x)\mathrm{\,d}x`. If the user has locked an integral style more specifically, reuse it everywhere in the same file. A stable handwritten pattern is:

```python
f"\\displaystyle \\int \\limits_{{{a}}}^{{{b}}} \\left[f(x)\\right]^2\\,\\mathrm{{d}}x"
```

## TikZ checks

1. End each drawing command with `;`.
2. Match each `\begin{scope}` with `\end{scope}`.
3. Verify every named point is defined before use.
4. Keep segment commands aligned with the current geometry, not an old template.
5. Fill shaded regions fully to the intended boundary or axis.
6. If a single fill path leaves a visual gap, split the fill into multiple same-style subregions.
7. Make illustrative figures visually credible: collinear points should look collinear, projections should sit on intended lines, and midpoint labels should sit on intended segments.
8. After moving points, re-check every point that should lie on an edge actually uses interpolation on that edge, not a nearby free coordinate.
9. For labels on opposite sides of a figure, set anchors deliberately (`left`, `right`, `above`, `below`) instead of relying on default placement; this prevents text such as repeated `x` labels from colliding with edges.
10. If two projected points share the same coordinate value on an axis, show the value once, not twice on top of itself.
11. Do not color helper faces or extra regions in the stem figure unless the reference image does; reserve extra shading/annotations for the solution figure.

## Generated `.tex` check

After a layout-sensitive patch, inspect the emitted `.tex` around the changed lines.

Look for:

- `\itemch` immediately followed by a figure block that should appear below the item label
- `minipage` widths or scales that make a figure drop below its partner
- helper wrappers injecting `\par`, `\noindent`, or `\\`
- Python code that looks correct but expands into a different classroom layout
