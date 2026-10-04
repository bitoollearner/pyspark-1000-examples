# Chapter 12: Complex Types

**50 examples** (541â€“590)

Difficulty mix: 14 Beginner Â· 20 Intermediate Â· 16 Advanced

[ðŸ“” Open the notebook](../../notebooks/12-complex-types.ipynb) Â· [ðŸ“– Read the chapter on Kindle](https://www.amazon.com/dp/B0DXXXXXXX)

---

## Examples

### Example 541: Construct an array column
*Beginner* Â· `array`

Build an array from several scalar columns.

### Example 542: Access array elements by index
*Beginner* Â· `getItem`, `indexing`

Read the first, second, and third elements of an array column.

### Example 543: Get the array length
*Beginner* Â· `size`

Count how many elements each array column contains.

### Example 544: Check membership with array_contains
*Beginner* Â· `array_contains`

Test whether an array contains a particular value.

### Example 545: Explode into rows
*Beginner* Â· `explode`

Turn each array element into its own row.

### Example 546: Explode with position
*Intermediate* Â· `posexplode`

Explode an array and record each element's position.

### Example 547: Outer explode keeps empty rows
*Intermediate* Â· `explode_outer`

Explode an array without dropping rows whose array is empty or null.

### Example 548: Split a string into an array
*Beginner* Â· `split`

Convert a delimited string into an array column.

### Example 549: Concatenate arrays
*Intermediate* Â· `concat`, `array_union`, `array_distinct`

Combine two arrays, with and without deduplication.

### Example 550: Transform each element
*Intermediate* Â· `transform`

Apply a function to every element of an array.

### Example 551: Filter array elements
*Intermediate* Â· `filter`

Keep only array elements satisfying a condition.

### Example 552: Test any element with exists
*Intermediate* Â· `exists`

Check whether at least one array element satisfies a condition.

### Example 553: All elements match with forall
*Intermediate* Â· `forall`

Check whether every array element satisfies a condition.

### Example 554: Aggregate an array
*Advanced* Â· `aggregate`

Fold an array into a scalar with an accumulator and a step function.

### Example 555: Zip two arrays
*Advanced* Â· `arrays_zip`

Combine two arrays element-wise into an array of structs.

### Example 556: Construct a struct
*Beginner* Â· `struct`

Bundle several columns into a single struct column.

### Example 557: Access struct fields
*Beginner* Â· `dot notation`

Read individual fields out of a struct.

### Example 558: Add a field to a struct
*Intermediate* Â· `withField`

Extend an existing struct with an additional field.

### Example 559: Rename a struct field
*Intermediate* Â· `withField`, `dropFields`

Rename a field inside a struct.

### Example 560: Nest struct inside struct
*Advanced* Â· `struct`, `nested access`

Build and query a two-level nested struct.

### Example 561: Convert struct to columns
*Beginner* Â· `select with dot`

Flatten a struct back into individual columns.

### Example 562: Struct equality
*Advanced* Â· `equality`

Compare two structs for equality.

### Example 563: Order struct fields in a projection
*Intermediate* Â· `struct`

Ensure a struct's field order matches an external contract.

### Example 564: max_by returning a struct
*Advanced* Â· `max_by`, `struct`

Return several columns at the row with the maximal ordering column, in one atomic step.

### Example 565: Collect struct from group
*Advanced* Â· `collect_list`, `struct`

Gather each group's rows as an array of structs.

### Example 566: Construct a map from entries
*Beginner* Â· `create_map`

Build a map from literal key-value pairs.

### Example 567: Access map values
*Beginner* Â· `getItem`, `indexing`

Read map values by key.

### Example 568: Check whether a key exists
*Intermediate* Â· `map_contains_key`

Distinguish a missing key from a key whose value is null.

### Example 569: Get map size
*Beginner* Â· `size`

Count the number of entries in a map.

### Example 570: Get keys and values as arrays
*Intermediate* Â· `map_keys`, `map_values`

Extract the key set and value list from a map.

### Example 571: Convert map to array of structs
*Intermediate* Â· `map_entries`

Turn a map into an array of key-value struct pairs for downstream processing.

### Example 572: Explode a map
*Intermediate* Â· `explode`, `map_entries`

Turn each map entry into its own row.

### Example 573: Combine two maps
*Intermediate* Â· `map_concat`

Merge two maps into one, with the second overriding on shared keys.

### Example 574: Filter a map by predicate
*Advanced* Â· `map_filter`

Keep only the entries of a map that satisfy a condition on key or value.

### Example 575: Transform map values
*Advanced* Â· `transform_values`

Apply a function to every value in a map, leaving keys unchanged.

### Example 576: Parse JSON to a struct
*Intermediate* Â· `from_json`

Convert a JSON string column into a struct column with typed fields.

### Example 577: Parse JSON to a map
*Intermediate* Â· `from_json`

Convert a JSON string into a map when the keys are not known in advance.

### Example 578: Serialise a struct to JSON
*Beginner* Â· `to_json`

Convert a struct column back into a JSON string for downstream systems.

### Example 579: JSON round-trip
*Intermediate* Â· `from_json`, `to_json`

Confirm that parsing and reserialising JSON preserves the content.

### Example 580: Handle malformed JSON
*Advanced* Â· `from_json`

Detect and handle records where the JSON is unparseable.

### Example 581: from_json with options
*Advanced* Â· `from_json`

Configure JSON parsing to accept non-standard input forms.

### Example 582: schema_of_json infers the schema
*Advanced* Â· `schema_of_json`

Infer a JSON schema from a sample row for use in `from_json`.

### Example 583: Serialise a map to JSON
*Intermediate* Â· `to_json`

Convert a map column into a JSON object string.

### Example 584: Serialise arrays
*Beginner* Â· `to_json`

Serialise an array column into a JSON array string.

### Example 585: Nested JSON round-trip
*Advanced* Â· `from_json`, `to_json`

Round-trip nested JSON with structs, arrays, and mixed types.

### Example 586: Nested filter without exploding
*Advanced* Â· `exists`, `filter`

Filter parent rows by a condition on nested array elements without first exploding.

### Example 587: Aggregate over nested structs
*Advanced* Â· `aggregate`, `transform`

Compute a summary statistic across nested struct fields per row.

### Example 588: Flatten nested schema for output
*Advanced* Â· `select with dot`, `alias`

Convert a nested DataFrame into a flat one for downstream consumers.

### Example 589: Complex-type columns in a Delta table
*Advanced* Â· `write.format("delta")`

Confirm that arrays, structs, and maps survive a Delta round-trip.

### Example 590: Complex-type checklist
*Intermediate* Â· `review`

Summarise the decisions complex types force.

---

â† [Back to main index](../../README.md)
