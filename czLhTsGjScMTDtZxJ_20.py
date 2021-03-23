"""


In mathematics, primorial, denoted by “#”, is a function from natural numbers
to natural numbers similar to the factorial function, but rather than
successively multiplying positive integers, the function only multiplies
**prime numbers**.

Create a function that takes an integer `n` and returns its **primorial**.

### Examples

    primorial(1) ➞ 2
    # First prime number = 2
    
    primorial(2) ➞ 6
    # Product of first two prime numbers = 2*3 = 6
    
    primorial(6) ➞ 30030

### Notes

n >= 1.

"""

from math import sqrt
def is_prime(num):
  return num > 1 and all([num % i for i in range(2, int(sqrt(num)) + 1)])
​
from functools import reduce
def primorial(num):
  res = []
  cnt = 2
  while len(res) < num:
    if is_prime(cnt):
      res.append(cnt)
    cnt += 1
  return reduce(lambda a, b: a * b, res)

