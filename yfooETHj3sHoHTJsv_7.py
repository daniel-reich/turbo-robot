"""


Create a function that returns `True` when `num1` is equal to `num2`;
otherwise return `False`.

### Examples

    is_same_num(4, 8) ➞ False
    
    is_same_num(2, 2) ➞  True
    
    is_same_num(2, "2") ➞ False

### Notes

Don't forget to `return` the result.

"""

def is_same_num(num1, num2):
  if num1 == num2: 
      return True
  elif num1 != num2:
      return False

