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

def c_fuge(n, k):
  lst = prime_facts(n)
  poss = {0}
  for p in lst:
    poss = {a+b for a in poss for b in range(0,n+1,p) if a+b<=n}
  return k in poss and n-k in poss  
​
def prime_facts(n):
  ans = []
  for p in range(2,n+1):
    if n%p == 0 and all(p%k for k in ans): ans+=[p]
  return ans

