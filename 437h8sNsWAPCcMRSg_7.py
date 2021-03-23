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
  import math as m
  prime_factors=[]
  while num % 2 == 0:
    num = num / 2
    prime_factors.append(2)
  for i in range(3,int(m.sqrt(num)+1),2):
    while num % i == 0:
      num = num / i
      prime_factors.append(i)
  if num > 2:
    prime_factors.append(num)
  if len(prime_factors) == 2:
    return True
  else:
    return False

