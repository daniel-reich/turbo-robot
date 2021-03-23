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

def is_prime(num):
  if num==1:
    return False
  i=2
  while i*i<=num:
    if num%i==0:
      return False
    i+=1
  return True
​
def all_prime(lst):
  return all(is_prime(i) for i in lst)

