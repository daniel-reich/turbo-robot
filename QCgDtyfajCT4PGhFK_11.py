"""


Write a function that returns the extended form of the prime factorization of
a number. Return in the format `[a, b, c, d, ...]`, where each element of the
list is an integer.

### Examples

    prime_factorization(216) ➞ [2, 2, 2, 3, 3, 3]
    
    prime_factorization(64) ➞ [2, 2, 2, 2, 2, 2]
    
    prime_factorization(23) ➞ [23]

### Notes

N/A

"""

def prime_factorization(n):
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
  factors = []
  while n > 1:
    for p in primes:
      if not n % p:
        n //= p
        factors.append(p)
        break
  return factors

