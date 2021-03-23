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
def binary_sum(lst):
  x, y = convert_to_float(lst[0].strip('0')), convert_to_float(lst[1].strip('0'))
  t = str(x+y)
  n = t.index('.')
​
  i, d = int(t[:n]), Fraction(t[n:])
  if not d:
    return str(i)
  elif not i:
    return str(d)
  else:
    return '{} {}'.format(i, d)
​
def convert_to_float(n):
  i, d = n.split('.')
  i = int(i,2) if i else 0
  d = int('0'+d,2)/2**(len(d)) if d else 0
  return float(i+d)

