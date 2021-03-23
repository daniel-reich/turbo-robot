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

import functools
def lcm(x,y):
  a = max(x,y)
  b = min(x,y)
  gcf = list(filter(lambda c: a % c == 0 and b % c == 0,range(1,b+1)))[-1]
  return x * (y//gcf)
def smallest(n):
  if n == 1:
    return 1
  return functools.reduce(lambda x,y: lcm(x,y),range(2,n+1))

