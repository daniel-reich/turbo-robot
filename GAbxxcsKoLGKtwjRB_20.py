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
  x = []
  if lst:
    for i in lst:
      if i > 1:
        t = 0
        for y in range(1, i//2 + 1):
          if i % y == 0:
            t += 1
        if t <=1:
          x.append(i)
  else:
    return None
  return sum(x)

