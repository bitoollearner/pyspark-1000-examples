# Chapter 3: DataFrame Basics

**80 examples** (51–130)

Difficulty mix: 29 Beginner · 38 Intermediate · 13 Advanced

[📔 Open the notebook](../../notebooks/03-dataframe-basics.ipynb) · [📖 Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 51: Build from Row objects
*Beginner* · `Row`, `createDataFrame`

Construct a DataFrame where each record is named rather than positional, so the code reads clearly and column order c...

### Example 52: Build from a list of dictionaries
*Beginner* · `createDataFrame`

You have records as Python dictionaries — from a JSON API, say — and want a DataFrame without restructuring them first.

### Example 53: Convert a pandas DataFrame
*Beginner* · `createDataFrame`

You have a small pandas DataFrame — from a spreadsheet or a library that returns one — and need it in Spark.

### Example 54: Create an empty DataFrame with a schema
*Intermediate* · `createDataFrame`, `StructType`

Produce a DataFrame with correct structure but no rows, to serve as a starting point for a union or an empty-result p...

### Example 55: Generate a numeric DataFrame
*Beginner* · `spark.range`

Create a DataFrame of sequential numbers for testing, benchmarking, or as a skeleton to join against.

### Example 56: Build from an RDD
*Intermediate* · `parallelize`, `createDataFrame`

Convert an RDD — from legacy code or a text-processing step — into a DataFrame with a proper schema.

### Example 57: Declare a schema with StructType
*Intermediate* · `StructType`, `StructField`

State a DataFrame's structure explicitly rather than letting Spark infer it.

### Example 58: Declare a schema with a DDL string
*Intermediate* · `createDataFrame`

Write the same schema in a compact form that fits on one line and is readable by people who know SQL.

### Example 59: Read a schema back as an object
*Intermediate* · `df.schema`, `simpleString`

Extract a DataFrame's schema programmatically, to compare or reuse it.

### Example 60: Compare inference against declaration
*Intermediate* · `createDataFrame`, `simpleString`

See concretely how an inferred schema differs from a declared one over the same data.

### Example 61: Enforce non-nullability
*Intermediate* · `StructField`

Declare that a column must never be null, and observe what Spark does when it is.

### Example 62: Serialise a schema and reuse it
*Advanced* · `schema.json`, `StructType.fromJson`

Store a schema outside your code so several jobs can share one definition.

### Example 63: Attach metadata to a field
*Advanced* · `StructField`, `metadata`

Carry documentation alongside a column so it travels with the data rather than living in a separate wiki.

### Example 64: Nest a struct inside a schema
*Intermediate* · `StructType`, `col`

Model a record with a nested object — an address inside a customer — and read a field out of it.

### Example 65: Declare an array column
*Intermediate* · `ArrayType`, `size`

Store a variable-length list inside a single column and query its length.

### Example 66: Declare a map column
*Intermediate* · `MapType`

Store key-value attributes whose keys are not known when the schema is written.

### Example 67: Print a deeply nested schema
*Beginner* · `printSchema`

Inspect the structure of a DataFrame containing nesting inside nesting.

### Example 68: Choose between schema, dtypes, and columns
*Beginner* · `schema`, `dtypes`, `columns`

Pick the right accessor for the structural information you actually need.

### Example 69: Rename every column at once
*Intermediate* · `toDF`

Replace all column names in one operation — after reading a headerless file, for instance.

### Example 70: Get the shape of a DataFrame
*Beginner* · `count`, `len`

Produce the row and column counts, the equivalent of pandas' `.shape`.

### Example 71: Cast a string column to a number
*Beginner* · `cast`

A column arrived as text — from a CSV read without `inferSchema` — and you need to do arithmetic on it.

### Example 72: Watch a failed cast produce null
*Beginner* · `cast`

Find out what Spark does with a value that cannot be converted.

### Example 73: Measure what a cast destroyed
*Intermediate* · `cast`, `isNull`, `count`

Quantify how many values a cast turned into null, so a silent failure becomes a visible number.

### Example 74: Use try_cast to be explicit about failure
*Intermediate* · `expr`, `try_cast`

Signal in the code itself that a conversion is expected to fail sometimes.

### Example 75: Make bad casts raise with ANSI mode
*Advanced* · `spark.conf.set`

Configure Spark to fail loudly on an invalid cast instead of producing null.

### Example 76: Understand overflow in a narrowing cast
*Intermediate* · `cast`

Convert values that may not fit in the target type, and see what Spark does with the ones that do not.

### Example 77: Use decimal for money, not double
*Intermediate* · `DecimalType`, `cast`

Add currency amounts and get the exact answer rather than a floating-point approximation.

### Example 78: Choose precision and scale
*Intermediate* · `DecimalType`

Decide the two numbers in `DecimalType(p, s)` and see what happens when a value does not fit.

### Example 79: Cast a string to a date
*Beginner* · `to_date`, `cast`

Convert date text into a real date type so date arithmetic and comparisons work.

### Example 80: Cast a string to boolean
*Beginner* · `cast`

Convert text flags into real booleans, and learn which spellings Spark accepts.

### Example 81: Write a cast two ways
*Beginner* · `cast`

Choose between the string form and the type-object form of a cast.

### Example 82: Cast several columns at once
*Intermediate* · `cast`, `select`

Apply types to a DataFrame whose columns all arrived as strings, without writing one line per column.

### Example 83: Watch types coerce in arithmetic
*Intermediate* · `arithmetic operators`

Determine the resulting type when operands of different types are combined.

### Example 84: Divide integers
*Beginner* · `division operator`

Divide two integers and establish what type comes back.

### Example 85: Watch nulls propagate through arithmetic
*Beginner* · `arithmetic operators`, `coalesce`

Calculate a total across columns where one value may be missing.

### Example 86: Compare values of different types
*Intermediate* · `comparison operators`

Compare a numeric column against a string literal and see how Spark resolves it.

### Example 87: Resolve types when unioning DataFrames
*Intermediate* · `unionByName`

Combine two DataFrames whose matching columns have different types.

### Example 88: Check a column's type before acting
*Intermediate* · `df.schema`, `dtypes`

Write code that adapts to a column's type rather than assuming it.

### Example 89: Round-trip a number through a string safely
*Advanced* · `cast`, `format_number`

Convert a number to text for output and back again without losing precision.

### Example 90: Fail fast on an unexpected schema
*Advanced* · `df.schema`, `simpleString`

Stop a pipeline at the boundary when incoming data does not match the expected contract.

### Example 91: Add a derived column
*Beginner* · `withColumn`

Add a computed column to an existing DataFrame without rebuilding it.

### Example 92: Add a constant column
*Beginner* · `lit`, `withColumn`

Tag every row with a fixed value — a source system name, a load date, a version marker.

### Example 93: Add several columns in one call
*Intermediate* · `withColumns`

Add three derived columns without chaining three separate calls.

### Example 94: Remove a column
*Beginner* · `drop`

Discard a column that should not travel further — an internal key, or something sensitive.

### Example 95: Remove several columns
*Beginner* · `drop`

Discard a set of columns, computed at runtime rather than hard-coded.

### Example 96: Rename one column
*Beginner* · `withColumnRenamed`

Change a single column's name while leaving everything else untouched.

### Example 97: Reorder columns
*Beginner* · `select`

Put columns in a specific order — to match a target table's layout, or simply for readability.

### Example 98: Replace a column in place
*Beginner* · `withColumn`

Clean a column's values while keeping its name and position.

### Example 99: Build a column conditionally
*Beginner* · `when`, `otherwise`

Derive a category from a numeric value, with a fallback for anything unmatched.

### Example 100: Write a column as a SQL expression
*Intermediate* · `expr`, `selectExpr`

Use SQL syntax for a derivation, where the SQL reads more clearly than the DataFrame API.

### Example 101: Select columns by pattern
*Advanced* · `colRegex`

Select every column whose name matches a pattern, without listing them.

### Example 102: Remove duplicate rows
*Beginner* · `distinct`

Collapse rows that are identical across every column.

### Example 103: Deduplicate on chosen columns
*Intermediate* · `dropDuplicates`

Keep one row per business key, even when other columns differ.

### Example 104: Count distinct values in a column
*Beginner* · `countDistinct`, `approx_count_distinct`

Find how many unique values a column holds.

### Example 105: Take a few rows, four ways
*Beginner* · `limit`, `head`, `first`, `take`

Retrieve a small number of rows and understand what each method returns.

### Example 106: Sample rows reproducibly
*Intermediate* · `sample`

Take a random subset for development, and get the same subset every run.

### Example 107: Get quick summary statistics
*Beginner* · `describe`

Get a fast overview of a numeric column's distribution.

### Example 108: Choose which statistics to compute
*Intermediate* · `summary`

Get percentiles as well as the basic statistics, without the ones you do not need.

### Example 109: Sort a DataFrame
*Beginner* · `orderBy`, `asc`, `desc`

Order rows by one column ascending and another descending.

### Example 110: Control where nulls sort
*Intermediate* · `asc_nulls_last`, `desc_nulls_first`

Decide whether missing values appear at the top or the bottom of a sort.

### Example 111: Cache a DataFrame you will reuse
*Intermediate* · `cache`, `count`

A DataFrame is referenced several times in one job. Compute it once instead of recomputing it at every action.

### Example 112: Choose a storage level
*Advanced* · `persist`, `StorageLevel`

Cache data too large for memory alone, so Spark spills to disk instead of dropping it.

### Example 113: Release cached data
*Intermediate* · `unpersist`

Free the memory a cached DataFrame is holding once it is no longer needed.

### Example 114: Check whether a DataFrame is cached
*Beginner* · `is_cached`, `storageLevel`

Determine the cache state of a DataFrame before deciding whether to cache it again.

### Example 115: Understand that caching is lazy
*Intermediate* · `cache`, `count`

Establish exactly when cached data is written to memory.

### Example 116: Increase the partition count
*Intermediate* · `repartition`

Raise parallelism on a DataFrame that has too few partitions to use the available cores.

### Example 117: Reduce partitions without a full shuffle
*Intermediate* · `coalesce`

Combine partitions before writing, so the output is not thousands of tiny files.

### Example 118: Partition by a column
*Advanced* · `repartition`

Place all rows sharing a key on the same partition, so later grouping does not need to shuffle again.

### Example 119: See how rows are spread across partitions
*Intermediate* · `spark_partition_id`

Find out how many rows each partition holds.

### Example 120: Attach the partition id to each row
*Intermediate* · `spark_partition_id`

Inspect which partition individual rows landed on, for debugging.

### Example 121: Detect skew from partition sizes
*Advanced* · `spark_partition_id`, `summary`

Quantify how unevenly data is distributed, rather than eyeballing it.

### Example 122: Package a transformation with transform()
*Advanced* · `transform`

Extract a reusable transformation so it can be tested and shared, without breaking the method chain.

### Example 123: Chain several transforms
*Advanced* · `transform`

Compose multiple reusable steps into one readable pipeline.

### Example 124: Find rows present in one DataFrame and not another
*Intermediate* · `exceptAll`, `subtract`

Identify what changed between two versions of a dataset.

### Example 125: Compare two DataFrames for equality
*Intermediate* · `exceptAll`, `count`

Determine whether two DataFrames hold exactly the same data.

### Example 126: Assert equality in a test
*Advanced* · `chispa.assert_df_equality`

Write a test that fails with a useful message when a transformation produces the wrong result.

### Example 127: Convert rows to dictionaries
*Beginner* · `asDict`

Turn collected rows into plain Python dictionaries for use outside Spark.

### Example 128: Convert a DataFrame to JSON strings
*Intermediate* · `toJSON`

Produce one JSON document per row, for a message queue or an HTTP payload.

### Example 129: Alias a DataFrame to disambiguate columns
*Intermediate* · `alias`

Give a DataFrame a name so its columns can be referenced unambiguously when two DataFrames share column names.

### Example 130: Stream rows to Python without collecting
*Advanced* · `toLocalIterator`

Process every row in Python when the full result would not fit in driver memory.

---

← [Back to main index](../../README.md)
