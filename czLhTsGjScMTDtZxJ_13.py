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

is_prime = lambda x : all(x % i for i in range(2,x))
​
def primorial(n):
  primes = []
  x = 2
  while(n):
    if is_prime(x):
      primes.append(x)
      n -= 1
    x += 1  
  prod = primes[0]
  for i in range(1, len(primes)):
    prod *= primes[i]
  return prod

