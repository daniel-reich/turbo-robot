"""


In mathematics, primorial, denoted by “#”, is a function from natural numbers
to natural numbers similar to the factorial function, but rather than
successively multiplying positive integers, the function only multiplies
**prime numbers**.

Create a function that takes an integer `n` and returns its **primorial**.

### Examples

    primorial(1) ➞ 2
    # First prime number = 2
    
    primorial(2) ➞ 6
    # Product of first two prime numbers = 2*3 = 6
    
    primorial(6) ➞ 30030

### Notes

n >= 1.

"""

from functools import reduce
def gen_primes(n):
    primes, k = {2}, 3
    while len(primes) < n:
        if all(k % p > 0 for p in primes):
            primes.add(k)
        k += 2
    return sorted(primes)
​
lst_primes = gen_primes(10)
​
def primorial(n):
    return reduce(lambda a, b: a * b, lst_primes[:n])

