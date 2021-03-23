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
  a = []
  from math import sqrt; from itertools import count, islice
  def isPrime(n):
      return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
  for x in range(number):
    if isPrime(x): 
      while number%x==0:
        a.append(x)
        number  = number/x
  return a

