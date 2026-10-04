# Chapter 2: Spark Session Management

**30 examples** (21–50)

Difficulty mix: 11 Beginner · 18 Intermediate · 1 Advanced

[📔 Open the notebook](../../notebooks/02-session.ipynb) · [📖 Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 21: Create a SparkSession the canonical way
*Beginner* · `SparkSession.builder`, `appName`, `master`, `getOrCreate`

Write the session-creation block that belongs at the top of a standalone PySpark script.

### Example 22: getOrCreate returns the session you already have
*Beginner* · `getOrCreate`, `getActiveSession`

Establish whether calling the builder twice produces two sessions.

### Example 23: Give your application a findable name
*Beginner* · `appName`

A cluster is running forty jobs. Make yours identifiable at a glance.

### Example 24: Configuration set after the session exists cannot reach the JVM
*Intermediate* · `config`, `getOrCreate`

Understand why a `.config()` call on the builder sometimes has no effect at all.

### Example 25: Tell static configuration from runtime-mutable
*Intermediate* · `spark.conf.set`, `spark.conf.get`

Determine which settings you can still change from inside a running session.

### Example 26: Change a setting for one query, then restore it
*Intermediate* · `spark.conf.set`, `spark.conf.get`

One aggregation needs a different shuffle width, without affecting anything else in the session.

### Example 27: Reset a setting to its default
*Intermediate* · `spark.conf.unset`

Undo a configuration change without knowing what the original value was.

### Example 28: Isolate work with newSession()
*Intermediate* · `newSession`

Run work that registers temporary views without those views colliding with another part of your application.

### Example 29: Register a DataFrame as a temporary view
*Beginner* · `createOrReplaceTempView`

Make a DataFrame queryable with SQL.

### Example 30: Mix SQL and the DataFrame API
*Intermediate* · `sql`, `createOrReplaceTempView`, `filter`

Express one step in SQL because it reads better there, and the rest in the DataFrame API.

### Example 31: Share a view across sessions
*Advanced* · `createOrReplaceGlobalTempView`

Make a view visible to every session in the application, not just the one that created it.

### Example 32: Inspect what is in the catalog
*Intermediate* · `spark.catalog.listTables`, `currentDatabase`

Find out which views and tables the current session can see.

### Example 33: Drop a view when you are finished
*Beginner* · `dropTempView`, `tableExists`

Remove a temporary view and confirm it is gone.

### Example 34: Control how much Spark logs
*Beginner* · `setLogLevel`

Spark's default logging buries your own output. Turn it down.

### Example 35: Reach the SparkContext underneath
*Intermediate* · `sparkContext`

Access the lower-level entry point that predates `SparkSession`.

### Example 36: Isolate work with newSession()
*Intermediate* · `newSession`, `sparkContext`

Run work that needs its own temporary views and its own SQL configuration, without disturbing the session everything ...

### Example 37: Register a Python function for use in SQL
*Intermediate* · `spark.udf.register`

You have a Python function encoding business logic and you want to call it from a SQL query.

### Example 38: Create a view with SQL rather than the API
*Beginner* · `spark.sql`, `CREATE TEMPORARY VIEW`

Define a derived view entirely in SQL, for a codebase whose logic lives in `.sql` files.

### Example 39: Cache a view through the catalog
*Intermediate* · `spark.catalog.cacheTable`, `isCached`

A view is referenced several times in one job. Compute it once and keep the result in memory.

### Example 40: Release cached memory
*Intermediate* · `uncacheTable`, `clearCache`

Free memory held by a cached view once the job no longer needs it.

### Example 41: Drop a temporary view
*Beginner* · `dropTempView`, `dropGlobalTempView`

Remove a registered view when the work that needed it is finished.

### Example 42: Check a table exists before querying it
*Beginner* · `spark.catalog.tableExists`

Write code that adapts to whether a table is present, without relying on exception handling.

### Example 43: Find and change the current database
*Intermediate* · `currentDatabase`, `setCurrentDatabase`

Determine which database unqualified table names resolve against.

### Example 44: See the session timezone change a result
*Intermediate* · `spark.conf.set`, `to_timestamp`

Demonstrate that the session timezone changes how timestamps are rendered, and restore the original setting.

### Example 45: Toggle Adaptive Query Execution
*Intermediate* · `spark.conf.set`

Turn AQE on and off, and understand why a book pins it off.

### Example 46: Report the versions in play
*Beginner* · `spark.version`, `sys.version_info`

Produce a one-line environment report for a bug report or job log.

### Example 47: Discover the functions Spark knows
*Intermediate* · `spark.catalog.listFunctions`

Check whether a function exists before writing a query around it.

### Example 48: Inspect a table's columns from the catalog
*Intermediate* · `spark.catalog.listColumns`

Read a registered view's schema through the catalog rather than the DataFrame.

### Example 49: Write a reusable session factory
*Intermediate* · `SparkSession.builder`, `getOrCreate`

Give a codebase one place where sessions are created, so tests and production share configuration without duplicating...

### Example 50: Shut a session down safely
*Beginner* · `SparkSession.getActiveSession`, `stop`

Release Spark's resources at the end of a script without stranding them on failure.

---

← [Back to main index](../../README.md)
