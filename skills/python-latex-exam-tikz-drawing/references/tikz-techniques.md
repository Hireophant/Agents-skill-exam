# TikZ Techniques For Exam Figures

This reference distills the user's `Vehinh.pdf` into reusable rules and snippets. Prefer the existing local file style if it differs.

## Basic Environment

Use:

```latex
\begin{tikzpicture}[scale=1, line join=round, line cap=round, >=stealth]
...
\end{tikzpicture}
```

Only include package/library declarations in a document preamble, not inside generated problem strings. Common libraries: `calc`, `intersections`, `angles`, `quotes`, `patterns`, `tkz-tab` when the project already loads them.

## Points And Segments

Declare points once:

```latex
\coordinate (A) at (0,0);
\coordinate (B) at (3,0);
\coordinate (C) at (1,2);
```

Draw segments or polygons:

```latex
\draw (A)--(B);
\draw (A)--(B)--(C)--cycle;
```

For midpoint/ratio:

```latex
\coordinate (M) at ($(A)!0.5!(B)$);
\coordinate (N) at ($(A)!0.25!(B)$);
```

For vector translation:

```latex
\coordinate (D) at ($(C)+(1,2)$);
```

## Labels And Points

Use nodes in math mode and choose anchors deliberately:

```latex
\fill (A) circle (1.2pt);
\node[below left] at (A) {$A$};
```

Use `above`, `below`, `left`, `right`, and combinations. Nudge with `shift={(...)}` only when the anchor is not enough.

## Intersections

When exact intersections matter and the paths are named:

```latex
\draw[name path=d1] (A)--(B);
\draw[name path=d2] (C)--(D);
\path[name intersections={of=d1 and d2, by=H}];
```

For two intersections, use the generated names or declare them:

```latex
\path[name intersections={of=c1 and c2}];
\coordinate (M) at (intersection-1);
\coordinate (N) at (intersection-2);
```

## Perpendiculars And Projections

Projection of a point `A` onto line `BC`:

```latex
\coordinate (H) at ($(B)!(A)!(C)$);
\draw[dashed] (A)--(H);
```

Only draw a right-angle mark when the sample has one or the solution needs it.

## Curves, Arcs, Circles, Ellipses

Circle and ellipse:

```latex
\draw (O) circle (2);
\draw (O) ellipse ({3} and {1});
```

Arc:

```latex
\draw (1,0) arc[start angle=0, end angle=120, x radius=2, y radius=2];
```

Bezier curve:

```latex
\draw (A) .. controls (P) and (Q) .. (B);
```

Use curves for decorative/organic shapes only when the source figure requires them.

## Axes And Function Graphs

For coordinate axes:

```latex
\draw[->] (-2,0)--(3,0) node[below] {$x$};
\draw[->] (0,-1)--(0,4) node[left] {$y$};
\node[below left] at (0,0) {$O$};
```

For function graphs:

```latex
\draw[domain=-1:3, smooth, samples=100, variable=\x]
  plot ({\x},{(\x)^3-3*(\x)^2+3});
```

Use explicit `domain`, `samples`, and `smooth`. In TikZ math, write multiplication with `*`, powers with `^`, and fractions with `/`.

For shaded graph regions, use `patterns` or clipped scopes when exact boundaries matter.

## Solids And 3D-Style Figures

For prisms/boxes, declare bottom face, top face as a translation, then draw visible and hidden edges separately:

```latex
\coordinate (A) at (0,0);
\coordinate (B) at (3,0);
\coordinate (C) at (4,1);
\coordinate (D) at (1,1);
\coordinate (Ap) at ($(A)+(0.8,2.2)$);
\coordinate (Bp) at ($(B)+(0.8,2.2)$);
\coordinate (Cp) at ($(C)+(0.8,2.2)$);
\coordinate (Dp) at ($(D)+(0.8,2.2)$);
\draw (A)--(B)--(C)--(D)--cycle;
\draw (Ap)--(Bp)--(Cp)--(Dp)--cycle;
\draw (B)--(Bp) (C)--(Cp) (D)--(Dp);
\draw[dashed] (A)--(Ap);
```

For exam geometry, pick a projection that makes helper points and labels visible. Preserve the sample's dashed/solid convention over geometric photorealism.

## Filling And Shading

Use `\fill` for simple transparent regions:

```latex
\fill[cyan!25, opacity=0.55] (A)--(B)--(C)--cycle;
\draw (A)--(B)--(C)--cycle;
```

Use patterns for hatched regions:

```latex
\fill[pattern=north east lines, pattern color=gray!70] (A)--(B)--(C)--cycle;
```

Always draw important borders again after filling if the fill covers line clarity.

## Variation Tables

If the project already has helper functions such as `bbtb2CTC(...)`, use those instead of hand-writing a new table. If hand-writing is required, use `tkz-tab` style consistently with existing files.
