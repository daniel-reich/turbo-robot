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

from collections import Counter
​
def prime_factors(n):
  i = 2
  factors = []
  while i ** 2 <= n:
    if n % i:
      i += 1
    else:
      n //= i
      factors.append(i)
  if n >1:
    factors.append(n)
  return factors
​
def smallest(n):
​
  prime_counts = Counter()
  for i in range(2, n+1):
    factors = prime_factors(i)
    for factor in set(factors):
      factor_count = factors.count(factor)
      if factor_count > prime_counts[factor]:
        prime_counts[factor] = factor_count
        
  product = 1
  for key in prime_counts:
    product *= key ** prime_counts[key]
    
  return product

