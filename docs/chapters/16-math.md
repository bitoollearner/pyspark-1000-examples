# Chapter 16: Math

**30 examples** (706–735)

Difficulty mix: 13 Beginner · 12 Intermediate · 5 Advanced

[📔 Open the notebook](../../notebooks/16-math.ipynb) · [📖 Read the chapter on Kindle](https://www.amazon.com/dp/YOUR-KINDLE-ASIN)

---

## Examples

### Example 706: Round to nearest integer
*Beginner* · `round`

Round a floating-point column to the nearest integer.

### Example 707: Round to a specific decimal place
*Beginner* · `round`

Round to a specific number of decimal places, positive or negative.

### Example 708: Ceil and floor
*Beginner* · `ceil`, `floor`

Round up (ceiling) or down (floor) to the nearest integer.

### Example 709: Banker's rounding with bround
*Intermediate* · `bround`

Round using half-to-even (banker's) rounding.

### Example 710: Truncation via cast
*Beginner* · `cast`

Truncate a float toward zero, dropping the fractional part.

### Example 711: Rounding negative numbers
*Intermediate* · `round`, `bround`

Compare the four rounding functions on negative half-values.

### Example 712: Absolute value
*Beginner* · `abs`

Convert every value in a column to its non-negative magnitude.

### Example 713: Sign via signum
*Beginner* · `signum`

Return -1, 0, or 1 based on a number's sign.

### Example 714: Categorise sign explicitly
*Beginner* · `when`

Categorise numbers as positive, negative, or zero with a label.

### Example 715: Power function
*Beginner* · `pow`

Raise one column to the power of another (or a constant).

### Example 716: Square root
*Beginner* · `sqrt`

Compute the principal square root of a column.

### Example 717: Exponential
*Beginner* · `exp`

Compute `e^x` for a column.

### Example 718: Natural logarithm
*Beginner* · `log`, `ln`

Compute the natural logarithm (base e) of a column.

### Example 719: Log with an explicit base
*Intermediate* · `log`, `log10`, `log2`

Compute logarithms with different bases.

### Example 720: expm1 and log1p for stability
*Advanced* · `expm1`, `log1p`

Compute `e^x - 1` and `ln(1 + x)` accurately for small `x`.

### Example 721: Basic trig functions
*Beginner* · `sin`, `cos`, `tan`

Compute sine, cosine, and tangent for angles in radians.

### Example 722: atan2 for coordinate angles
*Intermediate* · `atan2`

Compute the angle of a 2D vector, correct in all four quadrants.

### Example 723: Distance via hypot
*Intermediate* · `hypot`

Compute Euclidean distance without intermediate overflow.

### Example 724: Radians and degrees
*Beginner* · `radians`, `degrees`

Convert between radians and degrees.

### Example 725: Decimal type
*Intermediate* · `DecimalType`, `cast`

Declare a decimal column with specific precision and scale.

### Example 726: Decimal arithmetic precision
*Advanced* · `decimal ops`

See how precision grows through decimal arithmetic.

### Example 727: Cast float to decimal
*Intermediate* · `cast`

Convert a float column to decimal with a specific precision.

### Example 728: Money precision comparison
*Advanced* · `DecimalType`, `comparison`

See the difference between float and decimal for a classic penny- addition problem.

### Example 729: Variance and standard deviation
*Intermediate* · `variance`, `stddev`

Compute variance and standard deviation with sample and population variants.

### Example 730: Skewness, kurtosis, and quantiles
*Advanced* · `skewness`, `kurtosis`, `percentile_approx`

Describe the shape of a distribution beyond mean and variance.

### Example 731: Seeded random uniform
*Intermediate* · `rand`

Generate uniform random numbers reproducibly.

### Example 732: Seeded random normal
*Intermediate* · `randn`

Generate normally-distributed random numbers reproducibly.

### Example 733: Integer overflow
*Advanced* · `cast`

Demonstrate silent integer overflow and how casting to a wider type prevents it.

### Example 734: Division by zero
*Intermediate* · `division`, `when`

See how division by zero behaves and how to guard it.

### Example 735: Math checklist
*Intermediate* · `review`

Summarise the numeric decisions the chapter has covered.

---

← [Back to main index](../../README.md)
