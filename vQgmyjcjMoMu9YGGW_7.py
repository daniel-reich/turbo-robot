"""


Create a function that returns the simplified version of a fraction.

### Examples

    simplify("4/6") ➞ "2/3"
    
    simplify("10/11") ➞ "10/11"
    
    simplify("100/400") ➞ "1/4"
    
    simplify("8/4") ➞ "2"

### Notes

  * A fraction is simplified if there are no common factors (except 1) between the numerator and the denominator. For example, `4/6` is **not** simplified, since `4` and `6` both share `2` as a factor.
  * If improper fractions can be transformed into integers, do so in your code (see example #4).

"""

import math
from functools import reduce
​
def simplify(txt):
  numerator, denominator = map(int, txt.split('/'))
  numerator_factors = prime_factors(numerator)
  denominator_factors = prime_factors(denominator)
  final_num = []
  for i in numerator_factors:
    if i in denominator_factors:
      denominator_factors.remove(i)
    else:
      final_num.append(i)
  list_mult = lambda x, y: x * y
  if not denominator_factors:
    return str(reduce(list_mult, final_num))
  numerator, denominator = reduce(list_mult, final_num), reduce(list_mult, denominator_factors)
  return "{}/{}".format(numerator, denominator)
​
def prime_factors(num):
  factors = []
  factor = 2
  initial_num = num
  while num != 1 and factor <= initial_num/2:
    while num % factor == 0:
      num /= factor
      factors.append(factor)
    factor += 1
  return factors if factors else [1, num]

