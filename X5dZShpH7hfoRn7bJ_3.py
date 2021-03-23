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

import itertools
def c_fuge(n, k):
  if n <= 1 or k <= 1 or k > n:
    return False
  elif n == k:
    return True
  else:     
    factors = get_prime_factors(n)
    possible_sums = set(sum(k) for i in range(1,len(factors)+1) for k in itertools.permutations(factors,i))
    if k in factors or n-k in factors or k in possible_sums:
      return True
  return False
  
def get_prime_factors(n):
  factors = []
  for i in range(2,n):
    while not n%i:
      factors.append(i)
      n //= i
  return factors

