# Practice workspace

This folder is where you work through the examples from
**PySpark: 1,000 Examples**.

## How to use

1. Open the book on Kindle (or your preferred reader)
2. Pick an example — say, Chapter 10, Example 388
3. In this folder, open `chapter-10-aggregations/scratch.ipynb`
4. Run the "Chapter setup" cell at the top (once per session)
5. Type the example's **Solution** code into a new cell
6. Press Shift+Enter to run
7. Compare your output to the book's **Output** section
8. Read the book's **Explanation**, **Common Mistake**, **Recommendation**,
   and **Pattern Insight** for the full picture

## Why type the code yourself

Reading code is not the same as writing code. The muscle memory of typing
`F.col("x")`, the small typos you catch, the autocomplete suggestions you
explore, the brief moment where you wonder "wait, why does this work?" —
that is where the learning happens.

## Keeping your work

If you ran the container with a volume mount (recommended):

```bash
docker run --rm -p 8888:8888 \
  -v $(pwd)/practice:/workspace/practice \
  bitoollearner/pyspark1000-practice:1.0
```

Everything in this folder persists on your laptop between container restarts.

Without the volume mount, your notebooks live inside the container and
disappear when the container is removed. Mount a volume unless you want
a disposable scratch environment.

## Folder structure

- `chapter-01-introduction/` — scratch space for Chapter 1
- `chapter-02-session/` — Chapter 2
- ...
- `chapter-22-patterns/` — Chapter 22

Each chapter folder has a starter `scratch.ipynb` with the Chapter setup
cell pre-filled. Add more notebooks as you need them — `exercise-388.ipynb`,
`experiments.ipynb`, whatever helps you organize your work.

## Datasets

The datasets the book references are at `/workspace/datasets/` inside the
container (visible as `datasets/` from the Jupyter file browser). Example
paths you'll see in the book:

```python
spark.read.csv("/workspace/datasets/customers.csv", header=True)
spark.read.json("/workspace/datasets/events.json")
spark.read.parquet("/workspace/datasets/sales.parquet")
```

These are regenerated from a fixed random seed, so your data matches the
book's output byte-for-byte.
