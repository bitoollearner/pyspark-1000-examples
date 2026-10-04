# Chapter 9: Grouping Data

**40 examples** (386–425)

Difficulty mix: 11 Beginner · 18 Intermediate · 11 Advanced

[📔 Open the notebook](../../notebooks/09-grouping.ipynb) · [📖 Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 386: Group and count
*Beginner* · `groupBy`, `count`

Produce one row per group, showing how many rows fell into each.

### Example 387: Count as an aggregation function
*Beginner* · `groupBy`, `agg`, `count`

Achieve the same result using the general `agg` form.

### Example 388: Group by several columns
*Beginner* · `groupBy`

Produce one row per combination of two columns.

### Example 389: See what happens to non-grouped columns
*Beginner* · `groupBy`

Understand why a group-by cannot simply keep the other columns.

### Example 390: Aggregate several columns at once
*Intermediate* · `agg`, `sum`, `avg`

Produce several statistics per group in one call.

### Example 391: See how nulls in the key become a group
*Intermediate* · `groupBy`

Determine what happens to rows whose grouping column is null.

### Example 392: Detect a null key silently
*Advanced* · `groupBy`

Show how a null key in the source produces a null group in the output.

### Example 393: Group after normalising the key
*Intermediate* · `coalesce`, `groupBy`

Give the null-key group a real name in the output.

### Example 394: Check the group cardinality
*Advanced* · `countDistinct`

Estimate how many groups a group-by will produce before running it.

### Example 395: Group by an expression
*Intermediate* · `groupBy`

Group by a derived value rather than a raw column.

### Example 396: Sum a column per group
*Beginner* · `sum`

Total a numeric column across each group.

### Example 397: Average, min, max
*Beginner* · `avg`, `min`, `max`

Compute several summary statistics per group.

### Example 398: Count distinct
*Beginner* · `countDistinct`

Count how many distinct values appear in a column per group.

### Example 399: Approximate distinct
*Intermediate* · `approx_count_distinct`

Estimate distinct counts quickly, trading accuracy for speed.

### Example 400: Collect values into a list
*Intermediate* · `collect_list`, `collect_set`

Gather the values from a column into a list per group.

### Example 401: Combine several aggregate types
*Intermediate* · `agg`

Compute counts, sums, and collections in one aggregation call.

### Example 402: count(col) versus count("*")
*Intermediate* · `count`

Understand the difference between counting rows and counting values.

### Example 403: first and last
*Intermediate* · `first`, `last`

Take one representative value per group.

### Example 404: Aggregate a boolean column
*Intermediate* · `sum`, `cast`

Count rows meeting a condition using a boolean aggregate.

### Example 405: Group and rank aggregates
*Advanced* · `agg`, `orderBy`, `limit`

Find the top N groups by an aggregate.

### Example 406: Roll up totals
*Intermediate* · `rollup`

Produce per-group counts and a grand total in one aggregation.

### Example 407: Cross-tabulate with cube
*Intermediate* · `cube`

Produce every combination of grouping levels including the empty one.

### Example 408: Distinguish subtotal nulls from real nulls
*Advanced* · `grouping`, `rollup`

Tell subtotal rows apart from rows with genuinely null keys.

### Example 409: Choose specific grouping combinations
*Advanced* · `grouping_sets`

Produce a specific set of grouping combinations rather than every combination.

### Example 410: Aggregate the whole DataFrame
*Beginner* · `agg`

Produce a single-row summary of a whole DataFrame.

### Example 411: Summary statistics in one call
*Beginner* · `describe`, `summary`

Get a quick statistical profile of a numeric column.

### Example 412: Group and pivot preview
*Intermediate* · `groupBy`, `pivot`

Turn distinct values of a column into their own columns.

### Example 413: Pre-aggregate before joining
*Advanced* · `groupBy`, `join`

Reduce data before combining DataFrames.

### Example 414: Detect skew in group sizes
*Advanced* · `groupBy`, `count`

Find out whether a group-by will produce lopsided groups.

### Example 415: Reduce skew with a salt
*Advanced* · `groupBy`, `salt`

Split one enormous group across several partitions so no single task holds everything.

### Example 416: distinct is a group-by
*Intermediate* · `distinct`

Understand what `distinct()` actually does under the hood.

### Example 417: dropDuplicates keeps a subset
*Intermediate* · `dropDuplicates`

Deduplicate on some columns while keeping others.

### Example 418: Deduplicate on a computed key
*Intermediate* · `dropDuplicates`, `expression`

Deduplicate on a derived value rather than an existing column.

### Example 419: Group with a where clause
*Beginner* · `groupBy`, `filter`

Filter the source rows before grouping.

### Example 420: Filter that changes the answer
*Advanced* · `groupBy`, `filter`

Show a case where the filter position changes the result, not just the cost.

### Example 421: Cache a heavily-grouped source
*Intermediate* · `cache`

Compute several unrelated aggregations from the same source.

### Example 422: Compare group counts across DataFrames
*Advanced* · `groupBy`, `join`

Reconcile per-group counts between two DataFrames.

### Example 423: Whole-DataFrame agg on a filter
*Beginner* · `agg`

Compute a single-row summary of a filtered subset.

### Example 424: Aggregate an empty group
*Advanced* · `groupBy`, `count`

Handle an aggregation over a source that has no rows.

### Example 425: Preview: window functions
*Intermediate* · `Window`, `row_number`

Pick one row per group by an explicit ordering — the deterministic alternative to `dropDuplicates`.

---

← [Back to main index](../../README.md)
