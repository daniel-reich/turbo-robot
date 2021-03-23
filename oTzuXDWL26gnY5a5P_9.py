"""


Create a function that finds how many prime numbers there are, up to the given
integer.

### Examples

    prime_numbers(10) ➞ 4
    # 2, 3, 5 and 7
    
    prime_numbers(20) ➞ 8
    # 2, 3, 5, 7, 11, 13, 17 and 19
    
    prime_numbers(30) ➞ 10
    # 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29

### Notes

N/A

"""

import math
def is_prime(number):
  if number % 2 == 0 and number > 2:
    return False
  for i in range(3, int(math.sqrt(number)) + 1, 2):
    if number % i == 0:
      return False
  return True
    
def prime_numbers(num):
  count_prime = 0
  while num > 1:
    if is_prime(num):
      count_prime += 1
    num -= 1
  return count_prime

