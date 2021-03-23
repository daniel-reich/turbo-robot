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
    i = 1
    j = 1
​
    while i * j < num:
        i = next_prime(i)
        while i*j < num:
             j = next_prime(j)
​
        if i*j == num:
            return True
        j = 2
​
    return False
​
​
def next_prime(prime):
    a = prime + 1
    while not is_prime(a):
        a += 1
    return a
​
​
def is_prime(num):
    if num == 1 or num == 0:
        return False
    i = 2
    while i < num - 1:
        if num % i == 0:
            return False
        i += 1
    return True

