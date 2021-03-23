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
    res = []
    while not num % 2:
        num //= 2
        res += [2]
    divisor = 3
    while num > 1:
        while not num % divisor:
            num //= divisor
            res += [divisor]
        divisor += 2
    return list(set(res))
​
​
def c_fuge(n, k):
    if n == 1 or k == 1:
        return False
    elif n == k:
        return True
    n_factors = prime_factors(n)
    if len(n_factors) > 1:
        n_factors.append(n_factors[0] + n_factors[1])
        n_factors.append(n_factors[0] + n_factors[2])
    k_factors = prime_factors(k)
    nk_factors = prime_factors(n - k)
    return (any(f in k_factors for f in n_factors)
            and any(f in nk_factors for f in n_factors))

