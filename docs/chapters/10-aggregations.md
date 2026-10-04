# Chapter 10: Aggregations

**45 examples** (426–470)

Difficulty mix: 5 Beginner · 18 Intermediate · 22 Advanced

[📔 Open the notebook](../../notebooks/10-aggregations.ipynb) · [📖 Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 426: sum ignores nulls
*Beginner* · `sum`

Confirm that `sum` treats nulls as zero rather than propagating them.

### Example 427: avg ignores nulls too
*Beginner* · `avg`, `sum`, `count`

Compute a mean and understand what "mean" it computed.

### Example 428: max and min skip nulls
*Beginner* · `max`, `min`

Find the extreme values, ignoring rows with no value.

### Example 429: count in three shapes
*Beginner* · `count`, `countDistinct`

Show the three distinct meanings of "count" in one call.

### Example 430: count over an expression
*Intermediate* · `count`, `when`

Count rows satisfying each of several conditions in one aggregation.

### Example 431: avg of a boolean is a ratio
*Intermediate* · `avg`, `cast`

Compute the proportion of rows meeting a condition.

### Example 432: sum with widened output type
*Intermediate* · `sum`, `cast`

Understand what type `sum` returns and when overflow matters.

### Example 433: sum of doubles has precision hazards
*Advanced* · `sum`, `cast`

See how floating-point summation can lose precision on large groups.

### Example 434: Aggregate several columns programmatically
*Intermediate* · `dtypes`, `agg`

Compute the same aggregate for every numeric column of a DataFrame.

### Example 435: max_by and min_by pick associated values
*Advanced* · `max_by`, `min_by`

Find the value of one column at the row where another column is maximal.

### Example 436: first with ordering versus first_value
*Advanced* · `first`, `first_value`

Get the first value from a group deterministically.

### Example 437: mode picks the most common value
*Intermediate* · `mode`

Find the most frequent value in a column.

### Example 438: Exact percentile
*Intermediate* · `percentile`

Compute exact percentiles of a numeric column.

### Example 439: Approximate percentile
*Intermediate* · `percentile_approx`

Get percentiles quickly, trading exactness for speed.

### Example 440: Population and sample statistics differ
*Advanced* · `stddev`, `stddev_pop`, `var`, `var_pop`

Understand which standard deviation Spark computes by default.

### Example 441: Correlation and covariance
*Intermediate* · `corr`, `covar_samp`, `covar_pop`

Measure the linear relationship between two columns.

### Example 442: Skewness and kurtosis
*Advanced* · `skewness`, `kurtosis`

Measure the shape of a distribution beyond mean and variance.

### Example 443: Aggregate to fill downstream
*Intermediate* · `join`, `agg`

Compute an overall statistic and join it back to every row for downstream comparison.

### Example 444: collect_list preserves duplicates
*Intermediate* · `collect_list`, `collect_set`

Gather values from a group with and without duplicates.

### Example 445: Aggregate an array
*Advanced* · `aggregate`, `sort_array`

Compute a per-group sum of collected values inside the array itself.

### Example 446: Combine several summary sources
*Advanced* · `union`, `agg`

Produce one summary row with contributions from several DataFrames.

### Example 447: Aggregate on an empty input
*Advanced* · `agg`

See what each aggregate returns when there are no rows to aggregate.

### Example 448: Boolean aggregates: bool_and, bool_or
*Intermediate* · `bool_and`, `bool_or`

Test whether every row or any row in a group meets a condition.

### Example 449: Bitwise aggregates
*Advanced* · `bit_and`, `bit_or`, `bit_xor`

Combine integer values with bitwise operations across a group.

### Example 450: String concatenation aggregates
*Intermediate* · `concat_ws`, `collect_list`, `sort_array`

Concatenate the string values from a group into one comma-separated string.

### Example 451: Aggregate producing a JSON string
*Advanced* · `to_json`, `struct`, `collect_list`

Emit one JSON object per group summarising it.

### Example 452: Aggregate a nested field
*Advanced* · `groupBy`, `dot notation`

Aggregate a value from inside a struct column.

### Example 453: Aggregate an array element-wise
*Advanced* · `transform`, `aggregate`

Sum arrays element by element across rows.

### Example 454: Aggregate a map column
*Advanced* · `map_from_entries`, `collect_list`

Combine maps from many rows into one map per group.

### Example 455: Retain multiple aggregates from a struct
*Advanced* · `max_by`, `struct`

Return several associated columns at the row with the extremal value.

### Example 456: Split an aggregation across expressions
*Intermediate* · `agg`, `filter`

Compute aggregates over filtered subsets in the same call.

### Example 457: Aggregate expressions with alias reuse
*Advanced* · `agg`, `selectExpr`

Reference an aggregate in a subsequent expression within the same result.

### Example 458: Pivot as an aggregation shortcut
*Intermediate* · `pivot`, `agg`

Compute several aggregates broken out by another column, in wide form.

### Example 459: Sample and aggregate
*Intermediate* · `sample`, `agg`

Estimate a statistic on a sampled subset when the full computation is too expensive.

### Example 460: Aggregate to a schema
*Advanced* · `agg`, `schema comparison`

Produce a result whose schema matches a downstream contract exactly.

### Example 461: Test aggregates against known inputs
*Advanced* · `createDataFrame`, `agg`

Verify an aggregate returns the expected answer on constructed data.

### Example 462: Aggregate on a filtered subset
*Beginner* · `filter`, `agg`

Compute overall statistics on a filtered slice of a DataFrame.

### Example 463: Aggregate incrementally with union
*Advanced* · `union`, `agg`

Combine per-batch aggregates without re-scanning the source.

### Example 464: Aggregate on a Delta table
*Intermediate* · `format("delta")`, `agg`

Aggregate over a Delta table and confirm the read reflects the current transaction.

### Example 465: Aggregate with a running total via cumulative sum
*Advanced* · `Window`, `sum`

Compute a running total per group ordered by time.

### Example 466: Aggregate on multiple grain simultaneously
*Advanced* · `groupBy`, `union`

Produce region-level and country-level counts in one output.

### Example 467: Combine aggregates from two DataFrames
*Advanced* · `join`, `agg`

Compare a per-group aggregate from one source against the corresponding value from another.

### Example 468: Cache a source used for many aggregates
*Intermediate* · `cache`, `agg`

Compute several unrelated aggregations from the same expensive source.

### Example 469: Approximate quantile summary
*Advanced* · `approxQuantile`

Get multiple approximate quantiles directly from a DataFrame method.

### Example 470: Aggregation checklist
*Intermediate* · `review`

Summarise the decisions aggregation makes.

---

← [Back to main index](../../README.md)
