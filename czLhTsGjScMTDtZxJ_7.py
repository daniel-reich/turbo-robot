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

def is_prime(n):
  if n == 2: return True
  if not n % 2: return False
  for i in range(3, int(n ** 0.5) + 1, 2):
    if not n % i: return False
  return True
​
def primorial(n):
  ans, i, m = 1, 0, 2
  while i < n:
    if is_prime(m):
      ans *= m
      i += 1
    m += 1
  return ans

