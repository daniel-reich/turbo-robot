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

import numpy as np
def numpy_sieve(n):
    flags = np.ones(n,dtype=bool)
    flags[0] = flags[1] = False
    m = int(np.sqrt(n))+1
    for i in range(2,m):
        if flags[i]:
            flags[i*i::i] = False
    return np.flatnonzero(flags)
    
def moran(n):
  tot,x,primes = 0,n,numpy_sieve(1000)
  while x:
    x,r = divmod(x,10)
    tot += r
  return 'Neither' if n%tot else 'M' if n/tot in primes else 'H'

