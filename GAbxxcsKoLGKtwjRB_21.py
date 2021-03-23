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
  s = 0
  n = 0
  if len(lst) == 0:
    return None
  else:
    for i in lst:
      for j in range(2,i+1):
        if i%j == 0 and j != i :
          n = 0
          break
        else:
          n = i
​
      if n != 0:
        s += n
        n = 0
  return s

