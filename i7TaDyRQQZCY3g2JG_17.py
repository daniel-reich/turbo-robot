"""


Given a list of integers, create a function that will find the **smallest**
positive integer that is evenly divisible by all the members of the list. In
other words, find the least common multiple (LCM).

### Examples

    lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ 2520
    
    lcm([5]) ➞ 5
    
    lcm([5, 7, 11]) ➞ 385
    
    lcm([5, 7, 11, 35, 55, 77]) ➞ 385

### Notes

N/A

"""

from collections import Counter
​
​
def primes(n):
  factors = Counter()
  i = 2
  while i <= n:
    if not n % i:
      n /= i
      factors[i] += 1
    else:
      i += 1
  return factors
  
​
def lcm(nums):
  c = Counter()
  for i in nums:
    c.__ior__(primes(i))
  i = 1   # annoying that python doesnt have prod(items) until 3.8
  for x in c.elements():
    i *= x
  return i

