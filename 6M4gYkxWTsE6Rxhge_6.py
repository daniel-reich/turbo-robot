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

def prime_num(n):
​
  if n > 1:
    for i in range(2, n):
      if n % i == 0:
        return False
    return True
  else:
    return False
​
​
​
def all_prime(lst):
  ans = [prime_num(i) for i in lst]
  return all(ans)

