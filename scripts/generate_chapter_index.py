#!/usr/bin/env python3
"""
Generate per-chapter index markdown files from the book's .qmd sources.

For each chapter, produces one file under docs/chapters/:
    docs/chapters/01-introduction.md
    docs/chapters/02-session.md
    ...

Each index file lists every Example with:
  - Example number and title
  - Difficulty level (Beginner / Intermediate / Advanced)
  - Functions covered
  - A one-line excerpt from the Problem Statement

Output is PURE ASCII - no em-dashes, no smart quotes, no emoji. This avoids
UTF-8-vs-Windows-1252 encoding mojibake when files pass through PowerShell
on Windows machines.

Usage from the companion repo root:
    python scripts/generate_chapter_index.py <path-to-book-folder>
"""
import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CHAPTERS_DIR = REPO_ROOT / "docs" / "chapters"


def to_ascii(text):
    """Strip or replace all non-ASCII characters so the output is pure ASCII."""
    if not text:
        return text
    # Common Unicode punctuation to ASCII
    replacements = {
        "—": "-",   # em dash
        "–": "-",   # en dash
        "‘": "'",   # smart single open
        "’": "'",   # smart single close
        "“": '"',   # smart double open
        "”": '"',   # smart double close
        "…": "...", # ellipsis
        "·": ".",   # middle dot
        " ": " ",   # non-breaking space
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    # Strip anything else non-ASCII (emoji, accented letters, etc.)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if ord(c) < 128)
    return text


def extract_examples(text):
    """Find every '### Example N' and parse title + metadata + problem."""
    pattern = re.compile(
        r"^### Example\s+(\d+)\s*[-]+\s*(.+?)\s*$"
        r"(.+?)(?=^### Example|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    examples = []
    for m in pattern.finditer(to_ascii(text)):
        num = int(m.group(1))
        title = m.group(2).strip()
        body = m.group(3)

        level_m = re.search(r"\*\*Level:\*\*\s*(\w+)", body)
        funcs_m = re.search(r"\*\*Functions:\*\*\s*(.+?)$", body, re.MULTILINE)
        problem_m = re.search(
            r"\*\*Problem Statement\*\*\s*\n\n(.+?)(?=\n\n\*\*|\Z)",
            body, re.DOTALL,
        )
        examples.append({
            "num": num,
            "title": title.strip(),
            "level": level_m.group(1) if level_m else "",
            "functions": funcs_m.group(1).strip() if funcs_m else "",
            "problem": problem_m.group(1).strip().split("\n")[0] if problem_m else "",
        })
    return examples


def build_index_for_chapter(qmd_path):
    text = qmd_path.read_text(encoding="utf-8")
    text = to_ascii(text)

    title_m = re.search(r"^#\s+(.+?)(?:\s*\{[^}]*\})?\s*$", text, re.MULTILINE)
    chapter_title = title_m.group(1) if title_m else qmd_path.stem
    chapter_num_m = re.match(r"^(\d+)", qmd_path.name)
    chapter_num = int(chapter_num_m.group(1)) if chapter_num_m else 0

    examples = extract_examples(text)

    if not examples:
        first, last = 0, 0
    else:
        first, last = examples[0]["num"], examples[-1]["num"]

    levels = {}
    for ex in examples:
        lvl = ex["level"] or "Unspecified"
        levels[lvl] = levels.get(lvl, 0) + 1

    lines = []
    lines.append(f"# Chapter {chapter_num}: {chapter_title}")
    lines.append("")
    lines.append(f"**{len(examples)} examples** ({first}-{last})")
    lines.append("")
    if levels:
        mix = " . ".join(f"{v} {k}" for k, v in sorted(levels.items()))
        lines.append(f"Difficulty mix: {mix}")
        lines.append("")
    lines.append(
        f"[Open the practice notebook](../../notebooks/{qmd_path.stem}.ipynb) . "
        f"[Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)"
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Examples")
    lines.append("")

    for ex in examples:
        lines.append(f"### Example {ex['num']}: {ex['title']}")
        meta_parts = []
        if ex["level"]:
            meta_parts.append(f"*{ex['level']}*")
        if ex["functions"]:
            meta_parts.append(f"`{ex['functions']}`")
        if meta_parts:
            lines.append(" . ".join(meta_parts))
        if ex["problem"]:
            lines.append("")
            lines.append(ex["problem"])
        lines.append("")

    return chapter_num, chapter_title, lines, len(examples)


def main(book_dir):
    book_dir = Path(book_dir)
    if not book_dir.exists():
        print(f"ERROR: book directory not found: {book_dir}", file=sys.stderr)
        return 1
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)

    stats = []
    for qmd in sorted(book_dir.glob("[0-9]*-*.qmd")):
        chapter_num, title, lines, ex_count = build_index_for_chapter(qmd)
        out_path = CHAPTERS_DIR / (qmd.stem + ".md")
        content = "\n".join(lines)
        # Write as pure ASCII - no BOM, no encoding ambiguity
        out_path.write_bytes(content.encode("ascii", errors="ignore"))
        stats.append((chapter_num, title, ex_count, out_path.name))
        print(f"  Ch {chapter_num:2d}: {title:40s}  ({ex_count} examples)  -> {out_path.name}")

    total = sum(s[2] for s in stats)
    print(f"\nGenerated {len(stats)} chapter indexes with {total} total examples.")
    print(f"Output: {CHAPTERS_DIR}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
