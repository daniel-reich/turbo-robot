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

def isEven(n): 
  for i in range(2, n): 
    if n % i == 0: 
        return True
​
  return False
​
def sum_primes(lst): 
  if lst == []:
    return None
​
  total = 0
  for i in lst:
    if i == 1:
      continue
    if not isEven(i):
      total += i
​
  return total

