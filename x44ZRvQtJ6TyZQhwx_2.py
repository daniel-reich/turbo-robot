"""


A **pandigital** number contains all digits (0-9) at least once. Write a
function that takes an integer, returning `True` if the integer is pandigital,
and `False` otherwise.

### Examples

    is_pandigital(98140723568910) ➞ True
    
    is_pandigital(90864523148909) ➞ False
    # 7 is missing.
    
    is_pandigital(112233445566778899) ➞ False

### Notes

Think about the properties of a pandigital number when all duplicates are
removed.

"""

def is_pandigital(n):
  for i in range (10):
    if str(i) not in str(n):
      return False
  return True

