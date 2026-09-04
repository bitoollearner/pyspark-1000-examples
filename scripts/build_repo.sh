#!/usr/bin/env bash
# Convenience: regenerate notebooks + chapter indexes in one shot.
# Usage: ./scripts/build_repo.sh /path/to/book/folder
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: $0 <path-to-book-folder>"
  echo "  Book folder is the one containing 01-introduction.qmd etc."
  exit 1
fi

BOOK_DIR="$1"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo ">> Generating notebooks..."
python "$REPO_ROOT/scripts/generate_notebooks.py" "$BOOK_DIR"

echo ""
echo ">> Generating chapter indexes..."
python "$REPO_ROOT/scripts/generate_chapter_index.py" "$BOOK_DIR"

echo ""
echo "Done. Review the generated files, then:"
echo "  git status"
echo "  git add ."
echo "  git commit -m 'Regenerate notebooks and indexes'"
