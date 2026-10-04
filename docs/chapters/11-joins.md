# Chapter 11: Joins

**70 examples** (471â€“540)

Difficulty mix: 4 Beginner Â· 22 Intermediate Â· 44 Advanced

[ðŸ“” Open the notebook](../../notebooks/11-joins.ipynb) Â· [ðŸ“– Read the chapter on Kindle](https://www.amazon.com/dp/B0DXXXXXXX)

---

## Examples

### Example 471: Inner join
*Beginner* Â· `join`

Combine two DataFrames, keeping only rows that match on the key.

### Example 472: Left outer join
*Beginner* Â· `join with `left``

Keep every row from the left side, even when the right has no match.

### Example 473: Right outer join
*Beginner* Â· `join with `right``

Keep every row from the right side, even when the left has no match.

### Example 474: Full outer join
*Beginner* Â· `join with `outer``

Keep every row from both sides â€” matched, and unmatched from either.

### Example 475: Cross join
*Intermediate* Â· `crossJoin`

Produce every combination of rows from two DataFrames.

### Example 476: Join on a name versus a condition
*Intermediate* Â· `join`

Show how the two forms of `on` produce different output shapes.

### Example 477: Join on multiple columns
*Intermediate* Â· `join`

Combine DataFrames using a composite key.

### Example 478: Join on differently-named columns
*Intermediate* Â· `join with condition`

Combine DataFrames when the key columns have different names.

### Example 479: Rename before joining
*Intermediate* Â· `withColumnRenamed`, `join`

Normalise a key name before joining to get the coalesced output shape.

### Example 480: Join expression with a condition
*Advanced* Â· `join with expression`

Join on a condition that is not simple equality.

### Example 481: Ambiguous column after a join
*Intermediate* Â· `join`, `alias`

Show the ambiguity that arises from the condition-form join.

### Example 482: Alias both DataFrames
*Intermediate* Â· `alias`, `join`

Make cross-DataFrame column references unambiguous.

### Example 483: Composite key from several columns
*Advanced* Â· `concat_ws`, `join`

Build a synthetic composite key when the natural key is spread across several columns.

### Example 484: Handle null keys explicitly
*Advanced* Â· `join`, `eqNullSafe`

Join two DataFrames on a key that may contain nulls.

### Example 485: Detect duplicate keys before joining
*Intermediate* Â· `groupBy`, `count`

Confirm that a join key is unique on the side it should be unique.

### Example 486: Cardinality check after joining
*Intermediate* Â· `count`

Verify that a join preserved the row count of one side.

### Example 487: Coalesce the join key
*Intermediate* Â· `coalesce`, `join`

Join on a key that may need a default value on one side.

### Example 488: Filter before joining
*Advanced* Â· `join`, `filter`

Determine which side of a join a filter should apply to.

### Example 489: Left semi join
*Intermediate* Â· `join with `left_semi``

Keep rows from the left that have a match on the right, without carrying the right side's columns.

### Example 490: Left anti join
*Intermediate* Â· `join with `left_anti``

Keep rows from the left that have no match on the right.

### Example 491: Anti join to find orphans
*Intermediate* Â· `join with `left_anti``

Find rows whose foreign key does not resolve â€” a data quality check.

### Example 492: Semi join versus isin
*Advanced* Â· `isin`, `left_semi`

Compare the two forms and see when they diverge in behaviour.

### Example 493: Semi join cannot duplicate
*Advanced* Â· `left_semi`

Confirm the semi-join's guarantee that no left row is duplicated even when the right side has many matches.

### Example 494: Semi and anti partition the data
*Intermediate* Â· `left_semi`, `left_anti`

Verify that semi and anti joins together account for every left row.

### Example 495: See the default join strategy
*Advanced* Â· `explain`

Determine which physical join strategy Spark picked for a join.

### Example 496: Force a broadcast join
*Advanced* Â· `broadcast`, `join`

Ask Spark to broadcast one side of a join rather than shuffle both.

### Example 497: Auto-broadcast threshold
*Advanced* Â· `conf`

Understand when Spark broadcasts automatically without a hint.

### Example 498: Disable auto-broadcast
*Advanced* Â· `conf`

Force sort-merge for a join that would otherwise broadcast, and restore the threshold afterwards.

### Example 499: MERGE hint
*Advanced* Â· `hint`

Force a sort-merge join with a hint.

### Example 500: SHUFFLE_HASH hint
*Advanced* Â· `hint`

Force a shuffled-hash join.

### Example 501: Combine hints on both sides
*Advanced* Â· `hint`

See what happens when hints on both sides disagree.

### Example 502: Confirm hint was honoured
*Advanced* Â· `explain`

Verify programmatically that a hint took effect.

### Example 503: Self-join with aliases
*Advanced* Â· `alias`, `join`

Join a DataFrame with itself - for hierarchy, for pairs, for lag computations.

### Example 504: Find duplicate rows via self-join
*Advanced* Â· `self-join`, `groupBy`

Locate rows that appear more than once by a specific set of columns.

### Example 505: Self-join for previous-value comparison
*Advanced* Â· `self-join`, `orderBy`

Compare each order to the previous order for the same customer.

### Example 506: Self-join for hierarchical parents
*Advanced* Â· `self-join`

Join a tree-shaped DataFrame with itself to attach each node's parent row.

### Example 507: Self-join review
*Intermediate* Â· `review`

Summarise the rules that every self-join follows.

### Example 508: Detect join skew
*Advanced* Â· `groupBy`, `count`

Measure whether a join key is evenly distributed or dominated by a few values.

### Example 509: Salt a skewed join key
*Advanced* Â· `rand`, `salted join`

Split one enormous join key across several partitions so no single task carries the whole load.

### Example 510: Salt only the skewed keys
*Advanced* Â· `when`, `salted join`

Apply salting selectively to the keys that are actually skewed, leaving the rest untouched.

### Example 511: Let AQE handle skew
*Advanced* Â· `conf`, `join`

Enable Adaptive Query Execution's skew mitigation and observe its behaviour.

### Example 512: Broadcast a small skewed side
*Advanced* Â· `broadcast`

Sidestep skew entirely by broadcasting the small side.

### Example 513: Filter skewed keys separately
*Advanced* Â· `filter`, `union`

Handle a few extremely skewed keys with a different strategy from the rest.

### Example 514: Repartition before joining
*Advanced* Â· `repartition`

Pre-partition both sides on the join key to avoid a shuffle at join time.

### Example 515: Bucketed table joins
*Advanced* Â· `bucketBy`, `saveAsTable`

Persist data with a bucketing scheme so subsequent joins on the bucketed key avoid the shuffle.

### Example 516: Cache a heavily-joined DataFrame
*Intermediate* Â· `cache`, `join`

Reuse a joined DataFrame across several downstream queries without re-doing the join each time.

### Example 517: Prefer pre-aggregation to post-join filtering
*Advanced* Â· `groupBy`, `join`

Reduce a large side of a join before the join instead of after.

### Example 518: Range join with a small interval table
*Advanced* Â· `join with expression`, `broadcast`

Assign each row to an interval defined in a small side table.

### Example 519: Bucket then filter for large range joins
*Advanced* Â· `floor`, `join`, `filter`

Convert a large-side range join into an equi-join plus a filter.

### Example 520: Join to enrich with a lookup
*Intermediate* Â· `broadcast`, `join`

Add columns from a small reference table to a large fact table.

### Example 521: Chain several enrichment joins
*Advanced* Â· `join`, `chain`

Enrich a fact table with several dimension tables in one pipeline.

### Example 522: Union then join
*Advanced* Â· `union`, `join`

Combine two source DataFrames before joining against a shared reference.

### Example 523: Detect rows dropped by inner join
*Advanced* Â· `join`, `subtract`

Identify exactly which rows an inner join dropped.

### Example 524: Reconcile join by row count
*Intermediate* Â· `join`, `count`

Assert the row-count invariants a correct join should satisfy.

### Example 525: Join review
*Intermediate* Â· `review`

Summarise the decisions a join makes.

### Example 526: Latest row per group with a window
*Advanced* Â· `Window`, `row_number`

Pick the latest order per customer using a window function instead of a self-join.

### Example 527: Anti-join to detect changes
*Advanced* Â· `left_anti`

Find rows in a new snapshot that were not in the previous snapshot.

### Example 528: Delta merge for upserts
*Advanced* Â· `DeltaTable`, `merge`

Apply a batch of updates to an existing Delta table - insert new rows, update existing ones.

### Example 529: Anti-join then insert for upsert on plain Parquet
*Advanced* Â· `anti-join`, `union`, `overwrite`

Implement an upsert without a table format that supports MERGE.

### Example 530: Join over a time interval
*Advanced* Â· `join with condition`

Match each event to the campaign that was active at the time.

### Example 531: As-of join with a window
*Advanced* Â· `union`, `Window`

For each event, attach the most recent reading from another table.

### Example 532: Join reordering by Catalyst
*Advanced* Â· `explain`, `join`

Show that Spark reorders joins based on estimated sizes.

### Example 533: Broadcast timeout diagnosis
*Advanced* Â· `conf`, `broadcast`

Understand what happens when a broadcast times out and how to diagnose it.

### Example 534: Join over an in-memory lookup
*Intermediate* Â· `create_map`, `join`

Enrich a DataFrame using a Python dictionary as the lookup.

### Example 535: Repartition to skew-safe
*Advanced* Â· `repartition`, `groupBy`

Combine repartitioning with an aggregation to work around skew.

### Example 536: Detect join order matters
*Advanced* Â· `explain`

Show that filter order relative to a join can change the physical plan Catalyst produces.

### Example 537: Union all versus join
*Intermediate* Â· `union`, `join`

Choose between combining two DataFrames vertically (union) or horizontally (join).

### Example 538: Union then aggregate versus aggregate then union
*Advanced* Â· `union`, `groupBy`

Compare two shapes for combining aggregated data from multiple sources.

### Example 539: Assert join invariants in a pipeline
*Advanced* Â· `count`, `assert`

Bake row-count checks into a production join so unexpected inflation fails loudly.

### Example 540: Join checklist
*Intermediate* Â· `review`

Summarise the full join checklist covered in this chapter.

---

â† [Back to main index](../../README.md)
