# Chapter 13: Pivoting

**25 examples** (591â€“615)

Difficulty mix: 3 Beginner Â· 9 Intermediate Â· 13 Advanced

[ðŸ“” Open the notebook](../../notebooks/13-pivoting.ipynb) Â· [ðŸ“– Read the chapter on Kindle](https://www.amazon.com/dp/B0DXXXXXXX)

---

## Examples

### Example 591: Pivot without a value list
*Beginner* Â· `pivot`

Turn distinct values of one column into new columns, one aggregate each.

### Example 592: Pivot with an explicit value list
*Beginner* Â· `pivot`

Pin the pivot output columns to a known set, avoiding the discovery scan.

### Example 593: Pivot with several aggregates
*Intermediate* Â· `pivot`, `agg`

Compute several statistics broken out by a pivot column.

### Example 594: Pivot on a numeric column
*Intermediate* Â· `pivot`

Pivot on integer values as if they were categorical.

### Example 595: Pivot on a derived column
*Intermediate* Â· `pivot`, `withColumn`

Pivot on a value not present in the source, computed on the fly.

### Example 596: Pivot with a null-safe pivot value
*Advanced* Â· `pivot`, `coalesce`

Handle null values in the pivot column so they become a named category rather than disappearing.

### Example 597: Pivot with a filter first
*Beginner* Â· `filter`, `pivot`

Pivot only the rows meeting a condition.

### Example 598: Pivot with a multi-column grouping key
*Intermediate* Â· `groupBy`, `pivot`

Group by more than one column, then pivot.

### Example 599: Rename pivot columns with cleaner labels
*Advanced* Â· `pivot`, `withColumnRenamed`

Give the pivot output columns readable labels for a report.

### Example 600: Pivot with a per-group total
*Advanced* Â· `pivot`, `groupBy`

Add a per-group total to the pivot output.

### Example 601: Pivot preserving the total
*Advanced* Â· `rollup`, `pivot`

Include grand totals in the pivot output using a rollup-style pattern.

### Example 602: Pivot to a wide table for a dashboard
*Intermediate* Â· `pivot`, `sum`

Produce a wide dashboard-friendly table from long-form input.

### Example 603: Multiple aggregates with clean output
*Advanced* Â· `pivot`, `agg`, `alias`

Produce a pivot with multiple aggregates and a manageable output shape.

### Example 604: Pivot cardinality check
*Advanced* Â· `distinct`, `pivot`

Verify that a pivot would produce a manageable number of columns before running it.

### Example 605: Pivot on a nested field
*Advanced* Â· `pivot`, `dot notation`

Pivot on a field inside a struct column.

### Example 606: Unpivot with stack
*Intermediate* Â· `stack`, `selectExpr`

Convert wide-form columns back into rows - the inverse of pivot.

### Example 607: Unpivot programmatically
*Advanced* Â· `stack`, `generated`

Unpivot a variable number of columns.

### Example 608: Unpivot with a value list
*Advanced* Â· `stack`, `unpivot alias`

Unpivot only some columns, keeping the rest as identifiers.

### Example 609: Round-trip pivot and unpivot
*Intermediate* Â· `pivot`, `stack`

Confirm that pivot and unpivot are inverses on the same data.

### Example 610: Pivot then flatten
*Advanced* Â· `pivot`, `select`

Produce a wide pivot output and immediately flatten to specific column subset.

### Example 611: Pivot from a nested struct source
*Advanced* Â· `dot notation`, `pivot`

Pivot on values inside a struct column, on a per-row basis.

### Example 612: Pivot with a fill value
*Intermediate* Â· `pivot`, `fillna`

Replace null cells in pivot output with a default.

### Example 613: Pivot join back to source
*Advanced* Â· `pivot`, `join`

Combine a pivot summary with the source rows for a comparison report.

### Example 614: Pivot in Spark versus in the consumer
*Advanced* Â· `groupBy`, `comparison`

Compare pivoting in Spark against sending long-format data and letting the consumer pivot.

### Example 615: Pivot checklist
*Intermediate* Â· `review`

Summarise the decisions a pivot makes.

---

â† [Back to main index](../../README.md)
