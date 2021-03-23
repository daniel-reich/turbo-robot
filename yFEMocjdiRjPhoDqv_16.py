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

def prime_in_range(n1, n2):
  def is_prime(number):
    if number == 2:
      return True
    if number < 2 or number % 2 == 0:
      return False
    for num in range(3, int(number**0.5) + 1, 2):
      if number % num == 0:
        return False
    return True
  
  for num in range(n1, n2 + 1):
    if is_prime(num):
      return True
  return False

