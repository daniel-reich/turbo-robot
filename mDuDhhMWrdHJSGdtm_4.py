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

from math import sqrt, floor
def is_prime(n):
  if n < 2: return False
  if n < 4: return True
  if n % 2 == 0: return False
  return all(bool(n % f) for f in range(3, int(sqrt(n)) + 1, 2))
​
def is_exactly_three(n):
  root2 = floor(sqrt(n))
  return root2 * root2 == n and is_prime(root2)

