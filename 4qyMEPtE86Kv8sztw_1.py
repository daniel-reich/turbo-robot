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
def bin_to_fraction(b):
    ap, pp = b.split('.')
    return Fraction(int(ap,2) + int(pp, 2) / 2**len(pp))
​
def binary_sum(lst):
    sf = bin_to_fraction(lst[0]) + bin_to_fraction(lst[1])
    w, f = divmod(sf.numerator, sf.denominator)
    if w and f:
        return '{} {}/{}'.format(w, f, sf.denominator)
    return str(sf)

