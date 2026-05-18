#!/usr/bin/env python3
"""Validate the Awesome AI for CAD catalog metadata."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
PAPERS_DIR = ROOT / "research" / "papers"
SURVEY_FILES = [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "CONTRIBUTING.md",
]

EXPECTED = {
    "readme_entries": 723,
    "jsonl_dedup_records": 638,
    "jsonl_2024_2026_records": 496,
}

BANNED_PATTERNS = {
    r"700\+ papers": "Use a defined denominator instead of '700+ papers'.",
    r"over 700 papers": "Use a defined denominator instead of 'over 700 papers'.",
    r"approximately 60%": "Do not publish an unreproducible recent-paper percentage.",
    r"projected 230\+": "Do not publish projected corpus counts.",
    r"research/paper/": "The public Awesome repository must not link to manuscript files.",
    r"full-survey": "The public Awesome repository must not link to manuscript files.",
    r"BibTeX entries": "Do not expose submitted-paper bibliography counts in the Awesome repository.",
    r"TPAMI survey": "Keep survey-paper positioning out of the Awesome repository until the paper is ready.",
    r"Papers-700": "Badge must use a defined denominator.",
}


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def count_readme_entries() -> int:
    text = README.read_text(encoding="utf-8")
    entry_pattern = re.compile(r"^- \*\*.+\*\*")
    return sum(1 for line in text.splitlines() if entry_pattern.match(line))


def read_jsonl_registry(failures: list[str]) -> tuple[int, Counter[int]]:
    seen: set[str] = set()
    years: Counter[int] = Counter()
    total = 0

    for path in sorted(PAPERS_DIR.glob("*.jsonl")):
        with path.open(encoding="utf-8") as handle:
            for line_no, line in enumerate(handle, start=1):
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as exc:
                    fail(f"{path}:{line_no}: invalid JSON: {exc}", failures)
                    continue

                title = str(record.get("title", "")).strip()
                if not title:
                    fail(f"{path}:{line_no}: missing title", failures)
                    continue

                key = str(record.get("arxiv_id") or title).strip()
                if key in seen:
                    continue
                seen.add(key)
                total += 1

                try:
                    year = int(record.get("year"))
                except (TypeError, ValueError):
                    fail(f"{path}:{line_no}: invalid year for {title!r}", failures)
                    continue
                years[year] += 1

    return total, years


def check_expected(name: str, actual: int, failures: list[str]) -> None:
    expected = EXPECTED[name]
    if actual != expected:
        fail(f"{name}: expected {expected}, got {actual}", failures)


def check_banned_patterns(failures: list[str]) -> None:
    for path in SURVEY_FILES:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for pattern, reason in BANNED_PATTERNS.items():
            if re.search(pattern, text, flags=re.IGNORECASE):
                fail(f"{rel}: banned pattern {pattern!r}. {reason}", failures)


def main() -> int:
    failures: list[str] = []

    readme_entries = count_readme_entries()
    registry_total, years = read_jsonl_registry(failures)
    recent_total = sum(years[y] for y in (2024, 2025, 2026))

    check_expected("readme_entries", readme_entries, failures)
    check_expected("jsonl_dedup_records", registry_total, failures)
    check_expected("jsonl_2024_2026_records", recent_total, failures)
    check_banned_patterns(failures)

    print("Catalog validation summary")
    print(f"- README catalog entries: {readme_entries}")
    print(f"- Deduplicated JSONL records: {registry_total}")
    print(f"- JSONL records dated 2024-2026: {recent_total}")
    print(
        "- JSONL records by year 2018-2026: "
        + ", ".join(f"{year}={years[year]}" for year in range(2018, 2027))
    )

    if failures:
        print("\nFailures:", file=sys.stderr)
        for item in failures:
            print(f"- {item}", file=sys.stderr)
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
