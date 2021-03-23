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

def is_prime(n):
  if n == 1:
    return False
  for i in range(2, n // 2 + 1):
    if n % i == 0:
      return False
  return True
​
def sum_primes(lst):
  prime_lst = list(filter(is_prime, lst))
  if prime_lst == []:
    return None
  return sum(prime_lst)

