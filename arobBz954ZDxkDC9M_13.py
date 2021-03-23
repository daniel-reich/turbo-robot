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
  cond = 2**(num-1) % num == 1
  if cond:
    return num
  else:
    while(not cond):
      num += 1
      cond = 2**(num-1) % num == 1
    return num

