"""


You are given a number `n`. Determine whether `n` has exactly **3 divisors**
or not.

### Examples

    is_exactly_three(4) ➞ True
    # 4 has only 3 divisors: 1, 2 and 4
    
    is_exactly_three(12) ➞ False
    # 12 has 6 divisors: 1, 2, 3, 4, 6, 12
    
    is_exactly_three(25) ➞ True
    # 25 has only 3 divisors: 1, 5, 25

### Notes

1 ≤ n ≤ 10^12

"""

import math
​
def is_prime(n):
​
  factors = 0
​
  for i in range(1,n+1):
    if n%i==0:
      factors += 1
  if factors == 2:
    return True
  else:
    return False
​
def is_exactly_three(n):
  root = float(math.sqrt(n))
  if n == 1:
    return False
  elif root.is_integer():
    return is_prime(int(root))
  else:
    return False

