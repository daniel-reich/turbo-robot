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

def sum_primes(lst):
  res = 0
  for x in lst:
    if (x == 2):
      res = res + 2
    for a in range (2, x):
      if (x % a == 0):
        break
      if (a == x - 1):
        res = res + x
  if (res == 0):
    return None
  return res

