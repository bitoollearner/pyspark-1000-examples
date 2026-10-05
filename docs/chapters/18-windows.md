# Chapter 18: Windows

**65 examples** (771-835)

Difficulty mix: 23 Advanced . 14 Beginner . 28 Intermediate

[Open the practice notebook](../../notebooks/18-windows.ipynb) . [Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 771: Basic window with partition and order
*Beginner* . `Window, row_number`

Define a window that groups rows by region and orders them by date,

### Example 772: Window over the whole dataset
*Beginner* . `Window, row_number`

Rank every row across the whole DataFrame, without partitioning.

### Example 773: Multiple partition keys
*Intermediate* . `Window, partitionBy`

Partition by two columns to produce a rank per (region, month).

### Example 774: Multiple ordering columns
*Intermediate* . `Window, orderBy`

Break ties in the ordering using a second column.

### Example 775: Ascending and descending order
*Beginner* . `Window, asc, desc`

Order a window ascending or descending.

### Example 776: Nulls first or nulls last
*Intermediate* . `Window, nulls_first, nulls_last`

Control where null-valued rows appear in the window ordering.

### Example 777: Reusable window specifications
*Intermediate* . `Window`

Reuse the same window definition across several function calls.

### Example 778: Window functions are lazy
*Intermediate* . `Window, lazy`

Confirm that defining a window does no computation.

### Example 779: row_number for unique ranks
*Beginner* . `row_number`

Assign a distinct sequential number to each row within its partition.

### Example 780: rank for tied ranks with gaps
*Beginner* . `rank`

Assign the same rank to tied rows, with gaps after ties.

### Example 781: dense_rank for tied ranks without gaps
*Beginner* . `dense_rank`

Assign the same rank to tied rows, with no gaps after ties.

### Example 782: ntile for quantile buckets
*Intermediate* . `ntile`

Assign each row to one of N equal-sized buckets.

### Example 783: percent_rank for continuous ranking
*Intermediate* . `percent_rank`

Rank rows as a percentage from 0 to 1 based on their ordering position.

### Example 784: cume_dist for cumulative distribution
*Advanced* . `cume_dist`

Get each row's position as a fraction of the cumulative distribution.

### Example 785: Comparing row_number, rank, dense_rank
*Intermediate* . `row_number, rank, dense_rank`

Show all three ranking functions on the same tied data.

### Example 786: Top-N per group
*Intermediate* . `row_number, filter`

Keep the top 2 rows per region ordered by amount.

### Example 787: lag for previous value
*Beginner* . `lag`

Get the previous row's value within each partition.

### Example 788: lag with offset and default
*Intermediate* . `lag`

Get a value from N rows back, with a default when out of range.

### Example 789: lead for next value
*Beginner* . `lead`

Get the next row's value within each partition.

### Example 790: first_value in a window
*Intermediate* . `first_value, first`

Get the first row's value in each partition.

### Example 791: last_value in a window
*Intermediate* . `last`

Get the last row's value in each partition.

### Example 792: nth_value
*Advanced* . `nth_value`

Get the Nth row's value in each partition.

### Example 793: first_value with ignoreNulls
*Advanced* . `first, ignoreNulls`

Get the first non-null value in a window frame.

### Example 794: lag at partition boundary
*Intermediate* . `lag`

Confirm that `lag` returns null at partition boundaries, not from the

### Example 795: Difference from previous row
*Intermediate* . `lag, arithmetic`

Compute the difference between each row's amount and the previous

### Example 796: Running total
*Beginner* . `sum, Window`

Compute a running sum of amounts per region, ordered by date.

### Example 797: Running count
*Beginner* . `count, Window`

Count the rows seen so far in each partition.

### Example 798: Moving average with rowsBetween
*Intermediate* . `avg, rowsBetween`

Compute a 3-period moving average over an ordered window.

### Example 799: Running min and max
*Beginner* . `min, max`

Track the smallest and largest amounts seen so far in each partition.

### Example 800: Accumulating collect_list
*Advanced* . `collect_list`

Build an array of amounts seen so far in each partition.

### Example 801: Whole-partition aggregate (no orderBy)
*Beginner* . `sum, Window`

Add the region's total amount to every row without ordering.

### Example 802: orderBy changes frame semantics
*Intermediate* . `sum`

Show that adding `orderBy` changes the default frame from

### Example 803: Multiple aggregates in one window
*Intermediate* . `multiple aggregates`

Compute several running aggregates over the same window in one pass.

### Example 804: Running frame: unboundedPreceding to currentRow
*Intermediate* . `rowsBetween`

Define an explicit frame from the partition start to the current row.

### Example 805: Bounded lookback: last N rows
*Intermediate* . `rowsBetween`

Define a frame covering the current row plus the previous N-1 rows.

### Example 806: Centered frame
*Advanced* . `rowsBetween`

Compute an aggregate over a centered window - N rows before, current,

### Example 807: Whole-partition frame
*Beginner* . `rowsBetween`

Define a frame covering the entire partition explicitly.

### Example 808: rangeBetween with numeric ordering
*Advanced* . `rangeBetween`

Define a frame based on the value of the ordering column, not row

### Example 809: rangeBetween with time (epoch seconds)
*Advanced* . `rangeBetween, unix_timestamp`

Compute a rolling sum over the last N seconds using epoch time.

### Example 810: Default frame with orderBy
*Intermediate* . `default frame`

Confirm what the default frame is when `orderBy` is present.

### Example 811: Default frame without orderBy
*Intermediate* . `default frame`

Confirm what the default frame is when `orderBy` is absent.

### Example 812: Empty frame edge case
*Advanced* . `frame edge, count`

See what aggregates return when the frame is empty.

### Example 813: Current-row-only frame
*Advanced* . `rowsBetween`

Define a frame that includes only the current row.

### Example 814: Latest row per group
*Beginner* . `row_number, filter`

Keep only the most recent row per region.

### Example 815: Top-N per group with rank comparison
*Intermediate* . `row_number, rank`

Compare `row_number` and `rank` for a top-N-per-group filter.

### Example 816: Deduplication with row_number
*Intermediate* . `row_number, distinct`

Remove duplicate rows keeping the first occurrence by some ordering.

### Example 817: Percentage of group total
*Intermediate* . `sum, ratio`

Show each row as a percentage of its region's total.

### Example 818: Running distinct count via collect_set
*Advanced* . `collect_set, size`

Track the number of distinct amounts seen so far in each region.

### Example 819: Forward fill (last with ignoreNulls)
*Advanced* . `last, ignorenulls`

Fill null values with the most recent non-null value.

### Example 820: Backward fill (first with ignoreNulls)
*Advanced* . `first, ignorenulls`

Fill null values with the next non-null value.

### Example 821: Days since previous event
*Intermediate* . `lag, datediff`

Compute the number of days between each event and the previous one

### Example 822: Detect gaps in a sequence
*Advanced* . `lag, when`

Mark rows where the date sequence has a gap greater than 1 day.

### Example 823: Group consecutive rows (islands)
*Advanced* . `lag, sum, cumulative`

Assign a group id to consecutive rows with no gap between them.

### Example 824: Change detection via lag
*Intermediate* . `lag, when`

Flag rows where a value differs from the previous row.

### Example 825: Session detection by inactivity gap
*Advanced* . `unix_timestamp, gap detection`

Group events into sessions defined by a 30-minute inactivity gap.

### Example 826: Rolling difference within group
*Advanced* . `lag, arithmetic`

Compute period-over-period change per group.

### Example 827: Bucket into deciles per group
*Advanced* . `ntile`

Assign each row to one of 10 buckets based on its amount rank within

### Example 828: Filter with a window predicate
*Advanced* . `row_number, filter`

Keep rows above the group's median.

### Example 829: Multiple windows sharing partitioning
*Advanced* . `window reuse`

See that multiple window functions with the same partition and

### Example 830: Windows on already-sorted data
*Advanced* . `repartition`

Pre-partition data to avoid the window's internal shuffle.

### Example 831: Skew in partitions
*Advanced* . `groupBy, count`

Detect skew - partitions with vastly more rows than others.

### Example 832: Global versus partitioned windows
*Intermediate* . `Window, comparison`

Compare a global (unpartitioned) window with a partitioned window on

### Example 833: Windows combined with aggregation
*Advanced* . `window + groupBy`

Compute a windowed running total per region, then summarise the

### Example 834: Distinct-in-window workaround
*Advanced* . `approx_count_distinct workaround`

Approximate a running distinct count when the exact `count(distinct)`

### Example 835: Windows checklist
*Intermediate* . `review`

Summarise the decisions window code makes.
