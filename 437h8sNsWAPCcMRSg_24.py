"""


Write a function that returns `True` if the given number `num` is a product of
any two prime numbers.

### Examples

    product_of_primes(2059) ➞ True
    # 29*71=2059
    
    product_of_primes(10) ➞ True
    # 2*5=10
    
    product_of_primes(25) ➞ True
    # 5*5=25
    
    product_of_primes(999) ➞ False
    # There are no prime numbers.

### Notes

  * `num` is always greater than 0.
  * `0` and `1` aren't prime numbers.

"""

def product_of_primes(num):
    from functools import reduce
    from itertools import permutations
    primes_list = lambda N: list(reduce((lambda r, x: r - set(range(x ** 2, N, x)) if (x in r) else r),
                                        range(2, N), set(range(2, N))))
​
    perm = permutations(sorted(primes_list(round(num - 1))), 2)
​
    h = [True for i in perm if i[0] * i[1] == num or i[0] ** 2 == num or i[1] ** 2 == num]
    return True if True in h else False

