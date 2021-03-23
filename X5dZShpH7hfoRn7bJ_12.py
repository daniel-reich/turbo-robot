"""


A centrifuge, as you probably know, is a laboratory device used to separate
fluids based on density. The separation is achieved through centripetal force
by spinning a collection of test tubes at high speeds. This means, the
configuration needs to be in balance.

Create a function that takes two numbers as arguments `n` and `k` and returns
`True` if the configuration is balanced and `False` if it's not. To check out
the formula, look at the **resources tab**.

![The Centrifuge Problem with 6 Holes, n=6](https://edabit-
challenges.s3.amazonaws.com/6_hole_centrifuge.png)

Here are the valid configurations for _n_ = 6, _k_ = 2, 3, 4 and 6.

### Examples

    c_fuge(6, 4) ➞ True
    
    c_fuge(2, 1) ➞ False
    
    c_fuge(3, 3) ➞ True

### Notes

  * One test tube `k = 1` is **never** in balance.
  * One hole `n = 1` is **never** in balance, even empty.

"""

from math import ceil
from fractions import gcd
from itertools import combinations_with_replacement as cwr
​
def prime_factors(n):
    pfs = []
    while n%2 == 0:
        pfs.append(2)
        n /= 2
    lim = int(n**0.5) + 1
    for i in range(3, lim, 2):
        while n%i == 0:
            pfs.append(i)
            n /= i
    return pfs + [int(n)] if n > 2 else pfs
​
def has_prime_sum(pfn, k):
    if any(k%f == 0 for f in pfn): return True
    for n in range(2, ceil(k / min(pfn))):
        if any(True for c in cwr(pfn, n) if sum(c) == k): return True
    return False
​
def c_fuge(n, k):
    if k == 1 or n-k == 1: return False
    if n>1 and gcd(k,n) > 1: return True
    pfn = set(prime_factors(n))
    if len(pfn) == 1: return False
    return has_prime_sum(pfn, k) and has_prime_sum(pfn, n-k)

