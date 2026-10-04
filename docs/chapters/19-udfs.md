# Chapter 19: User-Defined Functions

**25 examples** (836â€“860)

Difficulty mix: 4 Beginner Â· 11 Intermediate Â· 10 Advanced

[ðŸ“” Open the notebook](../../notebooks/19-udfs.ipynb) Â· [ðŸ“– Read the chapter on Kindle](https://www.amazon.com/dp/B0DXXXXXXX)

---

## Examples

### Example 836: Simple Python UDF
*Beginner* Â· `F.udf`

Wrap a Python function as a Spark UDF and apply it to a column.

### Example 837: UDF with multiple arguments
*Beginner* Â· `F.udf`, `multi-arg`

Create a UDF that computes from several columns.

### Example 838: UDF via decorator
*Beginner* Â· `@F.udf`

Define a UDF using the decorator syntax.

### Example 839: Return type inference caveat
*Intermediate* Â· `UDF return types`

See what happens when the return type is not specified.

### Example 840: UDF returning an array
*Intermediate* Â· `ArrayType return`

Create a UDF that returns a list of values.

### Example 841: Register UDF for SQL
*Intermediate* Â· `spark.udf.register`

Register a UDF so it is callable from SQL strings.

### Example 842: Registered UDF in selectExpr
*Intermediate* Â· `selectExpr`

Use a registered UDF in `selectExpr` for concise SQL-like syntax.

### Example 843: Nulls propagate through UDFs
*Beginner* Â· `null handling`

Confirm that null inputs to a UDF arrive as Python None.

### Example 844: Null-safe wrapper
*Intermediate* Â· `null guard`

Wrap a function that does not handle nulls in a UDF that does.

### Example 845: UDF returning a struct
*Advanced* Â· `StructType return`

Return several values from a UDF as one struct column.

### Example 846: UDF returning a map
*Advanced* Â· `MapType return`

Return a dictionary-like structure from a UDF.

### Example 847: UDF taking array input
*Advanced* Â· `array input`

Create a UDF that receives an array column and processes it.

### Example 848: Scalar Pandas UDF
*Intermediate* Â· `pandas_udf`

Use a Pandas UDF for vectorised transformation.

### Example 849: Grouped map with applyInPandas
*Advanced* Â· `applyInPandas`

Apply a Pandas function per group, returning a per-group DataFrame.

### Example 850: Grouped aggregate Pandas UDF
*Advanced* Â· `pandas_udf`, `groupBy`

Create a Pandas UDF that computes a per-group aggregate.

### Example 851: Iterator Pandas UDF
*Advanced* Â· `iterator UDF`

Use the iterator form of Pandas UDF for expensive per-executor setup.

### Example 852: Multi-column Pandas UDF
*Intermediate* Â· `pandas_udf`, `multi-arg`

Create a Pandas UDF that takes several columns and returns one column.

### Example 853: Scalar Pandas UDF returning struct
*Advanced* Â· `pandas_udf`, `struct return`

Return multiple derived values per row from a Pandas UDF as a struct.

### Example 854: Built-in versus Python UDF
*Intermediate* Â· `performance`

Show that a built-in and its Python UDF equivalent produce identical results.

### Example 855: Python UDF versus Pandas UDF
*Intermediate* Â· `performance`

Show that a Python UDF and a Pandas UDF produce identical results.

### Example 856: Reformulate a UDF as built-ins
*Intermediate* Â· `built-in alternatives`

Rewrite a common UDF pattern using only built-in functions.

### Example 857: Broadcast large closures
*Advanced* Â· `broadcast`

Use a large lookup table in a UDF without shipping it with every task.

### Example 858: UDFs and function purity
*Advanced* Â· `purity`, `side effects`

Understand that UDFs can be called more times than the row count suggests.

### Example 859: Business logic UDF pattern
*Advanced* Â· `real-world`

Encode a piece of business logic as a UDF for readability.

### Example 860: UDF checklist
*Intermediate* Â· `review`

Summarise the decisions UDF code makes.

---

â† [Back to main index](../../README.md)
