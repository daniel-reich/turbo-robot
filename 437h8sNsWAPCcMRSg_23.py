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
  import math
  primes = []
  n = num
  while n % 2 == 0:
    primes.append(2)
    n = n / 2
  for i in range(3, num, 2):
    while n%i==0:
      primes.append(i)
      n = n/i
  for idx,i in enumerate(primes):
    for j in range(idx):
      if i * primes[j] == num:
        return True
  return False

