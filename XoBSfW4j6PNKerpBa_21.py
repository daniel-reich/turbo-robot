"""


Create a function that decomposes an integer into its prime factors, ordered
from smallest to largest.

For instance:

    complete_factorization(24) = [2, 2, 2, 3]
    # Since 24 = 8 x 3 = 2^3 x 3 = 2 x 2 x 2 x 3

### Examples

    complete_factorization(10) ➞ [2, 5]
    
    complete_factorization(9) ➞ [3, 3]
    
    complete_factorization(72) ➞ [2, 2, 2, 3, 3]

### Notes

`1` is not considered a prime number, so omit it in your final list of prime
factors.

"""

def complete_factorization(num):
  def isPrime(n):
    for f in range(2, n // 2 + 1):
      if n % f == 0:
        return False
    return True
  
  factors = []
  f = 2
  while num > 1:
    if isPrime(f):
      while num % f == 0:
        factors.append(f)
        num //= f
    f += 1
  return factors

