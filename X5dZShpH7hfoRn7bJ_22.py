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

# The Centrifuge Problem
import itertools
import math
def prime(num):
    if num == 2:
        return True
    max_trial = math.ceil(num ** (1/2))
    for number in range(2, max_trial + 1):
        if num % number == 0:
            return False
    return True
def prime_factors(num):
    prime_numbers = []
    for i in range(2, num + 1):
        if num % i == 0 and prime(i):
            prime_numbers.append(i)
    return prime_numbers
​
def c_fuge(holes, tubes):
    primes = prime_factors(holes)
    
    possibilities = set()
    for level in range(0, holes + 1):
        primes = prime_factors(holes) * level
        for items in [sum(item) for item in list(itertools.combinations(primes, level)) if sum(item) <= holes]:
            possibilities.add(items)
    return tubes in possibilities and (holes - tubes) in possibilities

