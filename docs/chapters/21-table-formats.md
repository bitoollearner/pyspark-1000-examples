# Chapter 21: Table Formats and Change Data

**55 examples** (901â€“955)

Difficulty mix: 14 Beginner Â· 21 Intermediate Â· 20 Advanced

[ðŸ“” Open the notebook](../../notebooks/21-table-formats.ipynb) Â· [ðŸ“– Read the chapter on Kindle](https://www.amazon.com/dp/B0DXXXXXXX)

---

## Examples

### Example 901: Create a Delta table
*Beginner* Â· `write.format("delta")`

Create a Delta table from a DataFrame at a given file path.

### Example 902: Read a Delta table
*Beginner* Â· `read.format("delta")`

Read a Delta table by path with typed schema preserved.

### Example 903: Append to a Delta table
*Beginner* Â· `mode("append")`

Add rows to an existing Delta table.

### Example 904: Overwrite a Delta table
*Beginner* Â· `mode("overwrite")`

Replace the contents of a Delta table.

### Example 905: Update rows in a Delta table
*Intermediate* Â· `DeltaTable.update`

Change values in existing rows matching a condition.

### Example 906: Delete rows from a Delta table
*Intermediate* Â· `DeltaTable.delete`

Remove rows matching a condition.

### Example 907: Merge (upsert) into Delta
*Advanced* Â· `DeltaTable.merge`

Insert new rows or update existing ones based on a key match.

### Example 908: Show table history
*Beginner* Â· `DeltaTable.history`

List the versions of a Delta table and the operations that produced them.

### Example 909: Get current version
*Beginner* Â· `history`, `max`

Read the current version number of a Delta table.

### Example 910: Describe table detail
*Intermediate* Â· `DESCRIBE DETAIL`

Inspect a Delta table's storage layout, file count, and size.

### Example 911: Create an Iceberg table
*Beginner* Â· `CREATE TABLE`, `ICEBERG`

Create an Iceberg table via SQL and populate it.

### Example 912: Read an Iceberg table
*Beginner* Â· `spark.table`

Read an Iceberg table with types preserved.

### Example 913: Append to an Iceberg table
*Beginner* Â· `INSERT INTO`

Add rows to an existing Iceberg table.

### Example 914: Overwrite an Iceberg table
*Beginner* Â· `INSERT OVERWRITE`

Replace the contents of an Iceberg table.

### Example 915: Update rows in an Iceberg table
*Intermediate* Â· `UPDATE`

Change values in existing rows matching a condition.

### Example 916: Delete from an Iceberg table
*Intermediate* Â· `DELETE FROM`

Remove rows matching a condition.

### Example 917: MERGE into an Iceberg table
*Advanced* Â· `MERGE INTO`

Insert new rows or update existing ones based on a key match, using SQL MERGE.

### Example 918: Show snapshots
*Intermediate* Â· `.snapshots metadata table`

List an Iceberg table's snapshots and their operations.

### Example 919: Inspect snapshot operations
*Advanced* Â· `snapshots metadata`

See the operation type for each snapshot in an Iceberg table.

### Example 920: Count files in an Iceberg table
*Advanced* Â· `.files metadata`

Count the data files backing an Iceberg table.

### Example 921: Read Delta at a specific version
*Intermediate* Â· `versionAsOf`

Read a Delta table as it existed at a specific version.

### Example 922: Read Delta at a specific timestamp
*Intermediate* Â· `timestampAsOf`

Read a Delta table as it existed at a specific timestamp.

### Example 923: Restore Delta to a previous version
*Advanced* Â· `RESTORE TABLE`

Roll a Delta table back to a previous version.

### Example 924: VACUUM to remove old files
*Advanced* Â· `VACUUM`

Reclaim storage by removing files no longer needed for time travel.

### Example 925: Read Iceberg at a specific snapshot
*Intermediate* Â· `snapshot-id option`

Read an Iceberg table at a specific snapshot.

### Example 926: Read Iceberg at a specific timestamp
*Intermediate* Â· `as-of-timestamp`

Read an Iceberg table as of a specific timestamp.

### Example 927: Rollback Iceberg to a snapshot
*Advanced* Â· `rollback_to_snapshot`

Undo recent changes to an Iceberg table by rolling back to a snapshot.

### Example 928: Compare versions before and after a change
*Advanced* Â· `time travel`, `join`

Compute the difference between two versions of a table.

### Example 929: Add column to Delta with mergeSchema
*Intermediate* Â· `mergeSchema`

Append data with an additional column, adding it to the table schema.

### Example 930: Add column to Iceberg
*Beginner* Â· `ALTER TABLE ADD COLUMN`

Add a new column to an Iceberg table via ALTER TABLE.

### Example 931: Rename column in Delta
*Advanced* Â· `RENAME COLUMN`, `column mapping`

Rename a column in a Delta table using column mapping.

### Example 932: Rename column in Iceberg
*Beginner* Â· `ALTER TABLE RENAME COLUMN`

Rename a column in an Iceberg table.

### Example 933: Drop a column
*Intermediate* Â· `DROP COLUMN`

Drop a column from an Iceberg table.

### Example 934: Change column type (widening)
*Advanced* Â· `ALTER COLUMN TYPE`

Change an Iceberg column's type to a wider compatible type.

### Example 935: Enable CDF on a new Delta table
*Intermediate* Â· `enableChangeDataFeed`

Create a Delta table with Change Data Feed enabled.

### Example 936: Enable CDF on an existing Delta table
*Intermediate* Â· `ALTER TABLE SET TBLPROPERTIES`

Enable CDF on a Delta table that was created without it.

### Example 937: Read Change Data Feed for a version range
*Advanced* Â· `readChangeFeed`

Read the change events between two versions of a Delta table.

### Example 938: Show change types
*Advanced* Â· `_change_type`

Show the distribution of change types from CDF output.

### Example 939: Filter CDF by change type
*Advanced* Â· `_change_type filter`

Read only the logically-current-state records (inserts, updates, deletes) from CDF, ignoring the pre-update snapshots.

### Example 940: CDF combined with MERGE
*Advanced* Â· `CDF`, `MERGE`, `downstream sync`

Apply CDF changes from a source Delta table into a target Delta table via MERGE.

### Example 941: SCD Type 1 with UPDATE
*Intermediate* Â· `DeltaTable.update`

Implement SCD Type 1 - overwrite the current value with no history.

### Example 942: SCD Type 1 via MERGE
*Intermediate* Â· `MERGE`, `upsert`

Apply a batch of changes as SCD Type 1 using MERGE.

### Example 943: Bulk SCD Type 1
*Advanced* Â· `MERGE with condition`

Only update rows where a value has actually changed.

### Example 944: SCD Type 2 schema
*Intermediate* Â· `schema design`

Design the schema for an SCD Type 2 table.

### Example 945: SCD Type 2 initial load
*Intermediate* Â· `SCD Type 2 write`

Perform the initial load of an SCD Type 2 dimension.

### Example 946: SCD Type 2 first change
*Advanced* Â· `close-and-insert`

Record an attribute change as an SCD Type 2 versioned update.

### Example 947: SCD Type 2 via MERGE
*Advanced* Â· `MERGE for SCD Type 2`

Apply a batch of SCD Type 2 updates using MERGE plus append.

### Example 948: Point-in-time query on SCD Type 2
*Advanced* Â· `date range filter`

Query the SCD Type 2 table for the state on a specific date.

### Example 949: Delta versus Iceberg feature matrix
*Beginner* Â· `comparison`

Compare Delta Lake and Iceberg features side by side.

### Example 950: Convert Parquet to Delta
*Intermediate* Â· `CONVERT TO DELTA`

Upgrade an existing Parquet dataset to a Delta table in place.

### Example 951: Convert Parquet to Iceberg via CTAS
*Intermediate* Â· `CREATE TABLE AS SELECT`

Create an Iceberg table from an existing Parquet dataset.

### Example 952: Format decision guide
*Beginner* Â· `decision matrix`

Guidelines for choosing between plain Parquet, Delta, and Iceberg.

### Example 953: Interop pitfalls
*Advanced* Â· `pitfall reference`

Enumerate the common interop mistakes with transactional formats.

### Example 954: Compaction with OPTIMIZE
*Advanced* Â· `OPTIMIZE`

Compact many small files into fewer larger ones.

### Example 955: Table formats checklist
*Intermediate* Â· `review`

Summarise the decisions transactional-table code makes.

---

â† [Back to main index](../../README.md)
