"""
A **Harshad** number is a number which is divisible by the sum of its digits.
For example, 132 is divisible by 6 (1+3+2).

A subset of the Harshad numbers are the **Moran** numbers. Moran numbers yield
a prime when divided by the sum of their digits. For example, 133 divided by 7
(1+3+3) yields 19, a prime.

Create a function that takes a number and returns `"M"` if the number is a
Moran number, `"H"` if it is a (non-Moran) Harshad number, or `"Neither"`.

### Examples

    moran(132) ➞ "H"
    
    moran(133) ➞ "M"
    
    moran(134) ➞ "Neither"

### Notes

N/A

"""

import math
​
def isPrime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if not n%i: return False
  return True
​
def moran(n):
  divisor=0
  for x in str(n):
    divisor+=int(x)
  if not n%divisor:
    if isPrime(n//divisor): return 'M'
    return 'H'
  return 'Neither'

