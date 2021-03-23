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
def moran(n):
  print(n)
  sum_d = sum_digits(n)
  print(sum_d)
  if n%sum_d == 0:
    print(int(n/sum_d))
    if isprime(int(n/sum_d)):
      return "M"
    else:
      return "H"
  else:
    return "Neither"
​
def isprime(n):
  for i in range(2,round(math.sqrt(n))+1):
    
    if n%i == 0:
      return False
  return True
      
def sum_digits(n):
  sum_dig = 0
  while(n > 0):
    sum_dig+=n%10
    n = int(n/10)
  return sum_dig

