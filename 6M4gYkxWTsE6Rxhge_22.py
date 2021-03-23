"""


Create a function thats takes a list and returns `True` if every number is
prime. Otherwise, return `False`.

### Examples

    all_prime([7, 5, 2, 4, 6]) ➞ False
    
    all_prime([2, 3, 5, 7, 13, 17, 19, 23, 29]) ➞ True
    
    all_prime([1, 5, 3]) ➞ False

### Notes

1 is not a prime number.

"""

def all_prime(lst):
  return all(is_prime(i) for i in lst)
  
def is_prime(val):
  if val < 2:
    return False
  else:
    for i in range(2, val//2 + 1):
      if not val % i:
        return False
    return True

