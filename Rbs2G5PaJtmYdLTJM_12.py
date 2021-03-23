"""


A **pronic** number (or otherwise called as **heteromecic** ) is a number
which is a _product of two consecutive integers_ , that is, a number of the
form `n(n + 1)`. Create a function that determines whether a number is pronic
or not.

### Examples

    is_heteromecic(0) ➞ True
    # 0 * (0 + 1) = 0 * 1 = 0
    
    is_heteromecic(2) ➞ True
    # 1 * (1 + 1) = 1 * 2 = 2
    
    is_heteromecic(7) ➞ False
    
    is_heteromecic(110) ➞ True
    # 10 * (10 + 1) = 10 * 11 = 110
    
    is_heteromecic(136) ➞ False
    
    is_heteromecic(156) ➞ True

### Notes

A recursive version of this challenge can be found
[here](https://edabit.com/challenge/hoxv8zaQJNMWJqnt3).

"""

import math
def is_heteromecic(n):
  for k in range(1, int(math.sqrt(n))+1):
    if n-k == k**2:
      return True
  if n==0:
    return True
  else:
    return False
