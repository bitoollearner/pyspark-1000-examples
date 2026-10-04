# Chapter 22: Real-World Patterns

**45 examples** (956â€“1000)

Difficulty mix: 8 Beginner Â· 24 Intermediate Â· 13 Advanced

[ðŸ“” Open the notebook](../../notebooks/22-patterns.ipynb) Â· [ðŸ“– Read the chapter on Kindle](https://www.amazon.com/dp/B0DXXXXXXX)

---

## Examples

### Example 956: Ingest with type coercion
*Beginner* Â· `ingestion`, `cast`

Ingest raw string data and coerce it to typed columns for a Delta target.

### Example 957: Handle schema drift on append
*Intermediate* Â· `mergeSchema`

Append data with an evolved schema without breaking the pipeline.

### Example 958: Dead letter pattern
*Intermediate* Â· `filter`, `split`

Route rows that fail validation to a separate table for later inspection.

### Example 959: Idempotent ingestion
*Advanced* Â· `MERGE`, `batch_id`

Ensure that re-running an ingestion job produces the same result.

### Example 960: Incremental via bookmark
*Intermediate* Â· `bookmark table`

Process only new data since the last successful run.

### Example 961: Union multiple sources
*Beginner* Â· `unionByName`

Combine data from multiple sources into a single stream.

### Example 962: Field cleaning during ingestion
*Intermediate* Â· `trim`, `lower`, `coalesce`

Normalise string fields during ingestion - trim whitespace, lowercase, substitute defaults for nulls.

### Example 963: Post-ingestion validation
*Intermediate* Â· `count`, `assert`

Validate the shape of ingested data before publishing it.

### Example 964: Exact-match deduplication
*Beginner* Â· `distinct`

Remove exact duplicate rows.

### Example 965: Latest-per-key deduplication
*Intermediate* Â· `row_number`, `Window`

For each key, keep only the most recent row.

### Example 966: Fuzzy deduplication via soundex
*Advanced* Â· `soundex`, `groupBy`

Group names that sound similar - a phonetic dedup for names with typos.

### Example 967: Priority-based deduplication
*Intermediate* Â· `Window with priority`

When the same key appears from multiple sources, prefer the higher-priority source.

### Example 968: Watermark filter
*Intermediate* Â· `watermark`

Reject events older than a watermark.

### Example 969: Reprocessing window
*Intermediate* Â· `rolling window`

Always reprocess the last N days to catch late-arriving data.

### Example 970: Detect out-of-order events
*Advanced* Â· `lag`, `filter`

Identify events whose timestamps are earlier than the previous arrival.

### Example 971: Backfill safety check
*Advanced* Â· `pre-check pattern`

Verify that backfilling data won't overwrite newer processing.

### Example 972: Bookmark update after processing
*Intermediate* Â· `bookmark`

Store the last processed timestamp reliably.

### Example 973: Detect new files
*Intermediate* Â· `set difference`

Identify files that haven't been processed yet.

### Example 974: Watermark-based incremental
*Advanced* Â· `timestamp bookmark`

Process events since the last watermark checkpoint.

### Example 975: CDF-driven incremental
*Advanced* Â· `Delta CDF incremental`

Read Delta CDF entries since the last processed version.

### Example 976: Iceberg incremental scan
*Advanced* Â· `Iceberg incremental read`

Read only rows added to an Iceberg table after a specific snapshot.

### Example 977: Row count assertion
*Beginner* Â· `count`, `assertion`

Assert that a DataFrame has a row count within an expected range.

### Example 978: Null count check
*Intermediate* Â· `null counts`

Count nulls per column and enforce a nullability contract.

### Example 979: Uniqueness check
*Intermediate* Â· `distinct count`

Assert that a key column is unique across all rows.

### Example 980: Referential integrity check
*Advanced* Â· `left_anti join`

Find rows in a fact table whose foreign key does not exist in the dimension table.

### Example 981: Range and domain check
*Intermediate* Â· `isin`, `filter`

Verify that values fall within a defined range or allowed set.

### Example 982: Sample-based test
*Intermediate* Â· `assertion on transformation`

Test that a transformation produces expected values on a small sample.

### Example 983: DataFrame content comparison
*Intermediate* Â· `exceptAll`

Compare two DataFrames for content equality.

### Example 984: Schema comparison
*Beginner* Â· `schema equality`

Compare two DataFrames for schema equality.

### Example 985: Fixture-based pipeline test
*Advanced* Â· `pipeline test structure`

Test a multi-step pipeline against known input and output fixtures.

### Example 986: Checkpoint state
*Intermediate* Â· `checkpoint pattern`

Save pipeline state to durable storage between runs.

### Example 987: Restart from checkpoint
*Intermediate* Â· `restart pattern`

Resume pipeline execution after a crash by reading the last checkpoint.

### Example 988: Restart-safe batch tracking
*Advanced* Â· `batch tracking`

Track completed batches so restart resumes at the right point.

### Example 989: Delta to Iceberg
*Intermediate* Â· `CTAS across formats`

Convert a Delta table to an Iceberg table.

### Example 990: Iceberg to Delta
*Intermediate* Â· `cross-format write`

Convert an Iceberg table to a Delta table.

### Example 991: Cross-format union
*Advanced* Â· `unionByName across formats`

Combine data from Delta and Iceberg sources into a single query.

### Example 992: Parameterized run
*Beginner* Â· `parameter`, `filter`

Accept a date parameter and process data for that specific date.

### Example 993: Config from environment
*Beginner* Â· `os.environ`

Read pipeline configuration from environment variables with sensible defaults.

### Example 994: Structured logging
*Intermediate* Â· `JSON logging`

Emit structured log entries that machines can parse and index.

### Example 995: Status file
*Intermediate* Â· `status file pattern`

Write a status file that orchestrators can check for run outcome.

### Example 996: Bronze layer
*Intermediate* Â· `bronze ingestion`

Ingest raw data into a bronze layer with minimal transformation.

### Example 997: Silver layer
*Advanced* Â· `silver cleaning`

Clean and deduplicate the bronze data into a silver layer.

### Example 998: Gold layer
*Intermediate* Â· `gold aggregation`

Compute business metrics from the silver data into a gold layer.

### Example 999: Monitoring wrapper
*Advanced* Â· `monitoring wrapper`

Wrap each pipeline step to log status, timing, and row counts.

### Example 1000: One thousand examples
*Beginner* Â· `review`

Reflect on the themes of the book.

---

â† [Back to main index](../../README.md)
