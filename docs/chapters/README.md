# Chapter indexes

Each `NN-slug.md` file in this folder is the detailed index for one chapter of
the book. Every example in that chapter is listed with:

- Example number and title
- Difficulty level (Beginner / Intermediate / Advanced)
- PySpark functions covered
- One-line problem statement

**These files are generated** by running (from repo root):

```bash
python scripts/generate_chapter_index.py <path-to-book-folder>
```

Chapter indexes let potential readers quickly see if the book covers what they
need, and they let existing readers navigate straight to the example they want.

The full explanations, common mistakes, best practices, and pattern insights
for each example are in the book itself.
