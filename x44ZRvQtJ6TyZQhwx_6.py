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
  num_str = str(n)
  count = 0
  for i in range(0, 10):
    if num_str.count("{}".format(i)) >= 1:
      count += 1
  if count == 10:
    return True
  else:
    return False

