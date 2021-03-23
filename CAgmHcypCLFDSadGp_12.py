"""


Write a function that returns `True` if a dictionary is empty, and `False`
otherwise.

### Examples

    is_empty({}) ➞ True
    
    is_empty({ "a": 1 }) ➞ False

### Notes

N/A

"""

def is_empty(dictionary):
  if dictionary == {}:
    return True
  else:
    return False

