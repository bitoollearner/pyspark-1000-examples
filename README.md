# PySpark: 1,000 Examples - Companion Code

> Official code companion for the eBook **[PySpark: 1,000 Examples: A Practical Reference for Data Engineers](https://www.amazon.com/dp/B0DXXXXXXX)** - available on Amazon Kindle.

This repository contains the reference environment and dataset generator for the book. Combined with the Docker image, it is everything you need to practice the 1,000 examples locally - matching the exact environment they were verified against.

The book itself (narrative, explanations, worked solutions, common mistakes, pattern insights) is not included here. Get it on [Amazon Kindle](https://www.amazon.com/dp/B0DXXXXXXX).

---

## Quick start - 2 minutes to running

**Prerequisite:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.

**Mac / Linux:**
```bash
mkdir practice
docker run --rm -p 8888:8888 -p 4040:4040 \
  -v $(pwd)/practice:/workspace/practice \
  bilearner/pyspark1000-practice:1.0
```

**Windows PowerShell:**
```powershell
mkdir practice -Force
docker run --rm -p 8888:8888 -p 4040:4040 `
  -v ${PWD}/practice:/workspace/practice `
  bilearner/pyspark1000-practice:1.0
```

Open **http://localhost:8888** - JupyterLab opens with 22 chapter folders ready for practice.

That is the entire setup. See **[docs/SETUP.md](docs/SETUP.md)** for the detailed walkthrough.

---

## How to use

1. Open the book on Kindle, pick an example (say Chapter 10, Example 388)
2. In JupyterLab, open `chapter-10-aggregations/scratch.ipynb`
3. Run the Chapter setup cell at the top (once per session)
4. Type the example's Solution code into a new cell
5. Shift+Enter - compare your output to the book's Output section
6. Read the book's Explanation, Common Mistake, Recommendation, and Pattern Insight

Why type the code yourself? Reading code is not the same as writing it. Typing `F.col("x")`, catching your own typos, exploring autocomplete - that is where the learning happens.

---

## What's in this repository

| Folder | What's inside |
|--------|---------------|
| `docs/SETUP.md` | Detailed step-by-step setup guide |
| `docs/chapters/` | Index of every chapter and example in the book |
| `docs/function-index.md` | Alphabetical index of PySpark functions covered |
| `docs/errata.md` | Corrections found after publication (report yours via Issues!) |
| `conf/` | Spark configuration (log4j2, spark-defaults) |
| `scripts/` | Utilities: environment verifier, chapter-index generator |
| `datasets/` | Dataset generator (`generate.py`) - produces the data every example references |
| `Dockerfile`, `Dockerfile.allinone`, `docker-compose.yml`, `requirements.txt` | The reference environment |
| `build-and-push.ps1` | Script that builds the practice image and pushes it to Docker Hub |

---

## Reference environment

Every example in the book was verified against this exact stack:

| Component | Version |
|-----------|---------|
| Python | 3.11 |
| PySpark | 3.5.3 |
| Delta Lake | 3.2.0 |
| Apache Iceberg | 1.5.2 |
| pandas | 2.2.3 |
| pyarrow | 17.0.0 |
| Java | OpenJDK 17 |

The all-in-one Docker image at `bilearner/pyspark1000-practice:1.0` contains this exact stack plus all the datasets.

---

## Chapter index

The book is organised in 8 parts covering 22 chapters and 1,000 examples:

### Part I - Getting Started
- [Chapter 1: Introduction to PySpark](docs/chapters/01-introduction.md)
- [Chapter 2: Spark Session Management](docs/chapters/02-session.md)

### Part II - DataFrame Fundamentals
- [Chapter 3: DataFrame Basics](docs/chapters/03-dataframe-basics.md)
- [Chapter 4: Reading Files](docs/chapters/04-reading-files.md)
- [Chapter 5: Writing Files](docs/chapters/05-writing-files.md)
- [Chapter 6: Columns](docs/chapters/06-columns.md)

### Part III - Shaping Data
- [Chapter 7: Selecting Data](docs/chapters/07-selecting.md)
- [Chapter 8: Filtering](docs/chapters/08-filtering.md)
- [Chapter 9: Grouping](docs/chapters/09-grouping.md)

### Part IV - Combining Data
- [Chapter 10: Aggregations](docs/chapters/10-aggregations.md)
- [Chapter 11: Joins](docs/chapters/11-joins.md)

### Part V - Rich Structures
- [Chapter 12: Complex Types](docs/chapters/12-complex-types.md)
- [Chapter 13: Pivoting](docs/chapters/13-pivoting.md)

### Part VI - Handling Variety
- [Chapter 14: Nulls](docs/chapters/14-nulls.md)
- [Chapter 15: Datetime](docs/chapters/15-datetime.md)
- [Chapter 16: Math](docs/chapters/16-math.md)
- [Chapter 17: Strings](docs/chapters/17-strings.md)

### Part VII - Advanced Techniques
- [Chapter 18: Windows](docs/chapters/18-windows.md)
- [Chapter 19: UDFs](docs/chapters/19-udfs.md)
- [Chapter 20: Performance](docs/chapters/20-performance.md)

### Part VIII - Production Patterns
- [Chapter 21: Table Formats and Change Data](docs/chapters/21-table-formats.md)
- [Chapter 22: Real-World Patterns](docs/chapters/22-patterns.md)

---

## Datasets

The practice image bakes in a canonical dataset spine seeded from a fixed random value, so every reader works with byte-identical data. See [datasets/README.md](datasets/README.md) for the full list.

Running the datasets fresh locally (outside the image):

```bash
# Core CSVs + raw messy files (no Spark needed)
pip install faker pandas
python datasets/generate.py --core

# Add binary format variants (needs Spark + Delta on classpath)
python datasets/generate.py --formats
```

---

## About the book

**PySpark: 1,000 Examples** is a practical reference for data engineers who work with Apache Spark daily. Each example is short, focused, and independently runnable. Rather than long walkthroughs, the book packs each example into a consistent seven-part structure:

- **Problem Statement** - what you are solving
- **Solution** - the code
- **Output** - verified output from the reference environment
- **Explanation** - why this works
- **Common Mistake** - the trap most people fall into
- **Recommendation** - best practice
- **Pattern Insight** - how this generalizes

**Get the book:** [Amazon Kindle](https://www.amazon.com/dp/B0DXXXXXXX)

---

## Reporting errata or asking questions

Found a typo? Something doesn't work in the code? Have a question?

- [Report an errata](../../issues/new?template=errata-report.md) - corrections we add to `docs/errata.md`
- [Ask a question](../../issues/new?template=question.md) - for anything community-relevant
- [Suggest a topic](../../issues/new?template=suggestion.md) - for a future edition

Please check `docs/errata.md` before reporting to avoid duplicates.

---

## License

- **Code** in `scripts/`, `conf/`, `datasets/generate.py`, and the Dockerfiles: [MIT License](LICENSE) - do whatever you want, commercial use OK.
- **The book itself** (narrative, explanations, worked solutions, structure, cover, images): Copyright (c) 2026 @bilearner. All rights reserved. Available on Amazon Kindle.
- **Chapter indexes** in `docs/chapters/`: CC BY 4.0 - please attribute if you republish.

---

## Support the work

If this book saved you time, the best thing you can do is:

1. Leave an honest review on Amazon - reviews genuinely help other engineers find the book
2. Star this repository
3. Share with your team or on LinkedIn/X

---

Made with care by @bilearner. Reach out on YouTube for tutorials and updates.
