"""


Create a function that returns `True` if there's at least one prime number in
the given range (`n1` to `n2` (inclusive)), `False` otherwise.

### Examples

    prime_in_range(10, 15) ➞ True
    # Prime numbers in range: 11, 13
    
    prime_in_range(62, 66) ➞ False
    # No prime numbers in range.
    
    prime_in_range(3, 5) ➞ True
    # Prime numbers in range: 3, 5

### Notes

  * `n2` is always greater than `n1`.
  * `n1` and `n2` are always positive.
  * 0 and 1 aren't prime numbers.

"""

def is_prime(num):
  if num < 2:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True
​
def prime_in_range(n1, n2):
  for j in range(n1, n2 + 1):
    if is_prime(j):
      return True
  return False

