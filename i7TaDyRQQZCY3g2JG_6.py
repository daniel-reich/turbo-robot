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

from functools import reduce
def lcm(nums):
  return reduce(lambda n, m: (n*m)/gcd(n,m),nums,1)
  
def gcd(x,y):
  while y:
    x, y = y, x%y
  return x

