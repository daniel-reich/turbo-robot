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
  prime_lst = []
  for i in range(n1, n2 + 1):
    prime = True
    if i == 1:
      prime = False
    elif prime == 2:
      prime = True
    else:
      for j in range(2, i):
        if i % j == 0:
          prime = False
          break
    if prime == True:
      prime_lst.append(i)
  if len(prime_lst) != 0:
    return True
  else:
    return False

