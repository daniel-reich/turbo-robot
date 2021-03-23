"""


Create a function that takes a list of numbers and returns the **sum** of all
**prime numbers** in the list.

### Examples

    sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
    
    sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
    
    sum_primes([]) ➞ None

### Notes

  * Given numbers won't exceed 101.
  * A prime number is a number which has exactly two divisors.

"""

import math
def sum_primes(series):
  if not series:
    return None
  primes = primes_upto(max(series))
  return sum(element for element in series if element in primes)
​
def primes_upto(n):
  if n <= 1:
    return list() 
  return [number for number in range(2, n+1) if is_prime(number)]
​
​
def is_prime(n):
  if n <= 1:
    return False
  elif n <= 3:
    return True
​
  for i in range(2, int(math.sqrt(n)+1)):
    if n % i == 0:
      return False
  return True

