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

import math
​
def primorial(n):
  count = 0
  increment = 2
  total = 1
  while count != n:
    if is_prime(increment):
      total = total * increment
      count += 1
      increment += 1
    else:
      increment += 1
  return total
  
  
def is_prime(n):
  if n == 2 or n == 3 or n == 5:
    return True
  elif n < 2:
    return False
  elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
    return False
  else:
    for i in range(2,int(math.sqrt(n))+1):
      if n % i == 0:
        return False
    return True

