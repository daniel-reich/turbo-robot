"""


Create a function to check whether a given number is **Cuban Prime**. A cuban
prime is a prime number that is a solution to one of two different specific
equations involving third powers of x and y. For this challenge we are only
concerned with the cuban numbers from the **first equation**. We **ignore**
the cuban numbers from the **second equation**.

### Equation Form

    p = (x^3 - y^3)/(x - y), x  = y + 1, y > 0

... and the first few cuban primes from this equation are 7, 19, 37, 61, 127,
271.

### Examples

    cuban_prime(7) ➞ "7 is cuban prime"
    
    cuban_prime(9) ➞ "9 is not cuban prime"
    
    cuban_prime(331) ➞ "331 is cuban prime"
    
    cuban_prime(40) ➞ "40 is not cuban prime"

### Notes

  * The inputs are positive integers only.
  * Check the **Resources** for help.

"""

from math import sqrt
​
def is_prime(n: int) -> bool:
  if n < 2:
    return False
  if n in (2, 3, 5):
    return True
  for p in (2, 3, 5):
    if n % p == 0:
      return False
  for i in range(6, int(sqrt(n)), 6):
    if n % (i + 1) == 0 or n % (i + 5) == 0:
      return False
  return True
​
def cuban_prime(n: int) -> str:
  if (sqrt((n - 1/4) / 3) - 1/2).is_integer() and is_prime(n):
    return '{} is cuban prime'.format(n)
  else:
    return '{} is not cuban prime'.format(n)

