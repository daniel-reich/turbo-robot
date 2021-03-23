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
def bintodec(st):
    if '.' not in st:
        return Fraction(int(st,base = 2),1)
    else:
        decimal_point_idx = len(st)-1-st.find('.')
        return Fraction(int(st.replace('.',''),base = 2),2**decimal_point_idx)
​
def binary_sum(lst):
    s = sum(map(bintodec, lst))
    if s.denominator == 1:
        return str(s)
    if s < 1:
        return str(s)
    else:
        return '{} {}'.format(s.numerator//s.denominator, s % 1)

