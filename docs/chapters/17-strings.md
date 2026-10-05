# Chapter 17: Strings

**35 examples** (736-770)

Difficulty mix: 6 Advanced . 14 Beginner . 15 Intermediate

[Open the practice notebook](../../notebooks/17-strings.ipynb) . [Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 736: Concatenate columns and literals
*Beginner* . `concat, lit`

Join several string columns and literals into a single output.

### Example 737: Concatenate with a separator
*Beginner* . `concat_ws`

Join several columns with a fixed separator.

### Example 738: Concat propagates null
*Intermediate* . `concat`

Confirm that any null in `concat` produces a null result.

### Example 739: String length
*Beginner* . `length`

Count the number of characters in each string.

### Example 740: Upper, lower, initcap
*Beginner* . `upper, lower, initcap`

Change the case of a string column.

### Example 741: Case-insensitive comparison
*Beginner* . `lower, comparison`

Compare two strings while ignoring case.

### Example 742: Case-preserving normalisation
*Intermediate* . `lower, upper`

Create a normalised comparison key alongside the original display

### Example 743: Substring with position and length
*Beginner* . `substring`

Extract a portion of a string by position and length.

### Example 744: Left and right
*Beginner* . `left, right, substring`

Extract the first N or last N characters of a string.

### Example 745: instr for first match position
*Intermediate* . `instr`

Find the first position of a substring within another string.

### Example 746: locate with a start position
*Intermediate* . `locate`

Find a substring starting from a specific position.

### Example 747: Split into an array
*Beginner* . `split`

Break a delimited string into an array of parts.

### Example 748: Trim whitespace
*Beginner* . `trim, ltrim, rtrim`

Remove leading and trailing whitespace.

### Example 749: Trim specific characters
*Intermediate* . `trim, expr`

Remove characters other than whitespace from string boundaries.

### Example 750: Pad to a fixed width
*Intermediate* . `lpad, rpad`

Pad strings to a uniform length on the left or right.

### Example 751: Truncate long strings via substring
*Intermediate* . `substring, when`

Truncate strings that exceed a maximum length, leaving shorter ones

### Example 752: Contains, startswith, endswith
*Beginner* . `contains, startswith, endswith`

Test substring containment, prefix, and suffix.

### Example 753: LIKE with wildcards
*Beginner* . `like`

Match strings against a pattern with `%` and `_` wildcards.

### Example 754: Case-insensitive LIKE
*Intermediate* . `ilike, lower`

Match a pattern without regard to case.

### Example 755: rlike for regex matching
*Intermediate* . `rlike`

Test whether a string matches a regex pattern.

### Example 756: Extract a matching group
*Intermediate* . `regexp_extract`

Extract a matching substring from a pattern.

### Example 757: Extract all matches
*Advanced* . `regexp_extract_all`

Return every match of a pattern, not just the first.

### Example 758: Replace matching text
*Beginner* . `regexp_replace`

Replace every match of a regex with a fixed string.

### Example 759: Replace with a capture group reference
*Advanced* . `regexp_replace, backreference`

Rewrite matched text using captured groups.

### Example 760: Escaping regex metacharacters
*Advanced* . `regexp_replace, quote`

Match a literal string that contains regex metacharacters like `.`,

### Example 761: Named capture groups
*Advanced* . `regexp_extract, named groups`

Use named capture groups for readability in complex patterns.

### Example 762: Format numbers with commas
*Beginner* . `format_number`

Format a number with thousands separators and a fixed decimal count.

### Example 763: printf-style templates
*Intermediate* . `format_string`

Build a formatted string from several column values.

### Example 764: Hex encoding
*Intermediate* . `hex, unhex`

Encode a string as hex and decode back.

### Example 765: Base64 encoding
*Intermediate* . `base64, unbase64`

Encode binary data as base64 and decode back.

### Example 766: Simple replace
*Beginner* . `replace, regexp_replace`

Replace all occurrences of a literal substring with another.

### Example 767: Translate for character mapping
*Intermediate* . `translate`

Map individual characters to other characters, position by position.

### Example 768: Overlay for in-place replacement
*Advanced* . `overlay`

Replace a specific position range in a string with new content.

### Example 769: Email normalisation and validation
*Advanced* . `trim, lower, rlike`

Clean and validate an email column from typical dirty ingestion.

### Example 770: String checklist
*Intermediate* . `review`

Summarise the decisions string code makes.
