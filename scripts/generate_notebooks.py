#!/usr/bin/env python3
"""
Generate the 22 chapter notebooks from the book's .qmd source files.

For each chapter, produces one .ipynb containing:
  - Chapter title cell
  - Chapter setup cell (imports, spark session, etc.)
  - For each example:
      - Markdown cell:  "## Example N: Title" + level, functions, problem
      - Code cell:      the Solution code

The book-only content (explanations, common mistakes, recommendations,
pattern insights) is intentionally NOT extracted — that stays in the book.

Usage from repo root:
    python scripts/generate_notebooks.py <path-to-book-folder>

Example:
    python scripts/generate_notebooks.py C:\\Users\\Caption\\PycharmProjects\\pyspark-1000-examples\\book
"""
import re
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"


def make_notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.11"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def _split_source(text):
    """Convert a source string to Jupyter's list-of-lines-with-newlines format."""
    if not text:
        return [""]
    lines = text.splitlines(keepends=True)
    # Jupyter convention: last line should not have trailing newline
    if lines and lines[-1].endswith("\n"):
        lines[-1] = lines[-1].rstrip("\n")
    return lines


def md_cell(text):
    return {"cell_type": "markdown", "metadata": {}, "source": _split_source(text)}


def code_cell(text):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": _split_source(text),
    }


def extract_chapter_setup(text):
    """The chapter has a '## Chapter setup' section with imports/session code."""
    m = re.search(
        r"^## Chapter setup\s*\n(?:.*?\n)?```python\n(.+?)\n```",
        text, re.MULTILINE | re.DOTALL,
    )
    return m.group(1).strip() if m else ""


def extract_examples(text):
    """Find every '### Example N — Title' and parse the parts we need."""
    pattern = re.compile(
        r"^### Example\s+(\d+)\s*[—–\-]+\s*(.+?)\s*$"
        r"(.+?)(?=^### Example|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    examples = []
    for m in pattern.finditer(text):
        num = int(m.group(1))
        title = m.group(2).strip()
        body = m.group(3)

        level_m = re.search(r"\*\*Level:\*\*\s*(\w+)", body)
        funcs_m = re.search(r"\*\*Functions:\*\*\s*(.+?)$", body, re.MULTILINE)
        problem_m = re.search(
            r"\*\*Problem Statement\*\*\s*\n\n(.+?)(?=\n\n\*\*|\Z)",
            body, re.DOTALL,
        )
        solution_m = re.search(
            r"\*\*Solution\*\*\s*\n\n```python\n(.+?)\n```",
            body, re.DOTALL,
        )
        examples.append({
            "num": num,
            "title": title,
            "level": level_m.group(1) if level_m else "",
            "functions": funcs_m.group(1).strip() if funcs_m else "",
            "problem": problem_m.group(1).strip() if problem_m else "",
            "solution": solution_m.group(1).strip() if solution_m else "",
        })
    return examples


def build_notebook_for_chapter(qmd_path):
    text = qmd_path.read_text(encoding="utf-8")

    title_m = re.search(r"^#\s+(.+?)(?:\s*\{[^}]*\})?\s*$", text, re.MULTILINE)
    chapter_title = title_m.group(1) if title_m else qmd_path.stem
    chapter_num_m = re.match(r"^(\d+)", qmd_path.name)
    chapter_num = int(chapter_num_m.group(1)) if chapter_num_m else 0

    setup_code = extract_chapter_setup(text)
    examples = extract_examples(text)

    if not examples:
        first, last = 0, 0
    else:
        first, last = examples[0]["num"], examples[-1]["num"]

    cells = []
    intro = (
        f"# Chapter {chapter_num}: {chapter_title}\n\n"
        f"Companion notebook for **PySpark: 1,000 Examples**.\n\n"
        f"This notebook contains **{len(examples)} runnable examples** "
        f"({first}–{last}).\n\n"
        f"For the full explanations, common mistakes, best practices, and "
        f"pattern insights for each example, see the book on Amazon Kindle."
    )
    cells.append(md_cell(intro))

    if setup_code:
        cells.append(md_cell(
            "## Chapter setup\n\nRun this once at the top of the notebook."
        ))
        cells.append(code_cell(setup_code))

    for ex in examples:
        header = f"## Example {ex['num']}: {ex['title']}"
        meta_parts = []
        if ex["level"]:
            meta_parts.append(f"**Level:** {ex['level']}")
        if ex["functions"]:
            meta_parts.append(f"**Functions:** {ex['functions']}")
        meta = " · ".join(meta_parts)

        md_parts = [header]
        if meta:
            md_parts.append(meta)
        if ex["problem"]:
            md_parts.append(ex["problem"])
        cells.append(md_cell("\n\n".join(md_parts)))

        if ex["solution"]:
            cells.append(code_cell(ex["solution"]))

    return chapter_num, chapter_title, cells, len(examples)


def main(book_dir):
    book_dir = Path(book_dir)
    if not book_dir.exists():
        print(f"ERROR: book directory not found: {book_dir}", file=sys.stderr)
        return 1
    NOTEBOOKS_DIR.mkdir(exist_ok=True)

    stats = []
    for qmd in sorted(book_dir.glob("[0-9]*-*.qmd")):
        chapter_num, title, cells, ex_count = build_notebook_for_chapter(qmd)
        out_path = NOTEBOOKS_DIR / (qmd.stem + ".ipynb")
        with out_path.open("w", encoding="utf-8") as f:
            json.dump(make_notebook(cells), f, indent=1, ensure_ascii=False)
        stats.append((chapter_num, title, ex_count, out_path.name))
        print(f"  Ch {chapter_num:2d}: {title:40s}  ({ex_count} examples)  -> {out_path.name}")

    total_examples = sum(s[2] for s in stats)
    print(f"\nGenerated {len(stats)} notebooks with {total_examples} total examples.")
    print(f"Output: {NOTEBOOKS_DIR}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
