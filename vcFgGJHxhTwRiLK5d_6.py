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
  def gcd(a,b):
    while a>0:
      a,b = b%a,a
    return b
  
  def lcm(a,b): return a*b//gcd(a,b)
  
  s=1
  for i in range(1,n+1):
    s = lcm(s,i)
  return s

