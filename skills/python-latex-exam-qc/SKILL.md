---
name: python-latex-exam-qc
description: Quality-control workflow for generated Python-LaTeX Vietnamese high-school math exam questions. Use after Codex has written or repaired a generator and produced randomized `.tex` output, especially the required 100-random-sample check, to audit math correctness, answer keys, TF/MC/SA structure, LaTeX/TikZ rendering, notation standards, practical realism, and equivalence across generated variants; keep fixing the source and rerunning until the QC report is clean.
---

# Python Latex Exam QC

## Role

Use this skill only after a question generator or exam set has been written, repaired, or randomized into `.tex` output. The job is not to admire the solution; the job is to find every defect that could break the exam, mislead a student, or violate the user's house style, then fix the source and rerun the checks until no blocking defect remains.

Pair this skill with `python-latex-exam-master` and the relevant domain solver when a defect requires changing the generator. Pair with `python-latex-exam-tikz-drawing` when the defect is a figure, graph, or TikZ layout issue.

## Required References

Before doing QC, read the relevant references below. Do not rely on this `SKILL.md` alone.

- Read [prompt-phan-bien.md](./references/prompt-phan-bien.md) for the user's original QC role and reporting contract. The source DOCX is preserved as [PROMPT_PHAN_BIEN.docx](./references/PROMPT_PHAN_BIEN.docx).
- Read [qc-workflow.md](./references/qc-workflow.md) for the required loop: randomize 100 samples, export `.tex`, inspect, fix, rerun.
- Read [qc-checklist.md](./references/qc-checklist.md) for the defect classes and pass/fail criteria.
- Read `../python-latex-exam-master/references/trinh-bay-cong-thuc-full.md` for mandatory formula/notation standards.
- Read `../python-latex-exam-master/references/latex-tikz-output-checklist.md` for LaTeX/TikZ and generated `.tex` checks.

## QC Loop

1. Identify the source generator file, the generated `.tex`, and any compile log/PDF if available.
2. Confirm the user or previous step has run 100 random generations. If not, run the project's existing random/export workflow or explain that QC cannot be complete without it.
3. Run static `.tex` triage:

```bash
python .agents/skills/python-latex-exam-qc/scripts/qc_tex_static.py path/to/output.tex
```

4. Inspect the generated `.tex` directly around every warning and around each changed question block.
5. Review every question instance, not just one sample. For TF, read the worked solution before judging the statements.
6. Check math, answer, units, rounding, wording, LaTeX, TikZ, and practical realism.
7. If any blocking defect exists, patch the source generator, regenerate 100 samples, and repeat QC.
8. Stop only when the source, generated `.tex`, answer key, and solution are all consistent and no blocking defect remains.

## Reporting Contract

Report findings first. Use these statuses:

- `OK`: correct and usable.
- `CAN_CHINH_NHE`: minor wording, formatting, or style issue.
- `CAN_SUA`: mathematical, answer-key, logic, or LaTeX issue that must be fixed.
- `KHONG_NEN_DUNG`: flawed structure, ambiguous task, invalid data model, or unreliable item.

For each defect, include the location, why it is wrong, the fix made or proposed, and whether the generator was rerun after the fix.

## Non-Negotiables

- Do not stop at "looks fine" after one generated sample. The standard check is 100 random samples.
- Do not fix only the generated `.tex` if the real bug is in the Python generator.
- Do not skip any generated question instance.
- Do not merge comments across variants or code paths when they differ.
- Do not trust the answer key without recomputing from the statement quantities.
- Do not accept LaTeX that compiles but violates the user's mandatory notation standard.
- Do not mark QC complete while any `CAN_SUA` or `KHONG_NEN_DUNG` defect remains.
