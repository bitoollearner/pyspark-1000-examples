# Seeded datasets

The book's examples reference a canonical set of seeded datasets. Everything
is generated from a fixed random seed (`SEED = 20240816`), so regenerating
produces byte-identical files on every machine. That matters: every output
block in the book is diffed against real Spark output; if the data shifts,
the examples break.

## What's in here after a full build

### Core tables (CSVs)

| File | Rows | What it's for |
|------|------|---------------|
| `customers.csv` | ~500 | Customer dimensions, nulls, SCD examples, joins |
| `products.csv` | ~80 | Pivots, categories, broadcast joins |
| `orders.csv` | ~2,000 | The fact table — groupBy, aggregations, joins |
| `order_items.csv` | ~5,000 | Line-level grain, explode/aggregate practice |
| `employees.csv` | ~120 | Hierarchy and salaries — windows, ranking |
| `web_events.csv` | ~5,000 | Sessionization, gap detection, time series |
| `transactions.csv` | ~3,000 | Fraud patterns, running totals |

### Raw messy files (Chapter 4 — Reading Files)

Everything deliberately broken in some way:

| File | What it demonstrates |
|------|---------------------|
| `raw/customers_dirty.csv` | Ragged rows, stray quotes, blank lines, unparseable values |
| `raw/orders_multiline.json` | Pretty-printed JSON needing `multiLine=True` |
| `raw/orders_nested.jsonl` | Newline-delimited JSON with nested structs and arrays |
| `raw/employees_fixed_width.txt` | No delimiter — parsed with `substring()` |
| `raw/customers.xml` | XML — needs `spark-xml` JAR |
| `raw/products_pipe.txt` | Pipe-delimited |
| `raw/notes_multiline.csv` | Newline inside a quoted field |
| `raw/daily/*.csv` | Same-schema daily files — directory reads, globs, `input_file_name()` |
| `raw/padded_regions.csv` | Whitespace padding — `" North"` != `"North"` for joins |
| `raw/by_region/region=*/data.csv` | Hive-style partitioned directories |

### Binary-format variants (Chapters 4, 5, 21)

Built by Spark from the core CSVs:

| Folder | Format |
|--------|--------|
| `formats/parquet/{customers,orders,order_items,products}/` | Parquet |
| `formats/parquet/orders_partitioned/` | Partitioned by `region`, `status` |
| `formats/orc/{...}/` | ORC |
| `formats/avro/{...}/` | Avro |
| `formats/delta/{...}/` | Delta Lake (with `_delta_log`) |

## Regenerating

In the practice Docker image, the datasets are baked in — no action needed.

To regenerate manually (e.g., after editing `generate.py`):

```bash
# Everything at once (needs Spark)
python datasets/generate.py --all

# Just the CSVs + raw files (no Spark needed)
python datasets/generate.py --core

# Just the binary formats (needs Spark; expects CSVs to already exist)
python datasets/generate.py --formats

# Larger dataset for performance-chapter examples
python datasets/generate.py --all --scale 5
```

Required Python packages for `--core`: `faker`, `pandas`.
For `--formats`: PySpark + delta-spark on the classpath.

## Why these specific tables

Each table is deliberately shaped to make a chapter's examples work:

- **employees** has one CEO and small team sizes so `RANK` vs `DENSE_RANK` vs `ROW_NUMBER` show different results on ties
- **orders** has `ship_ts` nulls where the order was cancelled — real nulls for Chapter 14, not placeholders
- **web_events** has bursty sessions with deliberate gaps between them — gives you something real to sessionize in Chapter 18
- **transactions** has a small planted set of fraud-shaped rows (large amounts, odd currencies, foreign countries) — findable but not obvious, good for Chapter 17 pattern matching
- **customers** has ~8% null emails on purpose — Chapter 14 nulls examples depend on these

## Not checked into Git

The `.gitignore` excludes everything in this folder except this README and the
`generate.py` script. Datasets are regenerable from the seed, so there's no
point versioning them.
