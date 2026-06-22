# Question Types And Templates

## Purpose

Use this file when deciding the question structure or writing a generator with the local `thuvien` helpers.

## Shared conventions

Start from the local import pattern when it matches the bank:

```python
import os
import sys
from pathlib import Path
import inspect
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pythonfile.thuvien import *
```

General rules:

- obey [trinh-bay-cong-thuc-full.md](./trinh-bay-cong-thuc-full.md) for every mathematical symbol, number, unit, interval, system, aligned formula, and list environment
- keep one function per question template
- derive `ID_cauhoi` from `inspect.currentframe().f_code.co_name` unless the project already has another convention
- build `debai_text` first, then call `generate_latex_question(...)`
- keep the same core variables across statement, answer, solution, and figure
- return exactly one formatter call per question function
- accept `for_moodle=False` in public question functions

## Multiple choice

Structure:

- exactly one correct option marked with `\True ` before shuffling
- four options parallel in style and units
- distractors that remain wrong after rounding and formatting
- solution text that does not refer to fixed option labels A, B, C, or D

Skeleton:

```python
def IDCauHoiI(for_moodle=False):
    ID_cauhoi = inspect.currentframe().f_code.co_name
    debai_text = f"Dien noi dung de bai vao day"
    debai = generate_latex_question(ID_cauhoi, debai_text, image1_name=None)

    PA = [f"\\True ", f"", f"", f""]
    random.shuffle(PA)

    loigiai = f"Loi giai se duoc viet o day"
    return format_output_MCquestion(debai, PA, loigiai, for_moodle=for_moodle)
```

## True/false

Structure:

- one shared stem
- exactly four statements
- four true candidates and four matched false variants
- true and false variants similar in length, tone, notation, and unit
- `LGtrue` explanations in the same order as the statements
- use the local `format_output_TFquestion(...)` template for the final assembly; fill only `PAtrue`, `PAfalse`, `LGtrue`, and `debai`
- do not hand-build `\choiceTFt`, `itemchoice`, QC display, or true/false labels unless the user explicitly asks for behavior the helper cannot express
- if a false variant tempts a custom false solution, first check whether the normal `LGtrue` explanation plus helper label is acceptable for this bank; preserve the template unless the user requests custom false-solution handling

Skeleton:

```python
def IDCauHoiII(QC=0, for_moodle=False):
    ID_cauhoi = inspect.currentframe().f_code.co_name
    debai_text = f"Dien noi dung de bai vao day"
    debai = generate_latex_question(ID_cauhoi, debai_text, image1_name=None)

    PAtrue = [f"\\True ", f"\\True ", f"\\True ", f"\\True "]
    PAfalse = [f"", f"", f"", f""]
    LGtrue = [f"Giai thich 1", f"Giai thich 2", f"Giai thich 3", f"Giai thich 4"]

    return format_output_TFquestion(
        PAtrue=PAtrue,
        PAfalse=PAfalse,
        LGtrue=LGtrue,
        debai=debai,
        QC=QC,
        for_moodle=for_moodle,
    )
```

## Short answer

Structure:

- one final answer
- exact expected answer type: integer, decimal, fraction, radical, or symbolic form
- explicit unit and rounding precision
- `ketqua` matching the displayed final answer in the solution

Skeleton:

```python
def IDCauHoiIII(for_moodle=False):
    ID_cauhoi = inspect.currentframe().f_code.co_name
    debai_text = f"Dien noi dung de bai vao day"
    debai = generate_latex_question(ID_cauhoi, debai_text, image1_name=None)

    loigiai = f"Nhap noi dung loi giai"
    ketqua = 0

    return format_output_SAquestion(debai, loigiai, ketqua, for_moodle=for_moodle)
```

## Common families

- Optimization and economics: derive the practical domain before sign analysis and verify feasibility constraints.
- Geometry or integral with figure: synchronize figure labels, integral bounds, variables, units, and solution text.
- Probability and combinatorics: write the general count or probability first, identify hard upper bounds, then justify the optimum or distribution.

## Bank assembly

Do not append `None` to the question bank. Call the real question function:

```python
nganhang = []
socau = 10

for i in range(socau):
    cauhoi = IDCauHoiI(for_moodle=False)
    cauhoi += "\n"
    nganhang.append(cauhoi)
```
