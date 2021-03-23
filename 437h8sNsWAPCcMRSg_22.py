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

def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True
​
def product_of_primes(num):
​
  for i in range(2,num):
    if num % i == 0:
      j = num // i
      if is_prime(j) and is_prime(i):
        return True 
    
  return False

