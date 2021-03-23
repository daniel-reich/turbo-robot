"""


Create a function that takes a number `max_den` and returns the total number
of fully simplified proper fractions that exist with denominator less than or
equal to `max_den`.

You only need to return the number of fractions; **NOT the fractions
themselves**. In the examples below, I list the fractions simply for your
reference.

### Examples

    sim_prop_frac(10) ➞ 31
    # 1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5, 1/6, 5/6, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7, 1/8, 3/8, 5/8, 7/8, 1/9, 2/9, 4/9, 5/9, 7/9, 8/9, 1/10, 3/10, 7/10, 9/10
    
    sim_prop_frac(7) ➞ 17
    # 1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5, 1/6, 5/6, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7

### Notes

A fully simplified proper fraction is a fraction where both the numerator and
denominator share no common factors besides 1 and the fraction is less than 1.

"""

from math import sqrt, ceil
from fractions import gcd
​
def is_prime(n):
  if n < 2: return False
  if n < 4: return True
  if n%2 == 0 or n%3 == 0: return False
  return all(n % i > 0 for i in range(3, ceil(sqrt(n)) + 1, 2))
​
def sim_prop_frac(max_den):
  count_distinct = 0
  for den in range(2, max_den + 1):
    if is_prime(den):
      count_distinct += den - 1
    else:
      for n in range(1, den):
        if gcd(n, den) == 1:
          count_distinct += 1
  return count_distinct

