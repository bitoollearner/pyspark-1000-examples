# Chapter 14: Nulls

**45 examples** (616â€“660)

Difficulty mix: 8 Beginner Â· 30 Intermediate Â· 7 Advanced

[ðŸ“” Open the notebook](../../notebooks/14-nulls.ipynb) Â· [ðŸ“– Read the chapter on Kindle](https://www.amazon.com/dp/B0DXXXXXXX)

---

## Examples

### Example 616: Equality with null
*Beginner* Â· `comparison`

See what happens when a column is compared to a null literal, and to another null-valued column.

### Example 617: isNull and isNotNull
*Beginner* Â· `isNull`, `isNotNull`

Test whether a column value is null or not, producing a proper boolean.

### Example 618: AND and OR with null
*Intermediate* Â· `boolean operators`

Understand how three-valued logic propagates through AND and OR.

### Example 619: NOT with null
*Intermediate* Â· `negation`

See what negation does to a null value.

### Example 620: Arithmetic with null
*Intermediate* Â· `arithmetic`

Confirm that arithmetic operations propagate null.

### Example 621: CASE and when with null
*Intermediate* Â· `when`, `otherwise`

See what a `when` expression does when its condition is null.

### Example 622: Filter on a nullable predicate
*Intermediate* Â· `filter`

Confirm that null predicates cause rows to be dropped by `filter`.

### Example 623: coalesce for a first non-null
*Beginner* Â· `coalesce`

Pick the first non-null value from several columns.

### Example 624: ifnull and nvl
*Beginner* Â· `ifnull`, `nvl`

Provide a default for a null column - the two-argument form of `coalesce`.

### Example 625: nvl2 for conditional defaults
*Intermediate* Â· `nvl2`

Return one value if a column is not null, and another if it is.

### Example 626: nullif to convert values to null
*Intermediate* Â· `nullif`

Convert specific values in a column to null, typically to clean out placeholder codes.

### Example 627: isnan versus isNull
*Intermediate* Â· `isnan`, `isNull`

Distinguish null from NaN in a float column.

### Example 628: Nulls compare as null with lit
*Advanced* Â· `lit`, `eqNullSafe`

Compare a column to a literal null value in a way that returns true for null rows.

### Example 629: Chained coalesce
*Intermediate* Â· `coalesce`, `chain`

Layer several fallbacks with a mix of column and literal sources.

### Example 630: na.drop with default settings
*Beginner* Â· `na.drop`

Drop rows that have any null values.

### Example 631: na.drop with how and thresh
*Intermediate* Â· `na.drop`

Drop rows where all values are null, or where fewer than N values are non-null.

### Example 632: na.drop with subset
*Intermediate* Â· `na.drop`

Apply the null check to specific columns only.

### Example 633: na.fill with a scalar
*Beginner* Â· `na.fill`

Fill all null values in matching-type columns with a scalar.

### Example 634: na.fill with per-column values
*Intermediate* Â· `na.fill`

Provide different default values for different columns.

### Example 635: na.replace for value swaps
*Intermediate* Â· `na.replace`

Replace specific values with other values, optionally scoped to particular columns.

### Example 636: na.fill in complex-typed columns
*Advanced* Â· `na.fill limitations`

See what `na.fill` can and cannot do with array, struct, and map columns.

### Example 637: Nulls in groupBy
*Intermediate* Â· `groupBy`

Confirm that null grouping keys form their own group.

### Example 638: Nulls in count
*Intermediate* Â· `count`

Distinguish `count(*)` from `count(column)` when nulls are present.

### Example 639: Nulls in sum and avg
*Intermediate* Â· `sum`, `avg`

Confirm that `sum` and `avg` skip null values rather than propagating them.

### Example 640: Nulls in join keys
*Intermediate* Â· `join`, `eqNullSafe`

Confirm that null-keyed rows drop from a standard equi-join, and stay with `eqNullSafe`.

### Example 641: Ordering with nulls first
*Beginner* Â· `asc_nulls_first`, `orderBy`

Sort a DataFrame so null-valued rows appear at the top.

### Example 642: Ordering with nulls last
*Beginner* Â· `asc_nulls_last`

Sort so null-valued rows appear at the bottom.

### Example 643: Multi-column ordering with nulls
*Intermediate* Â· `orderBy`

Sort by multiple columns where at least one is nullable.

### Example 644: distinct treats nulls as a single value
*Intermediate* Â· `distinct`

Confirm that `distinct()` treats multiple null values as one distinct value.

### Example 645: Union preserves duplicate nulls
*Intermediate* Â· `union`

See how `union` handles null values from both sides.

### Example 646: lag with default null
*Intermediate* Â· `lag`, `Window`

Confirm that `lag` on the first row of each partition returns null.

### Example 647: first and last with ignoreNulls
*Advanced* Â· `first`, `last`, `Window`

Use `first(..., ignorenulls=True)` in a window to forward-fill missing values.

### Example 648: Running aggregate over nulls
*Intermediate* Â· `sum`, `Window`

Confirm that running sums skip nulls the same way group-scoped sums do.

### Example 649: Nulls in row_number
*Intermediate* Â· `row_number`, `Window`

Confirm that `row_number` orders nulls consistently and does not skip them.

### Example 650: Null array versus empty array
*Intermediate* Â· `size`, `isNull`

Distinguish a null array from an empty array.

### Example 651: Null struct
*Intermediate* Â· `struct access on null`

Access a field on a null struct and see what happens.

### Example 652: Null map versus missing keys
*Intermediate* Â· `map_contains_key`

Distinguish a null map from a map that simply lacks a specific key.

### Example 653: Explode on null array drops the row
*Intermediate* Â· `explode`, `explode_outer`

Recall the row-loss behaviour of `explode` on null and empty arrays and use `explode_outer` to keep them.

### Example 654: Nested null propagation
*Advanced* Â· `nested struct access`

See how null propagates through several levels of struct nesting.

### Example 655: Count nulls per column
*Intermediate* Â· `sum`, `cast`

Report the null count for every column in a DataFrame.

### Example 656: Null percentage per column
*Intermediate* Â· `sum`, `cast`, `count`

Report the null percentage for every column.

### Example 657: Per-row null count
*Advanced* Â· `withColumn`, `sum`

Add a column with the count of null values per row.

### Example 658: Assert no nulls in required columns
*Advanced* Â· `assert`, `filter`

Fail loudly if a required column contains any null.

### Example 659: Combined data-quality report
*Advanced* Â· `aggregate`, `cast`

Report null count, non-null count, and null percentage for every column in one query.

### Example 660: Null checklist
*Intermediate* Â· `review`

Summarise the null rules across every operation.

---

â† [Back to main index](../../README.md)
