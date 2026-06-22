#!/usr/bin/env python3
"""Static QC triage for generated LaTeX exam files.

This script does not prove the math. It catches common emitted-tex defects so
the QC pass can focus attention before doing the human mathematical review.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Issue:
    severity: str
    path: Path
    line: int
    rule: str
    message: str


BEGIN_RE = re.compile(r"\\begin\{([^}]+)\}")
END_RE = re.compile(r"\\end\{([^}]+)\}")


LINE_RULES: list[tuple[str, str, re.Pattern[str], str]] = [
    ("ERROR", "placeholder", re.compile(r"\b(None|nan|NaN|inf|Infinity)\b"), "Raw placeholder or non-finite value appears in output."),
    ("WARN", "degree", re.compile(r"90\^(?:0|o)\b"), "Use ^\\circ for degree notation."),
    ("WARN", "parallel", re.compile(r"//"), "Use \\parallel instead of //."),
    ("WARN", "setminus", re.compile(r"\\backslash"), "Use \\setminus for set difference."),
    ("WARN", "raw_dx", re.compile(r"(?<![A-Za-z\\])dx(?![A-Za-z])"), "Use \\mathrm{d}x for differentials."),
    ("WARN", "probability", re.compile(r"(?<!\\mathrm\{)P\("), "Use \\mathrm{P}(A) for probability notation."),
    ("WARN", "combination", re.compile(r"(?<!\\mathrm\{)[CA]_\{?\\?[A-Za-z0-9]+"), "Use \\mathrm{C}_n^k or \\mathrm{A}_n^k for combinations/arrangements."),
    ("WARN", "enumerate_option", re.compile(r"\\begin\{enumerate\}\["), "Default enumerate has no optional label unless explicitly required."),
    ("WARN", "leading_hfill", re.compile(r"^\s*\\hfill\b"), "Do not start an exercise/solution with \\hfill."),
    ("WARN", "todo_debug", re.compile(r"TODO|FIXME|DEBUG|Nhap noi dung|Dien noi dung", re.IGNORECASE), "Debug/template text remains."),
]


def count_unescaped_dollars(text: str) -> int:
    count = 0
    escaped = False
    for ch in text:
        if ch == "\\" and not escaped:
            escaped = True
            continue
        if ch == "$" and not escaped:
            count += 1
        escaped = False
    return count


def brace_delta(line: str) -> int:
    delta = 0
    escaped = False
    for ch in line:
        if ch == "\\" and not escaped:
            escaped = True
            continue
        if not escaped:
            if ch == "{":
                delta += 1
            elif ch == "}":
                delta -= 1
        escaped = False
    return delta


def scan_file(path: Path) -> list[Issue]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    issues: list[Issue] = []

    if count_unescaped_dollars(text) % 2:
        issues.append(Issue("ERROR", path, 1, "dollar_balance", "Odd number of unescaped dollar signs."))

    brace_balance = 0
    env_stack: list[tuple[str, int]] = []

    for idx, line in enumerate(lines, start=1):
        brace_balance += brace_delta(line)
        if brace_balance < 0:
            issues.append(Issue("ERROR", path, idx, "brace_balance", "Closing brace appears before matching opening brace."))
            brace_balance = 0

        for env in BEGIN_RE.findall(line):
            env_stack.append((env, idx))
        for env in END_RE.findall(line):
            if not env_stack:
                issues.append(Issue("ERROR", path, idx, "environment_balance", f"\\end{{{env}}} has no matching begin."))
            else:
                opened, opened_line = env_stack.pop()
                if opened != env:
                    issues.append(
                        Issue(
                            "ERROR",
                            path,
                            idx,
                            "environment_balance",
                            f"\\end{{{env}}} closes \\begin{{{opened}}} from line {opened_line}.",
                        )
                    )

        for severity, rule, pattern, message in LINE_RULES:
            if pattern.search(line):
                issues.append(Issue(severity, path, idx, rule, message))

        if re.search(r"\$\d+,\d+\$", line):
            issues.append(Issue("WARN", path, idx, "decimal_comma", "Use decimal comma as {,} inside math mode, e.g. $1{,}23$."))

        if "\\begin{tikzpicture}" in line:
            # A lightweight marker; detailed TikZ inspection remains manual.
            pass

    if brace_balance:
        issues.append(Issue("ERROR", path, len(lines), "brace_balance", f"Unbalanced braces, final delta={brace_balance}."))
    for env, opened_line in env_stack:
        issues.append(Issue("ERROR", path, opened_line, "environment_balance", f"\\begin{{{env}}} has no matching end."))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Static QC triage for generated LaTeX files.")
    parser.add_argument("paths", nargs="+", help="Generated .tex files or directories to scan.")
    args = parser.parse_args()

    files: list[Path] = []
    for raw in args.paths:
        path = Path(raw)
        if path.is_dir():
            files.extend(sorted(path.rglob("*.tex")))
        else:
            files.append(path)

    all_issues: list[Issue] = []
    for path in files:
        if not path.exists():
            all_issues.append(Issue("ERROR", path, 0, "missing_file", "File does not exist."))
            continue
        all_issues.extend(scan_file(path))

    if not all_issues:
        print("QC_STATIC: PASS - no static LaTeX issues found.")
        return 0

    error_count = sum(1 for item in all_issues if item.severity == "ERROR")
    warn_count = sum(1 for item in all_issues if item.severity == "WARN")
    print(f"QC_STATIC: FOUND {error_count} error(s), {warn_count} warning(s)")
    for item in all_issues:
        loc = f"{item.path}:{item.line}" if item.line else str(item.path)
        print(f"- [{item.severity}] {loc} {item.rule}: {item.message}")

    return 2 if error_count else 1


if __name__ == "__main__":
    raise SystemExit(main())
