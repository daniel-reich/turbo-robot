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

def prime_factorization(number):
  primes = sieve(number + 1)
  factors = []
  for p in primes:
    while number % p == 0:
      number = number // p
      factors.append(p)
  return factors
​
def sieve(n):
  a = [True] * n
  a[0] = a[1] = False
  primes = []
  for i, is_prime in enumerate(a):
    if is_prime:
      primes.append(i)
      for j in range(i*i, n, i):
        a[j] = False
  return primes

