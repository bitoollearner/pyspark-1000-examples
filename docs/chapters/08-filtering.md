# Chapter 8: Filtering Data

**45 examples** (341–385)

Difficulty mix: 14 Beginner · 18 Intermediate · 13 Advanced

[📔 Open the notebook](../../notebooks/08-filtering.ipynb) · [📖 Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 341: filter and where are the same
*Beginner* · `filter`, `where`

Establish whether the two method names differ in any way.

### Example 342: Filter on a comparison
*Beginner* · `filter`, ``>``

Keep only the rows whose numeric column exceeds a threshold.

### Example 343: Require both conditions
*Beginner* · ``&``

Keep rows that satisfy two conditions at once.

### Example 344: Accept either condition
*Beginner* · ``|``, `isin`

Keep rows matching one of several values.

### Example 345: Negate a condition
*Beginner* · ``~``, ``!=``

Keep the rows that do not match a condition.

### Example 346: Negation over a nullable column
*Intermediate* · `filter`, `isNull`

Measure how much data three-valued logic makes invisible.

### Example 347: Compare against null directly
*Beginner* · `isNull`, ``==``

See why `col == None` returns nothing.

### Example 348: Include nulls deliberately
*Intermediate* · ``|``, `isNull`

Keep the rows that match a condition *and* the rows where the answer is unknown.

### Example 349: Find rows with missing values
*Beginner* · `isNull`

List the rows where a specific column is null.

### Example 350: Exclude rows with missing values
*Beginner* · `isNotNull`, `na.drop`

Drop rows where a specific column is null.

### Example 351: Match against a set of values
*Beginner* · `isin`

Keep rows whose column matches one of several fixed values.

### Example 352: Filter a numeric range
*Beginner* · `between`

Keep rows whose value falls within an inclusive range.

### Example 353: Match a substring
*Beginner* · `contains`, `startswith`, `endswith`

Filter text columns by substring position.

### Example 354: Match a SQL pattern
*Beginner* · `like`

Filter using SQL's wildcard pattern syntax.

### Example 355: Match a regular expression
*Intermediate* · `rlike`

Filter using a Java-style regular expression.

### Example 356: Filter without regard to case
*Intermediate* · `lower`, `rlike`

Match values regardless of capitalisation.

### Example 357: Filter on a computed value
*Intermediate* · `length`, `filter`

Filter on the result of an expression rather than a raw column.

### Example 358: Filter on a column added earlier
*Beginner* · `withColumn`, `filter`

Add a derived column and filter on it in the same chain.

### Example 359: Filter with a SQL string
*Intermediate* · `filter`

Write a predicate as a SQL string rather than a column expression.

### Example 360: Build a predicate at runtime
*Intermediate* · `col`, `filter`

Construct a filter from values decided at runtime.

### Example 361: Combine a list of predicates
*Intermediate* · `reduce`, ``&``

Combine an unknown number of predicates into one.

### Example 362: Apply predicates as separate steps
*Advanced* · `filter`, `explain`

Determine whether chaining several `filter` calls costs anything against combining them with `&`.

### Example 363: See a predicate reach the file reader
*Advanced* · `filter`, `explain`

Confirm that a filter is applied by the file reader rather than after loading.

### Example 364: Filter that cannot be pushed down
*Advanced* · `filter`, `explain`

See what defeats predicate pushdown.

### Example 365: Prune partitions with a filter
*Advanced* · `filter`, `partitioned read`

Filter on a partition column and confirm Spark skips whole directories.

### Example 366: Defeat partition pruning with a function
*Advanced* · `filter`, `explain`

Show how a function on a partition column prevents pruning.

### Example 367: Filter early to reduce a shuffle
*Intermediate* · `filter`, `join`

Filter before a join and confirm it makes a measurable difference.

### Example 368: Filter after aggregation
*Intermediate* · `groupBy`, `agg`, `filter`

Keep only the groups meeting a condition on the aggregate.

### Example 369: Filter with a subquery
*Advanced* · `collect`, `filter`, `isin`

Filter one DataFrame using values derived from another.

### Example 370: Filter on nested fields
*Intermediate* · `filter`, `dot notation`

Filter on a field inside a struct column.

### Example 371: Filter with a UDF
*Advanced* · `udf`, `filter`

See what a filter using a UDF costs compared with a built-in.

### Example 372: Filter and count in one pass
*Intermediate* · `count`, `when`

Count how many rows satisfy each of several conditions without scanning several times.

### Example 373: Sample rows instead of filtering
*Intermediate* · `sample`

Take a random subset of rows for exploration.

### Example 374: Filter with limit for exploration
*Beginner* · `limit`

Look at a small number of rows without processing the whole dataset.

### Example 375: Filter to the top-N
*Intermediate* · `orderBy`, `limit`

Take the N largest values from a column.

### Example 376: Exclude with an anti-join
*Advanced* · `join with `left_anti``

Filter out rows whose key appears in another DataFrame.

### Example 377: Keep matches with a semi-join
*Advanced* · `join with `left_semi``

Filter to rows whose key appears in another DataFrame, without pulling any of its columns.

### Example 378: Anti-join to spot orphans
*Advanced* · `join with `left_anti``

Find rows whose foreign key does not resolve.

### Example 379: Compare isin against a semi-join
*Advanced* · `isin`, `join`

See when the two forms diverge in behaviour.

### Example 380: Filter a large candidate set
*Advanced* · `semi-join`

Filter one table to rows whose id appears in a much larger set.

### Example 381: Filter an array column
*Intermediate* · `array_contains`, `size`

Filter rows whose array column contains a particular value.

### Example 382: Filter a map column
*Intermediate* · `map access`, `isNotNull`

Filter rows whose map column has a particular key.

### Example 383: Cache before repeated filtering
*Intermediate* · `cache`, `filter`

Filter one source by several conditions without re-reading it.

### Example 384: Filter safely against an empty source
*Advanced* · `filter`, `count`

Handle a filter against a DataFrame that has no rows.

### Example 385: Review the filter checklist
*Intermediate* · `review`

Summarise the decisions a filter makes.

---

← [Back to main index](../../README.md)
