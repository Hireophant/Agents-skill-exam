# QC Workflow

Use this workflow after a generator has produced 100 randomized `.tex` samples or an equivalent full exam bundle.

## Inputs

Collect these before reviewing:

- Python source file for the question/generator.
- Generated `.tex` from 100 random samples.
- Compile log and PDF if available.
- Any answer key or solution blocks emitted by the generator.
- The old/sample file from `old_file_new/` if the question has a same-code or same-type reference.

## Required Loop

1. Run or confirm 100 random generations.
2. Export to `.tex`.
3. Run static triage on `.tex`.
4. Read the generated `.tex` around every question instance.
5. Recompute answers from the statement quantities, not from the solution.
6. Compare the recomputation with the answer key and worked solution.
7. Check the mandatory notation standard.
8. Compile or inspect compile logs/PDF when possible.
9. Patch the Python generator for every real defect.
10. Regenerate 100 samples and repeat.

The loop stops only when:

- no static `.tex` warnings remain except explicitly justified false positives
- no compile-blocking issue remains
- all answer keys and solutions match the generated statements
- all randomized values stay in valid and realistic ranges
- formatting follows `trinh-bay-cong-thuc-full.md`

## Fixing Rules

- Patch the source generator, not only generated `.tex`.
- Keep user-approved style and solution rhythm.
- If a fix changes a formula, update statement, answer, solution, and figure labels together.
- If a false TF variant changes a threshold/value/conclusion, verify the explanation still matches.
- If a random guard is missing, add a `while True` rejection rule rather than hoping random values are good.

## Final Report

Use concise findings-first reporting:

```text
Tong quan: ...
Phat hien loi:
- Vi tri: ...
  Trang thai: CAN_SUA
  Ly do: ...
  Cach sua: ...
  Da rerun 100 mau: Co/Khong
Goc nhin phan bien: ...
Ket luan QC: PASS/CHUA PASS
```
