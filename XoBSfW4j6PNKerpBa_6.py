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

def complete_factorization(number):
  primes = [2,3]
  arr = []
  for i in range(4,number+1):
    if is_prime(i):
      primes.append(i)
  while number > 1:
    for x in primes:
      if number % x == 0:
        number /= x
        arr.append(x)
  return sorted(arr)
    
def is_prime(num):
    for i in range(2,num):
      if num % i == 0:
        return False
    return True

