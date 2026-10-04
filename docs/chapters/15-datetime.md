# Chapter 15: Datetime

**45 examples** (661â€“705)

Difficulty mix: 16 Beginner Â· 15 Intermediate Â· 14 Advanced

[ðŸ“” Open the notebook](../../notebooks/15-datetime.ipynb) Â· [ðŸ“– Read the chapter on Kindle](https://www.amazon.com/dp/B0DXXXXXXX)

---

## Examples

### Example 661: Parse a date with the default format
*Beginner* Â· `to_date`

Convert an ISO-format date string column to a `DATE` type.

### Example 662: Parse a date with a custom format
*Beginner* Â· `to_date`

Parse a date string that does not match the ISO format.

### Example 663: Parse a timestamp
*Beginner* Â· `to_timestamp`

Parse a date-plus-time string into a `TIMESTAMP` type.

### Example 664: Unix epoch conversion
*Intermediate* Â· `unix_timestamp`, `from_unixtime`

Convert between timestamps and Unix epoch seconds.

### Example 665: Construct dates and timestamps from parts
*Intermediate* Â· `make_date`, `make_timestamp`

Build a date or timestamp from separate year, month, and day columns.

### Example 666: Handle multiple date formats
*Advanced* Â· `coalesce`, `to_date`

Parse a column where different rows use different date formats.

### Example 667: Handle parse failures
*Advanced* Â· `to_date`, `isNull`

Detect rows where date parsing failed.

### Example 668: Format a date for display
*Beginner* Â· `date_format`

Convert a date or timestamp to a formatted string for display.

### Example 669: Common format patterns
*Beginner* Â· `date_format`

Compare the most common format patterns side by side.

### Example 670: Cast between date and string
*Beginner* Â· `cast`

Cast dates and timestamps to strings and back with the type system.

### Example 671: Parse with unusual separators
*Intermediate* Â· `to_date`

Parse dates with separators other than dashes.

### Example 672: Add and subtract days
*Beginner* Â· `date_add`, `date_sub`

Shift a date by a number of days.

### Example 673: Add months and compute month differences
*Intermediate* Â· `add_months`, `months_between`

Add months to a date and compute the number of months between two dates.

### Example 674: Days between two dates
*Beginner* Â· `datediff`

Count the days between two dates.

### Example 675: Interval arithmetic
*Intermediate* Â· `expr`, `INTERVAL`

Add or subtract typed intervals like "5 days" or "2 hours".

### Example 676: Next occurrence of a weekday
*Advanced* Â· `next_day`

Find the next occurrence of a specific weekday from a given date.

### Example 677: Last day of month
*Beginner* Â· `last_day`

Find the last date of the month containing a given date.

### Example 678: Year, month, day
*Beginner* Â· `year`, `month`, `dayofmonth`

Extract calendar parts from a date or timestamp.

### Example 679: Hour, minute, second
*Beginner* Â· `hour`, `minute`, `second`

Extract time-of-day parts from a timestamp.

### Example 680: Day of week and day of year
*Intermediate* Â· `dayofweek`, `dayofyear`

Extract week-based day information.

### Example 681: Week and quarter
*Intermediate* Â· `weekofyear`, `quarter`

Extract the ISO week number and the calendar quarter.

### Example 682: Generic extraction with date_part
*Advanced* Â· `date_part`

Extract any date component through a single generic function.

### Example 683: Extract with 12-hour formatting
*Intermediate* Â· `date_format`

Show a timestamp with 12-hour clock formatting.

### Example 684: Truncate a timestamp to hour, day, month
*Intermediate* Â· `date_trunc`

Round a timestamp down to the start of an hour, day, week, or month.

### Example 685: Truncate a date
*Beginner* Â· `trunc`

Truncate a date to the start of the year, quarter, or month.

### Example 686: Bucket to arbitrary intervals
*Advanced* Â· `unix_timestamp`, `floor`

Round a timestamp down to a 5-minute or 15-minute boundary.

### Example 687: ISO week versus calendar year boundary
*Advanced* Â· `weekofyear`, `year`, `dayofweek`

See how ISO weeks cross calendar year boundaries.

### Example 688: Tumbling window over time
*Advanced* Â· `window`, `groupBy`

Bucket events into fixed-width time windows and aggregate.

### Example 689: Session timezone
*Intermediate* Â· `spark.conf`

Read and change the session timezone, seeing how it affects timestamp display.

### Example 690: Convert UTC to a local zone
*Intermediate* Â· `from_utc_timestamp`

Convert a timestamp stored as UTC into the wall-clock time in a different zone.

### Example 691: Convert local to UTC
*Intermediate* Â· `to_utc_timestamp`

Convert a wall-clock timestamp in a specific zone to its UTC equivalent.

### Example 692: UTC round-trip
*Intermediate* Â· `from_utc_timestamp`, `to_utc_timestamp`

Confirm that `to_utc` followed by `from_utc` returns the original wall-clock time.

### Example 693: DST boundary caveat
*Advanced* Â· `to_utc_timestamp`

Note that DST transitions cause some local times to be ambiguous or non-existent.

### Example 694: Date range filter
*Beginner* Â· `between`, `filter`

Select rows whose date falls in a specified range.

### Example 695: Current date and timestamp
*Beginner* Â· `current_date`, `current_timestamp`

Reference the current date and time at query execution.

### Example 696: Filter by relative date
*Intermediate* Â· `current_date`, `date_sub`

Select rows from the last N days relative to today.

### Example 697: Compare dates directly
*Beginner* Â· `comparison`

Filter based on a direct date comparison.

### Example 698: Sliding time window
*Advanced* Â· `window with slide`

Compute aggregates over overlapping time windows.

### Example 699: Session window on inactivity gap
*Advanced* Â· `session_window`

Group events into sessions defined by an inactivity gap.

### Example 700: Range-based window frame
*Advanced* Â· `Window`, `rangeBetween`

Compute a running aggregate over the last N minutes of events using `rangeBetween` on epoch seconds.

### Example 701: Multiple time-scoped windows
*Advanced* Â· `Window`, `multiple`

Compute several different-window aggregates side by side.

### Example 702: Weekday filter
*Beginner* Â· `dayofweek`, `filter`

Filter out weekend dates.

### Example 703: Count business days in a range
*Advanced* Â· `sequence`, `filter`, `size`

Count the number of business days in a date range.

### Example 704: Fiscal quarter and year
*Advanced* Â· `when`, `month`

Compute a fiscal quarter and year where the fiscal year starts in July.

### Example 705: Datetime checklist
*Intermediate* Â· `review`

Summarise the decisions datetime code makes.

---

â† [Back to main index](../../README.md)
