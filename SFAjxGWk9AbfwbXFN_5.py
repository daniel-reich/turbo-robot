"""


Create a function that will find all primes below a given number. Return the
result as a list.

### Examples

    primes_below_num(5) ➞ [2, 3, 5]
    
    primes_below_num(10) ➞ [2, 3, 5, 7]
    
    primes_below_num(20) ➞ [2, 3, 5, 7, 11, 13, 17, 19]

### Notes

If `n` is a prime, it is included in the list.

"""

def is_prime(n):
  if 2 < n < 4:
    return True
  for i in range(2, n):
    if n % i == 0:
      return False
  return True
​
def primes_below_num(n):
  primes_list = []
  for i in range(2, n + 1):
    if is_prime(i):
      primes_list.append(i)
  return primes_list

