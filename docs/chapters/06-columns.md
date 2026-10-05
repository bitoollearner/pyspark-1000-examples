# Chapter 6: Column Operations

**60 examples** (241-300)

Difficulty mix: 14 Advanced . 15 Beginner . 31 Intermediate

[Open the practice notebook](../../notebooks/06-columns.ipynb) . [Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 241: Four ways to name a column
*Beginner* . `col, select`

Select the same column using each of the notations PySpark accepts, and confirm

### Example 242: When attribute access breaks
*Intermediate* . `col`

Find the column names that `df.name` cannot reach.

### Example 243: Bind a column to a specific DataFrame
*Intermediate* . `alias, col`

Distinguish two columns with the same name coming from different DataFrames.

### Example 244: Reference a column that does not exist
*Beginner* . `col`

See when and how Spark reports an unknown column name.

### Example 245: Handle names with spaces
*Intermediate* . `col, expr, backticks`

Work with a column whose name contains a space.

### Example 246: Build a column before you have a DataFrame
*Intermediate* . `col`

Define a reusable expression independently, then apply it.

### Example 247: Compute with arithmetic operators
*Beginner* . `arithmetic operators`

Derive numeric columns using ordinary Python operators.

### Example 248: Compare values
*Beginner* . `comparison operators`

Build boolean columns from comparisons, and see what a comparison produces.

### Example 249: Combine conditions
*Intermediate* . `&, |, ~`

Build a compound condition, and get the parentheses right.

### Example 250: Why `and` does not work
*Intermediate* . `&`

Understand why Python's boolean keywords cannot be used on columns.

### Example 251: Add a literal value
*Beginner* . `lit`

Use a constant in an expression where Spark expects a column.

### Example 252: Compare safely against null
*Advanced* . `eqNullSafe`

Compare two values where both may be null, treating two nulls as equal.

### Example 253: Test membership in a set
*Beginner* . `isin`

Match a column against several candidate values.

### Example 254: Test a range
*Beginner* . `between`

Select rows whose value falls within inclusive bounds.

### Example 255: Test for null
*Beginner* . `isNull, isNotNull`

Identify missing values, which comparison operators cannot do.

### Example 256: Rename with alias
*Beginner* . `alias`

Give a computed column a sensible name.

### Example 257: Reach into a struct
*Intermediate* . `dot notation, getField`

Read fields from a nested struct column.

### Example 258: Index into an array
*Intermediate* . `getItem, element_at, size`

Read a specific element from an array column.

### Example 259: Look up a map value
*Intermediate* . `getItem, map_keys`

Read a value from a map column by key.

### Example 260: Sort with explicit direction
*Beginner* . `asc, desc`

Attach a sort direction to a column expression rather than to the sort call.

### Example 261: Chain several conditions
*Beginner* . `when, otherwise`

Assign a category from a numeric value using more than two bands.

### Example 262: Nest one condition inside another
*Intermediate* . `when, otherwise`

Apply different bands depending on a second column.

### Example 263: Leave out otherwise
*Beginner* . `when`

See what happens to rows matching no condition when there is no fallback.

### Example 264: Fold a condition chain out of a mapping
*Advanced* . `when, reduce`

Generate a `when` chain from rules held in a dictionary rather than written out.

### Example 265: Generate the same chain readably
*Advanced* . `when, reduce`

Build the same chain with an explicit loop, and decide which form belongs in a

### Example 266: Take the first non-null value
*Beginner* . `coalesce`

Fall back through several columns to whichever has a value.

### Example 267: Turn a sentinel into null
*Intermediate* . `when, otherwise`

Convert a placeholder value into a real null.

### Example 268: Supply a default for a nullable column
*Beginner* . `coalesce, lit`

Replace nulls with a fixed value so arithmetic does not propagate them.

### Example 269: Combine several nullable columns
*Intermediate* . `coalesce, when`

Produce a single value from several partially populated columns, recording which

### Example 270: Test a condition against a nullable column
*Intermediate* . `when, isNull`

Handle nulls explicitly in a conditional rather than letting them fall through.

### Example 271: Build a select list from a list of names
*Intermediate* . `select`

Choose columns at runtime rather than writing them into the code.

### Example 272: Transform every column of a type
*Intermediate* . `dtypes, trim`

Apply the same cleaning to all string columns without naming them.

### Example 273: Rename columns from a mapping
*Intermediate* . `select, alias`

Apply a set of renames defined as data.

### Example 274: Prefix every column name
*Intermediate* . `select, alias`

Namespace a DataFrame's columns before combining it with another.

### Example 275: Add missing columns as null
*Advanced* . `lit, cast`

Conform a DataFrame to a contract, filling in columns it does not have.

### Example 276: Drop columns by pattern
*Intermediate* . `drop`

Remove every column whose name matches a rule.

### Example 277: Reuse an expression across DataFrames
*Intermediate* . `col`

Apply one business rule to two different DataFrames.

### Example 278: Keep expressions in a registry
*Advanced* . `dict of Columns`

Centralise derived columns so several jobs compute them identically.

### Example 279: Write a function returning a column
*Intermediate* . `function composition`

Parameterise an expression so one definition covers several thresholds.

### Example 280: Test an expression in isolation
*Advanced* . `createDataFrame, collect`

Verify a column expression against known inputs without involving a pipeline.

### Example 281: Build a struct column
*Intermediate* . `struct`

Group several columns into one nested value.

### Example 282: Build an array column
*Intermediate* . `array, array_contains`

Combine several columns into a list, and test its contents.

### Example 283: Build a map column
*Advanced* . `create_map, lit`

Construct key-value pairs from existing columns.

### Example 284: Expand a struct back into columns
*Intermediate* . `select with star`

Flatten a struct into top-level columns without naming each field.

### Example 285: Write an expression in SQL
*Intermediate* . `expr`

Use SQL syntax for a column expression inside a DataFrame chain.

### Example 286: Use selectExpr for several expressions
*Beginner* . `selectExpr`

Write a projection entirely in SQL.

### Example 287: Read and set column metadata
*Advanced* . `alias with metadata`

Attach machine-readable annotations to a column and read them back.

### Example 288: Take the greatest of several columns
*Intermediate* . `greatest, least`

Compare values across columns within a row rather than down a column.

### Example 289: Handle duplicate column names
*Advanced* . `toDF, alias`

Work with a DataFrame that has two columns of the same name.

### Example 290: Control case sensitivity
*Advanced* . `spark.sql.caseSensitive`

Determine whether `SALARY` resolves to a column named `salary`.

### Example 291: Know that when does not short-circuit
*Advanced* . `when`

Understand whether a later `when` branch is evaluated when an earlier one

### Example 292: Build a surrogate key with hash
*Advanced* . `hash, xxhash64`

Derive a stable identifier from several columns.

### Example 293: Concatenate into a composite key
*Intermediate* . `concat_ws`

Build a readable key from several columns, handling nulls.

### Example 294: Compare whole rows
*Advanced* . `struct, eqNullSafe`

Detect whether two versions of a row differ across every column at once.

### Example 295: Add a reproducible random column
*Intermediate* . `rand`

Assign random values that are the same on every run.

### Example 296: Cast inside an expression chain
*Intermediate* . `cast`

Change a type partway through a computation rather than beforehand.

### Example 297: Use one expression in filter and select
*Intermediate* . `col reuse`

Apply the same condition as a filter and as a visible column.

### Example 298: Count how many conditions a row satisfies
*Advanced* . `cast, arithmetic`

Score each row by how many rules it meets.

### Example 299: Inspect an expression
*Intermediate* . `print on a Column`

See what an expression is before applying it to data.

### Example 300: Review the column checklist
*Intermediate* . `review`

Summarise the decisions and traps this chapter has covered.
