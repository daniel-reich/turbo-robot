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

def isPrime(num):
  divisors = 0
  for i in range(1,num+1):
    if num%i == 0:
      divisors += 1
  if divisors == 2:
    return True
  else:
    return False
​
def sum_primes(lst):
  if len(lst) == 0:
    return None
  sum = 0
  for e in lst:
    if isPrime(e):
      sum += e
  return sum

