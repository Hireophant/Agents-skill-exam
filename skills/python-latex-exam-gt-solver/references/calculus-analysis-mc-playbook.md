# Calculus/Analysis MC Playbook
## Mandatory notation standard

This playbook controls mathematical strategy only. For every displayed formula, symbol, unit, interval, system, probability/combinatorics notation, vector, integral, variation table, list, and aligned solution chain, obey `python-latex-exam-master/references/trinh-bay-cong-thuc-full.md`. Do not let shorthand examples in this playbook override that standard.

Use this file when writing, repairing, or reviewing GT multiple-choice questions. The local style is short and decisive: one mathematical idea, four plausible answers, and a solution that explains the deciding step without turning into a full essay.

## Core Pattern

GT MC questions usually target one of these objects:

- monotonicity from a derivative sign or variation table
- domain, asymptote, extrema, or value read from a graph/table
- one integral computed by linearity or by a simple antiderivative
- one applied optimization quantity such as the best dimension, minimum material, maximum profit, or minimum cost
- one derivative/primitive/log/exponential step with a clean numeric answer

Before composing options, write the exact answer symbolically and decide which common mistake should produce each distractor.

## Algorithm

1. Identify the hidden contract: domain, interval, unit, and whether the question asks for a variable, an extremal value, or a conclusion.
2. Compute from one canonical relation.
3. Build three distractors from nearby mistakes.
4. Check every displayed option remains distinct after formatting and rounding.
5. In the solution, show only the decisive chain: `Ta co`, formula, substitution or table reading, then `Vay`.

## Reliable Formula Targets

- For a rational function monotonicity item, never say the function is monotone on all `D` when the domain is split. Use intervals separated by excluded points.
- For a table item, read derivative signs on each interval, not across a discontinuity or vertical asymptote.
- For integral linearity, expand as `I=a int x dx + b int f(x) dx + c int g(x) dx`; compute `int_a^b x dx=(b^2-a^2)/2`.
- For open-box or material problems, write the constraint first, substitute into one-variable area/cost, then optimize on the practical domain.
- For log/exponential questions, isolate the positive ratio before taking logs; keep base and sign consistent.

## Distractor Design

Good distractors should feel like student errors:

- using `b-a` instead of `(b^2-a^2)/2` for `int x dx`
- flipping the sign of one known integral term
- forgetting that monotonicity is on each interval of the domain
- choosing the critical point value instead of the requested variable
- missing the unit conversion from hours to minutes, `cm^3` to liters, or nghin dong to dong
- taking the endpoint value without checking the interior extremum

Avoid absurd options. In applied contexts, wrong answers should still have realistic units and magnitude.

## Code Guardrails

Use a `while True` loop when random values can collapse options or break the model.

- Ensure denominators and log arguments are nonzero/positive.
- Ensure the extremum exists in the stated domain or interval.
- Ensure derivative roots used in the solution are real and pedagogically clean.
- Ensure all MC options are distinct after `tinh_latex`, `lam_tron`, or fraction formatting.
- Keep numeric computation variables separate from display strings.
- If the answer may be exact, do not force `\approx`; if it is rounded, state the rounding rule.

## Presentation Style

MC solutions should be compact:

```latex
Ta co: ...
Ma ...
Suy ra ...
Vay ...
```

Use a variation table helper such as `bbtb2TCT(...)` or `bbtb2CTC(...)` only when it helps justify the extremum. For a simple integral-property item, a table is unnecessary; linearity plus substitution is enough.
