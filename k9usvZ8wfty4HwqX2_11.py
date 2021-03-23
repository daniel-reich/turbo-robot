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

def c_prime(y):
    x = y+1
    p = int((x**3-y**3)/(x-y))
    for i in range(2, p):
        if p % i == 0:
            x += 1
            y += 1
            p = int((x**3-y**3)/(x-y))
            continue 
    return p
​
def cuban_prime(num):
    for numbers in range(1, num):
        if c_prime(numbers) > num:
            break
        if c_prime(numbers) == num:
            return str(num) + " is cuban prime"
    return str(num) + " is not cuban prime"

