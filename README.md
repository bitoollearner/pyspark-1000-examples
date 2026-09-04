# PySpark: 1,000 Examples — Companion Code

> Official code companion for the eBook **[PySpark: 1,000 Examples: A Practical Reference for Data Engineers](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)** — available on Amazon Kindle.

This repository contains everything you need to run **every one of the 1,000 examples** covered in the book, in the exact same reference environment they were written and verified against.

The book itself — the narrative, explanations, common mistakes, best practices, and pattern insights that make the examples make sense — is **not included here**. Get it on [Amazon Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN).

---

## What's in this repository

| Folder | What's inside |
|--------|---------------|
| `notebooks/` | **22 Jupyter notebooks**, one per chapter, with all 1,000 examples as runnable code cells |
| `docs/chapters/` | Detailed index of each chapter — every example title, level, and functions covered |
| `docs/function-index.md` | Alphabetical index of every PySpark function used, cross-referenced to example numbers |
| `docs/errata.md` | Corrections found after publication (please report typos via Issues!) |
| `conf/` | Spark configuration files (log4j2, spark-defaults) — the exact tuning the book uses |
| `scripts/` | Utilities: dataset generator, notebook regenerator, environment check |
| `datasets/` | Seeded reference data used across the book (regenerable via `scripts/generate_datasets.py`) |
| `Dockerfile`, `docker-compose.yml`, `requirements.txt` | The **reference environment** — Spark 3.5.3, Delta 3.2.0, pinned Python deps |

---

## Quick start

**Prerequisite:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) and about 4 GB free RAM.

```bash
# 1. Clone
git clone https://github.com/YOUR-USERNAME/pyspark-1000-examples.git
cd pyspark-1000-examples

# 2. Build the container (~5 min first time; caches after)
docker compose build spark

# 3. Generate the seeded datasets (~30 sec)
docker compose run --rm spark python scripts/generate_datasets.py

# 4. Start JupyterLab
docker compose up -d spark
docker compose exec spark jupyter lab --ip=0.0.0.0 --no-browser --allow-root
```

Then open the printed `http://127.0.0.1:8888/lab?token=...` URL, navigate to `notebooks/`, and open any chapter.

**Every example is directly runnable** — click into a cell and press Shift+Enter.

---

## Reference environment

The book was written and every example verified against this exact stack:

| Component | Version |
|-----------|---------|
| Python | 3.11 |
| PySpark | 3.5.3 |
| Delta Lake | 3.2.0 |
| Apache Iceberg | 1.5.2 |
| pandas | 2.2.3 |
| pyarrow | 17.0.0 |
| Java | OpenJDK 17 |

You can absolutely use newer versions — but if an example behaves oddly, first check it against this stack. Version pinning is why the outputs in the book are reproducible.

---

## Chapter index

The book is organised in 8 parts covering 22 chapters and 1,000 examples:

### Part I — Getting Started
- [Chapter 1: Introduction to PySpark](docs/chapters/01-introduction.md) *(Examples 1–20)*
- [Chapter 2: Spark Session Management](docs/chapters/02-session.md) *(Examples 21–50)*

### Part II — DataFrame Fundamentals
- [Chapter 3: DataFrame Basics](docs/chapters/03-dataframe-basics.md) *(Examples 51–130)*
- [Chapter 4: Reading Files](docs/chapters/04-reading-files.md) *(Examples 131–190)*
- [Chapter 5: Writing Files](docs/chapters/05-writing-files.md) *(Examples 191–240)*
- [Chapter 6: Columns](docs/chapters/06-columns.md) *(Examples 241–290)*

### Part III — Shaping Data
- [Chapter 7: Selecting Data](docs/chapters/07-selecting.md)
- [Chapter 8: Filtering](docs/chapters/08-filtering.md)
- [Chapter 9: Grouping](docs/chapters/09-grouping.md)

### Part IV — Combining Data
- [Chapter 10: Aggregations](docs/chapters/10-aggregations.md)
- [Chapter 11: Joins](docs/chapters/11-joins.md)

### Part V — Rich Structures
- [Chapter 12: Complex Types](docs/chapters/12-complex-types.md)
- [Chapter 13: Pivoting](docs/chapters/13-pivoting.md)

### Part VI — Handling Variety
- [Chapter 14: Nulls](docs/chapters/14-nulls.md)
- [Chapter 15: Datetime](docs/chapters/15-datetime.md)
- [Chapter 16: Math](docs/chapters/16-math.md)
- [Chapter 17: Strings](docs/chapters/17-strings.md)

### Part VII — Advanced Techniques
- [Chapter 18: Windows](docs/chapters/18-windows.md)
- [Chapter 19: UDFs](docs/chapters/19-udfs.md)
- [Chapter 20: Performance](docs/chapters/20-performance.md)

### Part VIII — Production Patterns
- [Chapter 21: Table Formats and Change Data](docs/chapters/21-table-formats.md)
- [Chapter 22: Real-World Patterns](docs/chapters/22-patterns.md)

---

## About the book

**PySpark: 1,000 Examples** is a practical reference for data engineers who work with Apache Spark daily. Each example is short, focused, and independently runnable. Rather than long walkthroughs, the book packs each example into a consistent seven-part structure:

- **Problem Statement** — what you're solving
- **Solution** — the code
- **Output** — verified output from the reference environment
- **Explanation** — why this works
- **Common Mistake** — the trap most people fall into
- **Recommendation** — best practice
- **Pattern Insight** — how this generalizes

The 1,000 examples span everything from basic DataFrame construction to Delta Lake CDC, Iceberg time travel, streaming joins, and real-world Spark patterns.

**Get the book:** [Amazon Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Reporting errata or asking questions

Found a typo? Something doesn't work in the code? Have a question?

- [**Report an errata**](../../issues/new?template=errata-report.md) — corrections we'll add to `docs/errata.md`
- [**Ask a question**](../../issues/new?template=question.md) — for anything not book-specific but community-relevant
- [**Suggest a topic**](../../issues/new?template=suggestion.md) — for a future edition

Please check `docs/errata.md` before reporting to avoid duplicates.

---

## License

- **Code** in `notebooks/`, `scripts/`, and `conf/`: [MIT License](LICENSE) — do whatever you want, commercial use OK.
- **The book itself** (narrative, explanations, structure, cover, images): Copyright © 2026 Bi Learner. All rights reserved. Available for purchase on Amazon Kindle.
- **Chapter indexes** in `docs/chapters/`: CC BY 4.0 — please attribute if you republish.

---

## Support the work

If this book saved you time, the best thing you can do is:

1. Leave an honest review on Amazon — reviews genuinely help other engineers find the book
2. Star this repository ⭐
3. Share with your team or on LinkedIn/X

---

Made with care by Bi Learner. Reach out on [YouTube](https://youtube.com/@YOUR-CHANNEL) for tutorials and updates.
