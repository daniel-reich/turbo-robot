"""


A _Primorial_ is a product of the first `n` prime numbers (e.g. `2 x 3 x 5 =
30`). `2, 3, 5, 7, 11, 13` are prime numbers. If `n` was `3`, you'd multiply
`2 x 3 x 5 = 30` or Primorial = `30`.

Create a function that returns the Primorial of a number.

### Examples

    primorial(1) ➞ 2
    
    primorial(2) ➞ 6
    
    primorial(8) ➞ 9699690

### Notes

N/A

"""

import numpy as np
def primorial(n):
  i = 2
  lst = []
  while len(lst) < n:
    if is_prime(i):
      lst.append(i)
    i += 1
  return np.prod(lst)
    
​
def is_prime(n):
    if n <= 1:
      return n > 1
    true = []
    for i in range(2, n):
      true.append(n % i != 0)
    return all(true)

