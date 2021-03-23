"""


Create a function that takes a number as its only argument and returns `True`
if it's less than or equal to zero, otherwise return `False`.

### Examples

    less_than_or_equal_to_zero(5) ➞ False
    
    less_than_or_equal_to_zero(0) ➞ True
    
    less_than_or_equal_to_zero(-2) ➞ True

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def less_than_or_equal_to_zero(num):
  if num <= 0:
    return True 
  else:
    return False

