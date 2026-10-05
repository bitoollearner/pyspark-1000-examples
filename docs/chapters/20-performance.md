# Chapter 20: Performance

**40 examples** (861-900)

Difficulty mix: 15 Advanced . 7 Beginner . 18 Intermediate

[Open the practice notebook](../../notebooks/20-performance.ipynb) . [Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 861: Basic explain
*Beginner* . `explain`

Print a DataFrame's physical execution plan.

### Example 862: Explain with all plan phases
*Intermediate* . `explain(True)`

See all four plan phases: parsed, analyzed, optimized, and physical.

### Example 863: Formatted explain
*Intermediate* . `explain formatted`

Use the formatted explain mode for a more readable plan.

### Example 864: Detecting shuffles in the plan
*Intermediate* . `Exchange detection`

Identify shuffles by looking for `Exchange` nodes in the plan.

### Example 865: Detecting broadcast joins
*Intermediate* . `broadcast detection`

Identify whether a join uses the broadcast strategy.

### Example 866: Detecting filter pushdown
*Advanced* . `PushedFilters`

Verify that filters push down to the data source.

### Example 867: Whole-stage code generation
*Advanced* . `WholeStageCodegen`

See which parts of a plan use whole-stage code generation.

### Example 868: Explaining a windowed query
*Advanced* . `window plan`

See how a window function appears in the plan.

### Example 869: Default shuffle partitions
*Beginner* . `spark.sql.shuffle.partitions`

Check the default partition count for shuffle operations.

### Example 870: DataFrame partition count
*Beginner* . `getNumPartitions`

Get the current partition count of a DataFrame.

### Example 871: Increase parallelism with repartition
*Beginner* . `repartition`

Increase a DataFrame's partition count for better parallelism.

### Example 872: Reduce partitions with coalesce
*Beginner* . `coalesce`

Reduce a DataFrame's partition count without a full shuffle.

### Example 873: Repartition by column
*Intermediate* . `repartition with column`

Redistribute rows so that all rows with the same key value land in

### Example 874: repartitionByRange
*Advanced* . `repartitionByRange`

Distribute rows into ordered ranges rather than hash buckets.

### Example 875: Basic cache
*Beginner* . `cache`

Cache a DataFrame to avoid recomputation.

### Example 876: Persist with storage level
*Intermediate* . `persist, StorageLevel`

Cache with an explicit storage level - memory, disk, or both.

### Example 877: Materialise cache with count
*Intermediate* . `cache count trick`

Force the cache to materialise immediately rather than on first use.

### Example 878: Unpersist to release memory
*Beginner* . `unpersist`

Release a cached DataFrame's memory when no longer needed.

### Example 879: When caching hurts
*Intermediate* . `cache anti-pattern`

Recognise cases where caching adds overhead without benefit.

### Example 880: Cache and lineage
*Advanced* . `cache and lineage`

Understand what happens if a cached partition is lost.

### Example 881: Explicit broadcast hint
*Intermediate* . `F.broadcast`

Force a join to use broadcast strategy via the `broadcast` hint.

### Example 882: Auto-broadcast threshold
*Intermediate* . `conf inspection`

Read the current auto-broadcast size threshold.

### Example 883: Disable auto-broadcast
*Intermediate* . `conf.set`

Temporarily disable auto-broadcast to see the sort-merge alternative.

### Example 884: Auto-broadcast decision by size
*Advanced* . `auto-broadcast decision`

Confirm that auto-broadcast decisions are based on estimated data

### Example 885: Sort-merge join anatomy
*Advanced* . `SortMergeJoin components`

See the operators that make up a sort-merge join.

### Example 886: AQE status
*Intermediate* . `AQE conf`

Check whether Adaptive Query Execution is enabled and read its

### Example 887: Dynamic partition coalescing
*Advanced* . `AQE coalesce`

Read the settings that control AQE's dynamic partition coalescing.

### Example 888: Skew join handling
*Advanced* . `AQE skewJoin`

Read the settings for AQE's skew-join mitigation.

### Example 889: Local shuffle reader
*Advanced* . `AQE localShuffleReader`

Read the setting for AQE's local shuffle reader optimisation.

### Example 890: Detecting skew
*Intermediate* . `groupBy, count`

Detect partition skew by examining per-key row counts.

### Example 891: Salting a join key
*Advanced* . `salting pattern`

Redistribute a skewed join by adding a random salt to the join key.

### Example 892: Isolate hot keys for broadcast
*Advanced* . `filter, broadcast`

Handle a few known-hot keys separately from the rest.

### Example 893: Broadcast nested loop join
*Advanced* . `BroadcastNestedLoopJoin`

See what happens when a join uses a non-equality condition.

### Example 894: Parquet versus CSV
*Intermediate* . `file formats`

Compare Parquet and CSV for storage size and schema fidelity.

### Example 895: Compression codec comparison
*Intermediate* . `compression option`

Compare the file sizes produced by different Parquet compression

### Example 896: Partition pruning
*Advanced* . `partitionBy, PartitionFilters`

Verify that filters on partition columns prune entire directories.

### Example 897: Column pruning
*Intermediate* . `ReadSchema`

Verify that unused columns are not read from Parquet.

### Example 898: sortWithinPartitions
*Advanced* . `sortWithinPartitions`

Sort rows within each partition without a full shuffle.

### Example 899: Common performance anti-patterns
*Intermediate* . `anti-patterns`

Enumerate common performance mistakes and their fixes.

### Example 900: Performance checklist
*Intermediate* . `review`

Summarise the performance decisions this chapter has covered.
