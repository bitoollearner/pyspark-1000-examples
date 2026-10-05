# Chapter 22: Real-World Patterns

**45 examples** (956-1000)

Difficulty mix: 13 Advanced . 8 Beginner . 24 Intermediate

[Open the practice notebook](../../notebooks/22-patterns.ipynb) . [Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 956: Ingest with type coercion
*Beginner* . `ingestion, cast`

Ingest raw string data and coerce it to typed columns for a Delta

### Example 957: Handle schema drift on append
*Intermediate* . `mergeSchema`

Append data with an evolved schema without breaking the pipeline.

### Example 958: Dead letter pattern
*Intermediate* . `filter, split`

Route rows that fail validation to a separate table for later

### Example 959: Idempotent ingestion
*Advanced* . `MERGE, batch_id`

Ensure that re-running an ingestion job produces the same result.

### Example 960: Incremental via bookmark
*Intermediate* . `bookmark table`

Process only new data since the last successful run.

### Example 961: Union multiple sources
*Beginner* . `unionByName`

Combine data from multiple sources into a single stream.

### Example 962: Field cleaning during ingestion
*Intermediate* . `trim, lower, coalesce`

Normalise string fields during ingestion - trim whitespace, lowercase,

### Example 963: Post-ingestion validation
*Intermediate* . `count, assert`

Validate the shape of ingested data before publishing it.

### Example 964: Exact-match deduplication
*Beginner* . `distinct`

Remove exact duplicate rows.

### Example 965: Latest-per-key deduplication
*Intermediate* . `row_number, Window`

For each key, keep only the most recent row.

### Example 966: Fuzzy deduplication via soundex
*Advanced* . `soundex, groupBy`

Group names that sound similar - a phonetic dedup for names with

### Example 967: Priority-based deduplication
*Intermediate* . `Window with priority`

When the same key appears from multiple sources, prefer the

### Example 968: Watermark filter
*Intermediate* . `watermark`

Reject events older than a watermark.

### Example 969: Reprocessing window
*Intermediate* . `rolling window`

Always reprocess the last N days to catch late-arriving data.

### Example 970: Detect out-of-order events
*Advanced* . `lag, filter`

Identify events whose timestamps are earlier than the previous

### Example 971: Backfill safety check
*Advanced* . `pre-check pattern`

Verify that backfilling data won't overwrite newer processing.

### Example 972: Bookmark update after processing
*Intermediate* . `bookmark`

Store the last processed timestamp reliably.

### Example 973: Detect new files
*Intermediate* . `set difference`

Identify files that haven't been processed yet.

### Example 974: Watermark-based incremental
*Advanced* . `timestamp bookmark`

Process events since the last watermark checkpoint.

### Example 975: CDF-driven incremental
*Advanced* . `Delta CDF incremental`

Read Delta CDF entries since the last processed version.

### Example 976: Iceberg incremental scan
*Advanced* . `Iceberg incremental read`

Read only rows added to an Iceberg table after a specific snapshot.

### Example 977: Row count assertion
*Beginner* . `count, assertion`

Assert that a DataFrame has a row count within an expected range.

### Example 978: Null count check
*Intermediate* . `null counts`

Count nulls per column and enforce a nullability contract.

### Example 979: Uniqueness check
*Intermediate* . `distinct count`

Assert that a key column is unique across all rows.

### Example 980: Referential integrity check
*Advanced* . `left_anti join`

Find rows in a fact table whose foreign key does not exist in the

### Example 981: Range and domain check
*Intermediate* . `isin, filter`

Verify that values fall within a defined range or allowed set.

### Example 982: Sample-based test
*Intermediate* . `assertion on transformation`

Test that a transformation produces expected values on a small

### Example 983: DataFrame content comparison
*Intermediate* . `exceptAll`

Compare two DataFrames for content equality.

### Example 984: Schema comparison
*Beginner* . `schema equality`

Compare two DataFrames for schema equality.

### Example 985: Fixture-based pipeline test
*Advanced* . `pipeline test structure`

Test a multi-step pipeline against known input and output fixtures.

### Example 986: Checkpoint state
*Intermediate* . `checkpoint pattern`

Save pipeline state to durable storage between runs.

### Example 987: Restart from checkpoint
*Intermediate* . `restart pattern`

Resume pipeline execution after a crash by reading the last

### Example 988: Restart-safe batch tracking
*Advanced* . `batch tracking`

Track completed batches so restart resumes at the right point.

### Example 989: Delta to Iceberg
*Intermediate* . `CTAS across formats`

Convert a Delta table to an Iceberg table.

### Example 990: Iceberg to Delta
*Intermediate* . `cross-format write`

Convert an Iceberg table to a Delta table.

### Example 991: Cross-format union
*Advanced* . `unionByName across formats`

Combine data from Delta and Iceberg sources into a single query.

### Example 992: Parameterized run
*Beginner* . `parameter, filter`

Accept a date parameter and process data for that specific date.

### Example 993: Config from environment
*Beginner* . `os.environ`

Read pipeline configuration from environment variables with

### Example 994: Structured logging
*Intermediate* . `JSON logging`

Emit structured log entries that machines can parse and index.

### Example 995: Status file
*Intermediate* . `status file pattern`

Write a status file that orchestrators can check for run outcome.

### Example 996: Bronze layer
*Intermediate* . `bronze ingestion`

Ingest raw data into a bronze layer with minimal transformation.

### Example 997: Silver layer
*Advanced* . `silver cleaning`

Clean and deduplicate the bronze data into a silver layer.

### Example 998: Gold layer
*Intermediate* . `gold aggregation`

Compute business metrics from the silver data into a gold layer.

### Example 999: Monitoring wrapper
*Advanced* . `monitoring wrapper`

Wrap each pipeline step to log status, timing, and row counts.

### Example 1000: One thousand examples
*Beginner* . `review`

Reflect on the themes of the book.
