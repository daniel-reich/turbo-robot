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

def ip(n):
  f = []
  for i in range(1, n):
    if n%i==0:f+=[i]
  return len(f)==1
def cuban_prime(num):
  a = []
  for y in range(100):
    a+=[3*y**2 + 3*y + 1]
  if num in a and ip(num): return str(num) + ' is cuban prime'
  else: return str(num) + ' is not cuban prime'

