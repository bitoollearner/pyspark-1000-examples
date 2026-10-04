# Chapter 1: Introduction to PySpark

**20 examples** (1–20)

Difficulty mix: 16 Beginner · 4 Intermediate

[📔 Open the notebook](../../notebooks/01-introduction.ipynb) · [📖 Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 1: Confirm which Spark you are actually running
*Beginner* · `SparkSession.version`

Before debugging anything, establish which Spark version is running. Version mismatches between a local install and a...

### Example 2: Create a DataFrame from Python data
*Beginner* · `createDataFrame`, `show`

You want a small, throwaway DataFrame to test an idea, without touching a file.

### Example 3: Inspect a schema before trusting it
*Beginner* · `printSchema`, `dtypes`

You have a DataFrame and need to know its column names and types before writing transformations against it.

### Example 4: Count rows without materialising them
*Beginner* · `count`

You need to know how many rows a DataFrame holds — for a sanity check, or to confirm a filter did what you expected.

### Example 5: Look at data without pulling it all back
*Beginner* · `show`, `take`, `limit`

You want to eyeball a few rows of a large DataFrame to check a transformation worked.

### Example 6: Read your first file
*Beginner* · `read.csv`, `option`

Load the book's `orders.csv` into a DataFrame with correct column names and sensible types.

### Example 7: Watch a transformation do nothing
*Beginner* · `filter`, `select`

Demonstrate that building a chain of transformations performs no work at all.

### Example 8: Force execution with an action
*Beginner* · `count`, `collect`, `show`

Take the lazy chain from Example 7 and make it actually run.

### Example 9: Read the plan Spark intends to run
*Intermediate* · `explain`

See what Spark will actually execute, rather than what you wrote.

### Example 10: Find out how many partitions you have
*Intermediate* · `rdd.getNumPartitions`

Determine how many pieces Spark has split your DataFrame into.

### Example 11: Watch a shuffle change the partition count
*Intermediate* · `groupBy`, `repartition`

Show that a wide transformation reorganises data across partitions.

### Example 12: Understand why collect() is dangerous
*Beginner* · `collect`, `limit`

Retrieve rows into Python safely, and understand what makes the unsafe version unsafe.

### Example 13: Chain transformations readably
*Beginner* · `filter`, `withColumn`, `select`

Build a multi-step transformation that stays readable and reviewable.

### Example 14: The same aggregation in both
*Beginner* · `groupBy`, `agg`

You know how to group and sum in pandas. Write the same thing in PySpark and see what actually changes.

### Example 15: Convert a small result to pandas
*Beginner* · `toPandas`, `limit`

You want to plot a small aggregated result with a Python charting library.

### Example 16: Live without a row index
*Beginner* · `monotonically_increasing_id`, `row_number`

You need a per-row identifier, but Spark has no pandas-style index.

### Example 17: Nothing is mutable
*Beginner* · `withColumn`

Understand why adding a column appears to do nothing.

### Example 18: Inspect the configuration actually in force
*Intermediate* · `spark.conf.get`

Confirm which settings your session is really using, rather than the ones you believe you set.

### Example 19: Confirm the Spark UI is available
*Beginner* · `spark.conf.get`

Find out whether the web UI is enabled, so you can inspect jobs while they run.

### Example 20: Stop a session deliberately
*Beginner* · `SparkSession.stop`, `getActiveSession`

Release Spark's resources when a script finishes, and understand what that means for anything still holding the session.

---

← [Back to main index](../../README.md)
