# Chapter 17: Strings

**35 examples** (736â€“770)

Difficulty mix: 14 Beginner Â· 15 Intermediate Â· 6 Advanced

[ðŸ“” Open the notebook](../../notebooks/17-strings.ipynb) Â· [ðŸ“– Read the chapter on Kindle](https://www.amazon.com/dp/B0DXXXXXXX)

---

## Examples

### Example 736: Concatenate columns and literals
*Beginner* Â· `concat`, `lit`

Join several string columns and literals into a single output.

### Example 737: Concatenate with a separator
*Beginner* Â· `concat_ws`

Join several columns with a fixed separator.

### Example 738: Concat propagates null
*Intermediate* Â· `concat`

Confirm that any null in `concat` produces a null result.

### Example 739: String length
*Beginner* Â· `length`

Count the number of characters in each string.

### Example 740: Upper, lower, initcap
*Beginner* Â· `upper`, `lower`, `initcap`

Change the case of a string column.

### Example 741: Case-insensitive comparison
*Beginner* Â· `lower`, `comparison`

Compare two strings while ignoring case.

### Example 742: Case-preserving normalisation
*Intermediate* Â· `lower`, `upper`

Create a normalised comparison key alongside the original display value.

### Example 743: Substring with position and length
*Beginner* Â· `substring`

Extract a portion of a string by position and length.

### Example 744: Left and right
*Beginner* Â· `left`, `right`, `substring`

Extract the first N or last N characters of a string.

### Example 745: instr for first match position
*Intermediate* Â· `instr`

Find the first position of a substring within another string.

### Example 746: locate with a start position
*Intermediate* Â· `locate`

Find a substring starting from a specific position.

### Example 747: Split into an array
*Beginner* Â· `split`

Break a delimited string into an array of parts.

### Example 748: Trim whitespace
*Beginner* Â· `trim`, `ltrim`, `rtrim`

Remove leading and trailing whitespace.

### Example 749: Trim specific characters
*Intermediate* Â· `trim`, `expr`

Remove characters other than whitespace from string boundaries.

### Example 750: Pad to a fixed width
*Intermediate* Â· `lpad`, `rpad`

Pad strings to a uniform length on the left or right.

### Example 751: Truncate long strings via substring
*Intermediate* Â· `substring`, `when`

Truncate strings that exceed a maximum length, leaving shorter ones unchanged.

### Example 752: Contains, startswith, endswith
*Beginner* Â· `contains`, `startswith`, `endswith`

Test substring containment, prefix, and suffix.

### Example 753: LIKE with wildcards
*Beginner* Â· `like`

Match strings against a pattern with `%` and `_` wildcards.

### Example 754: Case-insensitive LIKE
*Intermediate* Â· `ilike`, `lower`

Match a pattern without regard to case.

### Example 755: rlike for regex matching
*Intermediate* Â· `rlike`

Test whether a string matches a regex pattern.

### Example 756: Extract a matching group
*Intermediate* Â· `regexp_extract`

Extract a matching substring from a pattern.

### Example 757: Extract all matches
*Advanced* Â· `regexp_extract_all`

Return every match of a pattern, not just the first.

### Example 758: Replace matching text
*Beginner* Â· `regexp_replace`

Replace every match of a regex with a fixed string.

### Example 759: Replace with a capture group reference
*Advanced* Â· `regexp_replace`, `backreference`

Rewrite matched text using captured groups.

### Example 760: Escaping regex metacharacters
*Advanced* Â· `regexp_replace`, `quote`

Match a literal string that contains regex metacharacters like `.`, `*`, and `?`.

### Example 761: Named capture groups
*Advanced* Â· `regexp_extract`, `named groups`

Use named capture groups for readability in complex patterns.

### Example 762: Format numbers with commas
*Beginner* Â· `format_number`

Format a number with thousands separators and a fixed decimal count.

### Example 763: printf-style templates
*Intermediate* Â· `format_string`

Build a formatted string from several column values.

### Example 764: Hex encoding
*Intermediate* Â· `hex`, `unhex`

Encode a string as hex and decode back.

### Example 765: Base64 encoding
*Intermediate* Â· `base64`, `unbase64`

Encode binary data as base64 and decode back.

### Example 766: Simple replace
*Beginner* Â· `replace`, `regexp_replace`

Replace all occurrences of a literal substring with another.

### Example 767: Translate for character mapping
*Intermediate* Â· `translate`

Map individual characters to other characters, position by position.

### Example 768: Overlay for in-place replacement
*Advanced* Â· `overlay`

Replace a specific position range in a string with new content.

### Example 769: Email normalisation and validation
*Advanced* Â· `trim`, `lower`, `rlike`

Clean and validate an email column from typical dirty ingestion.

### Example 770: String checklist
*Intermediate* Â· `review`

Summarise the decisions string code makes.

---

â† [Back to main index](../../README.md)
