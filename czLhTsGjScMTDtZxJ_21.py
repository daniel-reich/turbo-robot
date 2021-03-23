"""


In mathematics, primorial, denoted by “#”, is a function from natural numbers
to natural numbers similar to the factorial function, but rather than
successively multiplying positive integers, the function only multiplies
**prime numbers**.

Create a function that takes an integer `n` and returns its **primorial**.

### Examples

    primorial(1) ➞ 2
    # First prime number = 2
    
    primorial(2) ➞ 6
    # Product of first two prime numbers = 2*3 = 6
    
    primorial(6) ➞ 30030

### Notes

n >= 1.

"""

import numpy
def primorial(n):
  primes = []
  k = n*n if n>2 else 2
  for possiblePrime in range(2, n+k):
    isPrime = True
    for num in range(2, possiblePrime):
      if possiblePrime % num == 0:
        isPrime = False 
    if isPrime:
      primes.append(possiblePrime)
  return numpy.prod(primes[:n])

