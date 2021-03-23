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
  i= [2,3,5,7]
  retorn = []
  for x in lst:
    if x!=1:
      retorn.append(x)
    for c in i:
      if x % c == 0 and x != c:
        retorn.pop(-1)
        break
  return sum(retorn) if len(lst) > 0 else None

