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

import math
​
def primes(n):
  p = [2]
  for i in range(3, n+1):
    for pr in p:
      if i%pr == 0:
        break
    else:
      p.append(i)
  return p
  
def smallest(n):
  pr = primes(n)
  mmc = 1
  for p in pr:
    exp = int(math.log(n, p))
    mmc *= p**exp
  return mmc

