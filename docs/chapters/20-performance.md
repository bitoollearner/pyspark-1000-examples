# Chapter 20: Performance

**40 examples** (861â€“900)

Difficulty mix: 7 Beginner Â· 18 Intermediate Â· 15 Advanced

[ðŸ“” Open the notebook](../../notebooks/20-performance.ipynb) Â· [ðŸ“– Read the chapter on Kindle](https://www.amazon.com/dp/B0DXXXXXXX)

---

## Examples

### Example 861: Basic explain
*Beginner* Â· `explain`

Print a DataFrame's physical execution plan.

### Example 862: Explain with all plan phases
*Intermediate* Â· `explain(True)`

See all four plan phases: parsed, analyzed, optimized, and physical.

### Example 863: Formatted explain
*Intermediate* Â· `explain formatted`

Use the formatted explain mode for a more readable plan.

### Example 864: Detecting shuffles in the plan
*Intermediate* Â· `Exchange detection`

Identify shuffles by looking for `Exchange` nodes in the plan.

### Example 865: Detecting broadcast joins
*Intermediate* Â· `broadcast detection`

Identify whether a join uses the broadcast strategy.

### Example 866: Detecting filter pushdown
*Advanced* Â· `PushedFilters`

Verify that filters push down to the data source.

### Example 867: Whole-stage code generation
*Advanced* Â· `WholeStageCodegen`

See which parts of a plan use whole-stage code generation.

### Example 868: Explaining a windowed query
*Advanced* Â· `window plan`

See how a window function appears in the plan.

### Example 869: Default shuffle partitions
*Beginner* Â· `spark.sql.shuffle.partitions`

Check the default partition count for shuffle operations.

### Example 870: DataFrame partition count
*Beginner* Â· `getNumPartitions`

Get the current partition count of a DataFrame.

### Example 871: Increase parallelism with repartition
*Beginner* Â· `repartition`

Increase a DataFrame's partition count for better parallelism.

### Example 872: Reduce partitions with coalesce
*Beginner* Â· `coalesce`

Reduce a DataFrame's partition count without a full shuffle.

### Example 873: Repartition by column
*Intermediate* Â· `repartition with column`

Redistribute rows so that all rows with the same key value land in the same partition.

### Example 874: repartitionByRange
*Advanced* Â· `repartitionByRange`

Distribute rows into ordered ranges rather than hash buckets.

### Example 875: Basic cache
*Beginner* Â· `cache`

Cache a DataFrame to avoid recomputation.

### Example 876: Persist with storage level
*Intermediate* Â· `persist`, `StorageLevel`

Cache with an explicit storage level - memory, disk, or both.

### Example 877: Materialise cache with count
*Intermediate* Â· `cache count trick`

Force the cache to materialise immediately rather than on first use.

### Example 878: Unpersist to release memory
*Beginner* Â· `unpersist`

Release a cached DataFrame's memory when no longer needed.

### Example 879: When caching hurts
*Intermediate* Â· `cache anti-pattern`

Recognise cases where caching adds overhead without benefit.

### Example 880: Cache and lineage
*Advanced* Â· `cache and lineage`

Understand what happens if a cached partition is lost.

### Example 881: Explicit broadcast hint
*Intermediate* Â· `F.broadcast`

Force a join to use broadcast strategy via the `broadcast` hint.

### Example 882: Auto-broadcast threshold
*Intermediate* Â· `conf inspection`

Read the current auto-broadcast size threshold.

### Example 883: Disable auto-broadcast
*Intermediate* Â· `conf.set`

Temporarily disable auto-broadcast to see the sort-merge alternative.

### Example 884: Auto-broadcast decision by size
*Advanced* Â· `auto-broadcast decision`

Confirm that auto-broadcast decisions are based on estimated data size, not just intent.

### Example 885: Sort-merge join anatomy
*Advanced* Â· `SortMergeJoin components`

See the operators that make up a sort-merge join.

### Example 886: AQE status
*Intermediate* Â· `AQE conf`

Check whether Adaptive Query Execution is enabled and read its sub-settings.

### Example 887: Dynamic partition coalescing
*Advanced* Â· `AQE coalesce`

Read the settings that control AQE's dynamic partition coalescing.

### Example 888: Skew join handling
*Advanced* Â· `AQE skewJoin`

Read the settings for AQE's skew-join mitigation.

### Example 889: Local shuffle reader
*Advanced* Â· `AQE localShuffleReader`

Read the setting for AQE's local shuffle reader optimisation.

### Example 890: Detecting skew
*Intermediate* Â· `groupBy`, `count`

Detect partition skew by examining per-key row counts.

### Example 891: Salting a join key
*Advanced* Â· `salting pattern`

Redistribute a skewed join by adding a random salt to the join key.

### Example 892: Isolate hot keys for broadcast
*Advanced* Â· `filter`, `broadcast`

Handle a few known-hot keys separately from the rest.

### Example 893: Broadcast nested loop join
*Advanced* Â· `BroadcastNestedLoopJoin`

See what happens when a join uses a non-equality condition.

### Example 894: Parquet versus CSV
*Intermediate* Â· `file formats`

Compare Parquet and CSV for storage size and schema fidelity.

### Example 895: Compression codec comparison
*Intermediate* Â· `compression option`

Compare the file sizes produced by different Parquet compression codecs.

### Example 896: Partition pruning
*Advanced* Â· `partitionBy`, `PartitionFilters`

Verify that filters on partition columns prune entire directories.

### Example 897: Column pruning
*Intermediate* Â· `ReadSchema`

Verify that unused columns are not read from Parquet.

### Example 898: sortWithinPartitions
*Advanced* Â· `sortWithinPartitions`

Sort rows within each partition without a full shuffle.

### Example 899: Common performance anti-patterns
*Intermediate* Â· `anti-patterns`

Enumerate common performance mistakes and their fixes.

### Example 900: Performance checklist
*Intermediate* Â· `review`

Summarise the performance decisions this chapter has covered.

---

â† [Back to main index](../../README.md)
