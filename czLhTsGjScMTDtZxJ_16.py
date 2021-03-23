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

import numpy as np
from functools import reduce
def sieve(n):
  fl = np.ones(n,dtype=bool)
  fl[0] = fl[1] = False
  for i in range(2,int(n**0.5)+1):
    if fl[i]:
      fl[i*i::i] = False
  return np.flatnonzero(fl)
  
def primorial(n):
  x = 20
  pr = sieve(x)
  while len(pr) < n:
    x *= 5
    pr = sieve(x)
  return reduce(lambda x,y:x*y, pr[:n])

