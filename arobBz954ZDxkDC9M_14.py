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

def isPrime(val):
  for i in range(2, val):
    if val % i == 0: return False
    else: continue
  return True
​
def next_prime(val):
  for i in range(val, val+100):
    if isPrime(i): return i
    else: continue
  return False

