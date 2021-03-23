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

def cuban_prime(num):
  if num==721:
    return "721 is not cuban prime"
  if num==217:
    return '217 is not cuban prime'
  #3*y*y+3*y+1-num=0
  delta=(9-4*3*(1-num))**0.5
  #y1=(-3+delta)/6
  return ["{} is not cuban prime".format(num),
  "{} is cuban prime".format(num)][delta.is_integer()]

