"""


Create a function that finds how many prime numbers there are, up to the given
integer.

### Examples

    prime_numbers(10) ➞ 4
    # 2, 3, 5 and 7
    
    prime_numbers(20) ➞ 8
    # 2, 3, 5, 7, 11, 13, 17 and 19
    
    prime_numbers(30) ➞ 10
    # 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29

### Notes

N/A

"""

def prime_numbers(num):
  if num < 2:
    return 0
  return len([i for i in range(2,num+1) if is_prime(i)])
    
def is_prime(num):
  for i in range(2, num//2 + 1):
    if num % i == 0:
      return False
  return True

