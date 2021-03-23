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

def primes_below_num(n):
  def is_prime(n):
    for num in range(2, n):
      if n%num == 0:
        return False
    return True
  
  primes = []
  
  for num in range(2, n+1):
    p = is_prime(num)
    if p == True:
      primes.append(num)
  
  return primes

