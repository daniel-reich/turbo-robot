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
  while 1:
    if is_prime(num): return num
    else: num += 1 
    
def is_prime(num):
  return all([num % i != 0 for i in range(2, num, 1)])

