"""


Given a positive integer `n`, implement a function that finds the **smallest**
number that is evenly divisible by the integers `1` through `n` inclusive.

### Examples

    smallest(1) ➞ 1
    
    smallest(5) ➞ 60
    
    smallest(10) ➞ 2520
    
    smallest(20) ➞ 232792560

### Notes

N/A

"""

from functools import reduce
from fractions import gcd
def smallest(n):
  return reduce(lcm,list(range(1,n+1)))
​
def lcm(x,y):
  return x*y//gcd(x,y)

