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
def convert(b):
    x, y = b.split('.')
    ans = Fraction(int('0b' + x, 2), 1)
    p = 0
    for digit in y:
        p += 1
        if digit == '1':
            ans += Fraction(1, 2**p)
    return ans
​
def binary_sum(lst):
    a = convert(lst[0])
    b = convert(lst[1])
    c = a + b
    n, d = c.numerator, c.denominator
    whole = n // d
    fractional = n % d
    if fractional == 0:
        return str(whole)
    ans = "" if whole == 0 else str(whole) + ' '
    ans += str(n % d) + '/' + str(d)
    return ans

