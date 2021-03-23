"""


Create a function that returns `True` if the given string has any of the
following:

  * Only letters and no numbers.
  * Only numbers and no letters.

If a string has **both** numbers and letters, or contains characters which
don't fit into any category, return `False`

### Examples

    alphanumeric_restriction("Bold") ➞ True
    
    alphanumeric_restriction("123454321") ➞ True
    
    alphanumeric_restriction("H3LL0") ➞ False
    
    alphanumeric_restriction("ed@bit") ➞ False

### Notes

Any string that contains spaces or is empty should return `False`.

"""

def alphanumeric_restriction(s):
  isalpha = False
  isnum = False
  if len(s) == 0:
    return False
  for i in s:
    if i.isalpha() == True:
      isalpha = True
    elif i.isnumeric() == True:
      isnum = True
    else:
      return False
    if isalpha == True and isnum == True:
      return False
      
  return True

