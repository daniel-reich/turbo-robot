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

c = []
for i in range(2,5000):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        c.append(i)
def cuban_prime(num):
    p = [1+3*y*(y+1) for y in range(1,100)]
    return '{} is cuban prime'.format(num) if num in set(c) & set(p) else '{} is not cuban prime'.format(num)

