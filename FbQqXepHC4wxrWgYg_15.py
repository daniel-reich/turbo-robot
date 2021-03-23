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
def check_prime(n):
    if n <= 0:
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
​
def prime_divisors(num):
    result = []
    for i in range(2, num//2):
        if num % i == 0 and check_prime(i):
            result.append(i)
    if check_prime(num):
        result.append(num)
    return result

