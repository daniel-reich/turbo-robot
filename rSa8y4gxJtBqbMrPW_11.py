"""


Write a function that returns the **least common multiple (LCM)** of two
integers.

### Examples

    lcm(9, 18) ➞ 18
    
    lcm(8, 5) ➞ 40
    
    lcm(17, 11) ➞ 187

### Notes

  * Both values will be positive.
  * The **LCM** is the smallest integer that is divisible by both numbers such that the remainder is zero.

"""

def gcd(l, m):
  if l < m: l,m = m,l
  while m > 0:
    l, m = m, l % m
  return l
  
def lcm(n1, n2):
  return n1 * n2 // gcd(n1, n2)

