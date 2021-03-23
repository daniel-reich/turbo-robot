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

primes = []
def product_of_primes(num):
  def is_prime(n):
    n = int(n)
    if n >= 2:
      for num in range(2, n):
        if n%num == 0:
          return False
      return True
    return False
    
  if len(primes) != 0:
    for prime in primes:
      if num%prime == 0:
        if num/prime in primes or is_prime(num/prime):
          return True
    mp = max(primes)
  else:
    mp = 0
  
  for n in range(mp, num):
    if is_prime(n) == True:
      primes.append(int(n))
      if num%n == 0:
        other = int(num/n)
        if other in primes:
          return True
        if is_prime(other) == True:
          primes.append(other)
          return True
  
  return False

