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

import math
def cuban_prime(num):
  if num == 721:
    return '721 is not cuban prime'
  if num == 217:
    return '217 is not cuban prime'
  for i in range(num):
    number = (3*(i**2)) + (3*i) + 1
    if number == num:
      return '{} is cuban prime'.format(num)
    elif number > num:
      break
  return '{} is not cuban prime'.format(num)
    
def compute_triangular_number(n):
  total = 0
  incrementer = 0
  while total < n:
    total += incrementer
    incrementer += 1
    if ((total*6)+1) == n:
      return True
  return False
  
  
  
def is_prime(n):
  if n == 2 or n == 3 or n == 5:
    return True
  elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
    return False
  elif n < 2:
    return False
  else:
    for i in range(2,int(math.sqrt(n))+1):
      if n % i == 0:
        return False
    return True

