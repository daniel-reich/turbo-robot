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

def primorial(n, p=2):
  if n == 1:
    return p
  return p * primorial(n-1, next_prime(p))
        
def next_prime(n):
  while True:
    n += 1
    if all(n%i != 0 for i in range(2, n)):
      return n

