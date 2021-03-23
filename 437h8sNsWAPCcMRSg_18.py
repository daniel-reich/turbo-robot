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
    primes = prime_sieve(num)
    for p in primes:
        if num/p in primes:
            return True
    return False
    
def prime_sieve(num):
    if num < 2:
        return []
    sieve = [True] * num
    sieve[0], sieve[1] = False, False
​
    for i in range(2, int(num ** 0.5) + 1):
        p = i * 2
        while p < num:
            sieve[p] = False
            p += i
    return [i for i in range(num) if sieve[i]]

