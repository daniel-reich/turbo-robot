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
  for i in range(num):
    cur = cuban_eq(i,i+1)
    if cur==num and is_prime(cur):
      return '{0} is cuban prime'.format(num)
  return '{0} is not cuban prime'.format(num)
  
​
def cuban_eq(x,y):
  return (pow(x,3) - pow(y,3))/(x - y)
​
def is_prime(n):
  if n<2:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

