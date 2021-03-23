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

def prime_factors(num):
    return [p for p in range(2,num//2+1) if num%p==0 and all(p%ii!=0 for ii in range(2,p//2+1))]
def c_fuge(n, k, factors=[]):
    factors = factors or prime_factors(n)
    if n<1 or k==1 or k<0 or not factors and n!=k:
        return False
    k = k if k < n/2 else n-k #balacing holes instead of items if necesary
    return n==k or k==0 or any(c_fuge(n, k-factor, factors) for factor in factors)

