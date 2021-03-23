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

def smallest(n):
  fact = []
  for i in range(2, n+1):
    if not any([i%f == 0 for f in fact]):
      power = i
      while power <= n:
        power *= i
        fact.append(i)
  prod = 1
  for f in fact:
    prod *= f
  return prod

