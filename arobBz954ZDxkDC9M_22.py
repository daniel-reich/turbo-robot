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

def next_prime(num):
  if all(num % i for i in range(2, int(num**0.5) + 1)):
    return num
  else:
    return next_prime(num + 1)

