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

def has_factors(n):
  if n<2:
    return True
  if n == 2:
    return False
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return True
  return False
​
def primorial(n):
  p = []
  s = 2
  while len(p) < n:
    if not has_factors(s):
      p.append(s)
    s += 1
  output = 1
  for i in p:
    output *= i
  return output

