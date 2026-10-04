# Chapter 4: Reading Files

**60 examples** (131–190)

Difficulty mix: 14 Beginner · 29 Intermediate · 17 Advanced

[📔 Open the notebook](../../notebooks/04-reading-files.ipynb) · [📖 Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 131: Read a CSV with a header
*Beginner* · `read.csv`, `option`

Load a comma-separated file whose first line names the columns, and get usable types rather than strings.

### Example 132: Read a CSV with an explicit schema
*Intermediate* · `read.schema`, `csv`

Read the same file against a declared contract, so the types cannot drift and the file is read only once.

### Example 133: Read a CSV with no header
*Beginner* · `read.csv`, `toDF`

Load a file whose first line is data, not column names.

### Example 134: Read a file with a different delimiter
*Beginner* · `option("sep")`

Read a pipe-delimited file, since not every "CSV" uses commas.

### Example 135: Handle quoted fields
*Intermediate* · `option("quote")`, `option("escape")`

Read a file where a field contains the delimiter, protected by quotes.

### Example 136: Discard rows that do not fit
*Intermediate* · `option("mode"`, `"DROPMALFORMED")`

Read a file containing a row with too many fields, keeping only what parses.

### Example 137: Capture the rows that failed
*Advanced* · `columnNameOfCorruptRecord`

Read a file while keeping the raw text of every row that could not be parsed, so the failures can be investigated rat...

### Example 138: Refuse to read a file with bad rows
*Intermediate* · `option("mode"`, `"FAILFAST")`

Make the job fail rather than proceed when the source does not match the contract.

### Example 139: Treat specific strings as null
*Intermediate* · `option("nullValue")`, `option("emptyValue")`

Handle a file where missing data is written as a placeholder rather than left blank.

### Example 140: Parse dates during the read
*Intermediate* · `option("dateFormat")`

Read date text into a real date type in one step, with an explicit format.

### Example 141: Read every file in a directory
*Beginner* · `read.csv`

Load a folder of daily extracts as a single DataFrame.

### Example 142: Read only the files that match a pattern
*Intermediate* · `read.csv with a glob`

Read a subset of a directory, selected by filename.

### Example 143: Record which file each row came from
*Intermediate* · `input_file_name`, `regexp_extract`

Add the source filename to every row, so a bad record can be traced back to its file.

### Example 144: Read from an explicit list of paths
*Intermediate* · `read.csv with a list`

Read exactly the files you intend, named individually rather than matched by pattern.

### Example 145: Trim whitespace as you read
*Beginner* · `ignoreLeadingWhiteSpace`, `ignoreTrailingWhiteSpace`

Strip padding around field values at the read boundary, before it becomes a join key.

### Example 146: Read a field containing a newline
*Advanced* · `option("multiLine")`

Read a CSV where a quoted field spans several lines.

### Example 147: Read a file in a specific encoding
*Intermediate* · `option("encoding")`

Read a file containing accented characters, and see what a wrong encoding does.

### Example 148: Read a plain text file
*Beginner* · `read.text`

Load a file with no delimiter structure at all, one row per line.

### Example 149: Parse fixed-width records
*Advanced* · `substring`, `trim`, `cast`

Split a fixed-width extract into columns using character positions.

### Example 150: Read each file as a single string
*Advanced* · `option("wholetext")`

Load whole files intact, for formats where a line is not a meaningful unit.

### Example 151: Read newline-delimited JSON
*Beginner* · `read.json`

Load a file holding one JSON document per line, the format most APIs and log shippers produce.

### Example 152: Read a JSON file containing an array
*Intermediate* · `option("multiLine")`

Load a file that wraps its records in a single JSON array, as a REST response would.

### Example 153: Reach into a nested structure
*Beginner* · `col with dot notation`

Read a field buried two levels inside a nested JSON document.

### Example 154: Flatten a nested structure
*Intermediate* · `select with dot notation`

Convert a nested document into flat columns for a consumer that expects a plain table.

### Example 155: Expand an array into rows
*Intermediate* · `explode`, `size`

Turn a document containing a list of items into one row per item.

### Example 156: Supply a schema for JSON
*Intermediate* · `read.schema`, `json`

Read JSON without letting Spark scan the file to work out its shape.

### Example 157: Capture unparseable JSON
*Advanced* · `columnNameOfCorruptRecord`

Read JSON while keeping the raw text of documents that could not be parsed.

### Example 158: Parse JSON held in a column
*Advanced* · `from_json`, `schema_of_json`

Extract fields from a column whose values are JSON strings — a common shape in event tables and message queues.

### Example 159: Read Parquet
*Beginner* · `read.parquet`

Load a Parquet dataset, the default storage format for analytical data.

### Example 160: See that Parquet carries its own schema
*Beginner* · `printSchema`

Confirm that types survive a round trip through Parquet, unlike CSV.

### Example 161: Read only the columns you need
*Intermediate* · `select`, `explain`

Confirm that selecting a few columns from Parquet avoids reading the rest.

### Example 162: Read a partitioned directory
*Intermediate* · `read.parquet`

Load a dataset written into directories named by column value, and recover those columns.

### Example 163: Filter on a partition column
*Advanced* · `filter`, `explain`

Confirm that filtering on a partition column skips entire directories rather than scanning and discarding rows.

### Example 164: Read ORC
*Beginner* · `read.orc`

Load an ORC dataset, the columnar format common in Hive environments.

### Example 165: Read Avro
*Intermediate* · `format("avro")`

Load an Avro dataset, the row-oriented format used for streaming and message payloads.

### Example 166: Read Delta
*Intermediate* · `format("delta")`

Load a Delta table — Parquet with a transaction log on top.

### Example 167: Confirm the formats agree
*Intermediate* · `read across formats`

Verify that the same data read from four formats produces identical row counts.

### Example 168: Read a Hive-partitioned CSV directory
*Intermediate* · `read.csv`

Read CSV files stored in `column=value` directories and recover the partition column.

### Example 169: Recover partition columns with basePath
*Advanced* · `option("basePath")`

Read one partition directly while still getting the partition column back.

### Example 170: Choose a format deliberately
*Intermediate* · `comparison`

Summarise what each format costs and offers, as a decision you make once per dataset.

### Example 171: Read a compressed file
*Beginner* · `read.csv`

Load a gzip-compressed CSV without decompressing it first.

### Example 172: Use the generic reader
*Beginner* · `read.format`, `load`

Write a reader whose format is decided at runtime rather than in the code.

### Example 173: Filter files by name
*Intermediate* · `option("pathGlobFilter")`

Read a directory but skip files whose names do not match a pattern.

### Example 174: Read nested directories
*Intermediate* · `option("recursiveFileLookup")`

Read every file under a directory tree, ignoring the `column=value` convention.

### Example 175: Read only recently modified files
*Advanced* · `option("modifiedAfter")`

Process only files that arrived after a given moment, without tracking state yourself.

### Example 176: Read XML
*Intermediate* · `format("xml")`, `option("rowTag")`

Load an XML document, treating a repeated element as the row unit.

### Example 177: Control how many partitions a read produces
*Advanced* · `spark.sql.files.maxPartitionBytes`

Influence the parallelism of a file read by changing the target partition size.

### Example 178: Read text with a custom line separator
*Advanced* · `option("lineSep")`

Read a file whose records are separated by something other than a newline.

### Example 179: Reduce the cost of schema inference
*Advanced* · `option("samplingRatio")`

Infer a schema from part of a file rather than all of it.

### Example 180: Trust the schema over the header
*Advanced* · `option("enforceSchema")`

Decide what happens when a file's header names disagree with your declared schema.

### Example 181: Detect a repeated header line
*Intermediate* · `filter`

Find header rows that appear in the middle of a file, a common artefact of concatenated exports.

### Example 182: Read several sources into one DataFrame
*Intermediate* · `unionByName`

Combine data arriving in two different formats into a single DataFrame.

### Example 183: Check a file against a contract before using it
*Advanced* · `schema comparison`

Refuse to process a file whose structure has changed.

### Example 184: Split a read into clean and quarantined rows
*Advanced* · `_corrupt_record`, `filter`

Process the rows that parsed while keeping the ones that did not, for later investigation.

### Example 185: Build a reusable reader
*Advanced* · `function composition`

Capture the reading conventions a project has agreed on, so every job applies them identically.

### Example 186: Count files before reading them
*Intermediate* · `input_file_name`, `countDistinct`

Establish how many files contributed to a DataFrame, to confirm you read what you expected.

### Example 187: Handle a missing path gracefully
*Intermediate* · `exception handling`

Decide what a job should do when the directory it expects is not there.

### Example 188: Preview a file cheaply
*Beginner* · `read.text`, `limit`

Look at the first few lines of an unfamiliar file before writing a reader for it.

### Example 189: Compare partition counts across formats
*Advanced* · `rdd.getNumPartitions`

See how the storage format affects the parallelism of a read.

### Example 190: Choose read options deliberately
*Intermediate* · `review`

Summarise the decisions every read makes, whether or not you make them consciously.

---

← [Back to main index](../../README.md)
