"""


Adding fractional binary numbers is similar to adding decimals. The places to
the right of the decimal point (or binary point) are halves, quarters, eighths
instead of tenths, hundredths, thousandths, etc.

Improvise a function that takes two fractional binary numbers and produces
their base-10 sum. The sum can be a whole number, a fraction, or a mixed
number. The answer should be returned as a string with fractions reduced to
lowest terms.

### Examples

    binary_sum(["1.1", "1.1"]) ➞ "3"
    # 1.5 + 1.5
    
    binary_sum(["11.1", "0.001"]) ➞ "3 5/8"
    # 3.5 + 0.125
    
    binary_sum(["1101.0", "0.0100"]) ➞ "13 1/4"
    # 13 + 1/4
    
    binary_sum(["0.11", "0.00001"]) ➞ "25/32"
    # 3/4 + 1/32
    
    binary_sum(["0.0", "101.00"]) ➞ "5"

### Notes

N/A

"""

from fractions import Fraction
​
def _get_decimal(frac):
  parts = frac.split(".")
  return int(parts[0], 2) + int(parts[1], 2) / 2 ** len(parts[1])
​
def binary_sum(lst):
  frac = Fraction(sum(_get_decimal(f) for f in lst))
  if frac.numerator > frac.denominator and frac.denominator != 1:
    num = frac.numerator // frac.denominator
    return "{} {}".format(num, Fraction(frac.numerator % frac.denominator, frac.denominator))
  return str(frac)

