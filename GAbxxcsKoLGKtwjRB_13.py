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
  mylst = []
  for j in lst:
    if j > 1: 
      isPrime = True
      for i in range(2, j): 
        if (j % i) == 0: 
          isPrime = False
          break
      if isPrime:
        mylst.append(j)
  x = sum(mylst)
  if x == 0:
    return None
  else:
    return x

