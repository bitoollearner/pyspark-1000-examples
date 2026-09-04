#!/usr/bin/env python3
"""
Generate the per-chapter index files at docs/chapters/NN-slug.md.

For each chapter, produces a markdown file listing every example with:
  - Example number and title
  - Level (Beginner / Intermediate / Advanced)
  - Functions covered
  - Problem statement (one line)

These are the "rich indexes" that help potential readers discover what's in
each chapter without giving away the full teaching content.

Usage from repo root:
    python scripts/generate_chapter_index.py <path-to-book-folder>
"""
import re
import sys
from pathlib import Path
from collections import Counter

REPO_ROOT = Path(__file__).parent.parent
CHAPTERS_DIR = REPO_ROOT / "docs" / "chapters"


def extract_examples(text):
    """Same regex-parse as generate_notebooks.py, kept in sync."""
    pattern = re.compile(
        r"^### Example\s+(\d+)\s*[—–\-]+\s*(.+?)\s*$"
        r"(.+?)(?=^### Example|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    out = []
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
        out.append({
            "num": num,
            "title": title,
            "level": level_m.group(1) if level_m else "",
            "functions": funcs_m.group(1).strip() if funcs_m else "",
            "problem": problem_m.group(1).strip() if problem_m else "",
        })
    return out


def build_chapter_index(qmd_path):
    text = qmd_path.read_text(encoding="utf-8")
    title_m = re.search(r"^#\s+(.+?)(?:\s*\{[^}]*\})?\s*$", text, re.MULTILINE)
    chapter_title = title_m.group(1) if title_m else qmd_path.stem
    chapter_num_m = re.match(r"^(\d+)", qmd_path.name)
    chapter_num = int(chapter_num_m.group(1)) if chapter_num_m else 0

    examples = extract_examples(text)
    if not examples:
        return None

    first, last = examples[0]["num"], examples[-1]["num"]

    # Count levels for a summary line
    level_counts = Counter(ex["level"] for ex in examples if ex["level"])

    lines = []
    lines.append(f"# Chapter {chapter_num}: {chapter_title}")
    lines.append("")
    lines.append(f"**{len(examples)} examples** ({first}–{last})")
    lines.append("")

    if level_counts:
        parts = []
        for lvl in ("Beginner", "Intermediate", "Advanced"):
            n = level_counts.get(lvl, 0)
            if n:
                parts.append(f"{n} {lvl}")
        lines.append(f"Difficulty mix: {' · '.join(parts)}")
        lines.append("")

    lines.append(f"[📔 Open the notebook](../../notebooks/{qmd_path.stem}.ipynb) · "
                 f"[📖 Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Examples")
    lines.append("")

    for ex in examples:
        # Trim problem to one line, ~120 chars
        problem_short = ex["problem"].replace("\n", " ").strip()
        if len(problem_short) > 120:
            problem_short = problem_short[:117] + "..."

        lines.append(f"### Example {ex['num']}: {ex['title']}")
        meta_parts = []
        if ex["level"]:
            meta_parts.append(f"*{ex['level']}*")
        if ex["functions"]:
            # Wrap function names in backticks
            fns = ", ".join(f"`{f.strip()}`" for f in ex["functions"].split(","))
            meta_parts.append(fns)
        if meta_parts:
            lines.append(" · ".join(meta_parts))
        if problem_short:
            lines.append("")
            lines.append(problem_short)
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"← [Back to main index](../../README.md)")
    lines.append("")

    return chapter_num, chapter_title, len(examples), "\n".join(lines)


def main(book_dir):
    book_dir = Path(book_dir)
    if not book_dir.exists():
        print(f"ERROR: book directory not found: {book_dir}", file=sys.stderr)
        return 1
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)

    stats = []
    for qmd in sorted(book_dir.glob("[0-9]*-*.qmd")):
        result = build_chapter_index(qmd)
        if not result:
            continue
        chapter_num, title, ex_count, content = result
        out_path = CHAPTERS_DIR / (qmd.stem + ".md")
        out_path.write_text(content, encoding="utf-8")
        stats.append((chapter_num, title, ex_count, out_path.name))
        print(f"  Ch {chapter_num:2d}: {title:40s}  ({ex_count} examples)  -> {out_path.name}")

    print(f"\nGenerated {len(stats)} chapter index files at {CHAPTERS_DIR}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
