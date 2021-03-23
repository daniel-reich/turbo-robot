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

from fractions import Fraction as frac
​
def binary_sum(lst):
    groups = []
    for s in lst:
        left, right = s.split('.')
        groups += [frac(int(left, 2))] + [frac(0.5**idx*int(i)) for idx, i in enumerate(right, 1)]
    res = sum(groups)
    n, d = res.numerator, res.denominator
    if d == 1:
        return str(n)
    return '{} {}'.format(n//d, str(res - frac(n//d))).lstrip('0 ')

