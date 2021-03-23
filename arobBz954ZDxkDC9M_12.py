"""


Given an integer, create a function that returns the next prime. If the number
is prime, return the number itself.

### Examples

    next_prime(12) ➞ 13
    
    next_prime(24) ➞ 29
    
    next_prime(11) ➞ 11
    # 11 is a prime, so we return the number itself.

### Notes

N/A

"""

def isPrime(n):
  i = 2
  tallies = 0
  while n > i:
    if n%i == 0:
      tallies += 1
    i += 1
  return(tallies==0)
​
def next_prime(num):
  if isPrime(num):
    return num
  else:
    return next_prime(num+1)

