"""


Given a number, return all its prime divisors in a list. Create a function
that takes a number as an argument and returns all its prime divisors.

  * n = 27
  * All divisors: `[3, 9, 27]`
  * Finally, from that list of divisors, return the prime ones: `[3]`

### Examples

    prime_divisors(27) ➞ [3]
    
    prime_divisors(99) ➞ [3, 11]
    
    prime_divisors(3457) ➞ [3457]

### Notes

N/A

"""

import math
def isPrime(n):
    if n == 1 or n == 0 :
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i ==0:
            return False
    return True
def prime_divisors(num):
    return [i for i in range(2,num + 1) if num%i == 0 and  isPrime(i) ==True ]

