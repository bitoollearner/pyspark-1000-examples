# PySpark: 1,000 Examples — Practice Environment

A ready-to-practice Spark + Jupyter environment for the book
**[PySpark: 1,000 Examples](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)**.

## What this image gives you

- Spark 3.5.3, Delta Lake 3.2.0, Python 3.11, OpenJDK 17 — identical to the book
- JupyterLab 4.2.5, auto-opens to the `practice/` folder
- Pre-generated seeded datasets (customers, products, orders, etc.)
- 22 pre-created chapter folders, each with a starter notebook

## What this image does NOT contain

- The example code or solutions — you type those yourself from the book
- Any text, explanation, or content from the book — read those on Kindle

The point is to practice: open the book, read Example N, type the Solution
code into your Jupyter notebook, run it, compare your output to the book's.
That's how PySpark sticks.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
- 4 GB free RAM, 8 GB free disk

## Quick start

**Mac / Linux:**

```bash
mkdir -p practice
docker run --rm \
  -p 8888:8888 -p 4040:4040 \
  -v $(pwd)/practice:/workspace/practice \
  bitoollearner/pyspark1000-practice:1.0
```

**Windows PowerShell:**

```powershell
mkdir practice -Force
docker run --rm `
  -p 8888:8888 -p 4040:4040 `
  -v ${PWD}/practice:/workspace/practice `
  bitoollearner/pyspark1000-practice:1.0
```

Open http://localhost:8888/lab in your browser. JupyterLab appears, already
showing the 22 chapter folders.

Pick a chapter folder → open `scratch.ipynb` → run the Chapter setup cell →
start typing examples from the book.

## Workflow

1. Open the book on Kindle, pick an example (say Chapter 10, Example 388)
2. Open `chapter-10-aggregations/scratch.ipynb` in JupyterLab
3. Type the Solution code from the book into a new cell
4. Shift+Enter — compare your output to the book's Output section
5. Read the book's Explanation, Common Mistake, Recommendation, Pattern Insight

## Persisting your work

The `-v $(pwd)/practice:/workspace/practice` flag mounts a `practice/` folder
from your laptop into the container. Everything you type and save in Jupyter
persists on your laptop, even if the container is removed.

Without that flag, your notebooks live inside the container and vanish when
the container stops. Always use the volume mount unless you want a disposable
scratch environment.

## Datasets

The book's examples reference these paths inside the container:

```python
spark.read.csv("/workspace/datasets/customers.csv", header=True)
spark.read.json("/workspace/datasets/events.json")
spark.read.parquet("/workspace/datasets/sales.parquet")
```

All datasets are pre-generated and ready — no setup needed.

## Stopping

Press Ctrl+C in the terminal running the image. The container stops; your
`practice/` folder on the host stays intact.

To fully remove the image:

```bash
docker rmi bitoollearner/pyspark1000-practice:1.0
```

## License

MIT. Image contents include third-party software under their own licenses.
Book content (narrative, explanations, example solutions) is copyright
© 2026 Bi Learner — available on [Amazon Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN).
