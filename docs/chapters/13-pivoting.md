# Chapter 13: Pivoting

**25 examples** (591-615)

Difficulty mix: 13 Advanced . 3 Beginner . 9 Intermediate

[Open the practice notebook](../../notebooks/13-pivoting.ipynb) . [Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 591: Pivot without a value list
*Beginner* . `pivot`

Turn distinct values of one column into new columns, one aggregate each.

### Example 592: Pivot with an explicit value list
*Beginner* . `pivot`

Pin the pivot output columns to a known set, avoiding the discovery

### Example 593: Pivot with several aggregates
*Intermediate* . `pivot, agg`

Compute several statistics broken out by a pivot column.

### Example 594: Pivot on a numeric column
*Intermediate* . `pivot`

Pivot on integer values as if they were categorical.

### Example 595: Pivot on a derived column
*Intermediate* . `pivot, withColumn`

Pivot on a value not present in the source, computed on the fly.

### Example 596: Pivot with a null-safe pivot value
*Advanced* . `pivot, coalesce`

Handle null values in the pivot column so they become a named category

### Example 597: Pivot with a filter first
*Beginner* . `filter, pivot`

Pivot only the rows meeting a condition.

### Example 598: Pivot with a multi-column grouping key
*Intermediate* . `groupBy, pivot`

Group by more than one column, then pivot.

### Example 599: Rename pivot columns with cleaner labels
*Advanced* . `pivot, withColumnRenamed`

Give the pivot output columns readable labels for a report.

### Example 600: Pivot with a per-group total
*Advanced* . `pivot, groupBy`

Add a per-group total to the pivot output.

### Example 601: Pivot preserving the total
*Advanced* . `rollup, pivot`

Include grand totals in the pivot output using a rollup-style pattern.

### Example 602: Pivot to a wide table for a dashboard
*Intermediate* . `pivot, sum`

Produce a wide dashboard-friendly table from long-form input.

### Example 603: Multiple aggregates with clean output
*Advanced* . `pivot, agg, alias`

Produce a pivot with multiple aggregates and a manageable output shape.

### Example 604: Pivot cardinality check
*Advanced* . `distinct, pivot`

Verify that a pivot would produce a manageable number of columns before

### Example 605: Pivot on a nested field
*Advanced* . `pivot, dot notation`

Pivot on a field inside a struct column.

### Example 606: Unpivot with stack
*Intermediate* . `stack, selectExpr`

Convert wide-form columns back into rows - the inverse of pivot.

### Example 607: Unpivot programmatically
*Advanced* . `stack, generated`

Unpivot a variable number of columns.

### Example 608: Unpivot with a value list
*Advanced* . `stack, unpivot alias`

Unpivot only some columns, keeping the rest as identifiers.

### Example 609: Round-trip pivot and unpivot
*Intermediate* . `pivot, stack`

Confirm that pivot and unpivot are inverses on the same data.

### Example 610: Pivot then flatten
*Advanced* . `pivot, select`

Produce a wide pivot output and immediately flatten to specific column

### Example 611: Pivot from a nested struct source
*Advanced* . `dot notation, pivot`

Pivot on values inside a struct column, on a per-row basis.

### Example 612: Pivot with a fill value
*Intermediate* . `pivot, fillna`

Replace null cells in pivot output with a default.

### Example 613: Pivot join back to source
*Advanced* . `pivot, join`

Combine a pivot summary with the source rows for a comparison report.

### Example 614: Pivot in Spark versus in the consumer
*Advanced* . `groupBy, comparison`

Compare pivoting in Spark against sending long-format data and letting

### Example 615: Pivot checklist
*Intermediate* . `review`

Summarise the decisions a pivot makes.
