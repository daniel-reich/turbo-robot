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

def primes(num):
  primes = [2]
  number = 3
  while number <= num/2:
    if not any([number%p == 0 for p in primes]):
      primes.append(number)
    number += 2
  return primes
    
def product_of_primes(num):
  prim = primes(num)
  print(prim)
  return any([p*q == num for p in prim for q in prim])

