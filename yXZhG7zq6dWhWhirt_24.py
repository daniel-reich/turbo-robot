"""


Create a function that takes a list and returns a new list containing only
prime numbers.

### Examples

    filter_primes([7, 9, 3, 9, 10, 11, 27]) ➞ [7, 3, 11]
    
    filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) ➞ [10007, 1009]
    
    filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) ➞ [1009, 3, 61, 1087, 1091, 1093, 1097]

### Notes

  * New list must maintain the order of primes as they first appear in the original list.
  * Check the **Resources** tab for help.

"""

def is_prime(n):
  if (n==1):
    return False
  for i in range(2,round(n**(0.5))+1):
    if i!=n and (n%i)==0:
      return False
  return True
  
def filter_primes(num):
  return [n for n in num if is_prime(n)]

