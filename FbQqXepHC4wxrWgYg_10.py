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

from math import sqrt
def prime_divisors(num):
  for i in range(2,int(sqrt(num)) + 1):
    if num % i == 0:
      return sorted(list(set([i] + prime_divisors(num // i))))
  return [num]

