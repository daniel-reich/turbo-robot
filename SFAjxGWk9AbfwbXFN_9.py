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

def is_prime(num):
  for i in range(2, int(num ** 0.5)+1):
    if num % i == 0:
      return False
  else:
    return True
​
def primes_below_num(n):
  return [num for num in range(2,n+1) if is_prime(num)]

