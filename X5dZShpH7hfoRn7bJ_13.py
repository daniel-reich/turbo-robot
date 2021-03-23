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

from itertools import combinations_with_replacement
def c_fuge(n, k):
  if n == 1 or k == 1: return False
  pn = prime_divisors(n)
  cs = [sum(comb) for i in range(n) for comb in combinations_with_replacement(pn, i) ]
  return k in cs and n-k in cs
​
def prime_divisors(n):
  ret = []
  while n % 2 == 0:
    ret.append(2)
    n = n//2
  
  for i in range(3, n//2, 2):
    if n % i == 0:
      ret.append(i)
      n = n//i
  if n > 2:
    ret.append(n)
​
  return ret

