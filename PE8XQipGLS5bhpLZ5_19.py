"""


Programmer Pete is trying to create a function that returns `True` if two
lists share the same length and have identical numerical values at every
index, otherwise, it will return `False`.

However, the solution his function gives is in an unexpected format. Can you
fix Pete's function so that it behaves as seen in the examples below?

### Examples

    check_equals([1, 2], [1, 3]) ➞ False
    
    check_equals([1, 2], [1, 2]) ➞ True
    
    check_equals([4, 5, 6], [4, 5, 6]) ➞ True
    
    check_equals([4, 7, 6], [4, 5, 6]) ➞ False
    
    check_equals([1, 12], [11, 2]) ➞ False

### Notes

Check the **Resources** tab for more info.

"""

def check_equals(lst1, lst2):
  return len(lst1)==len(lst2) and lst1==lst2

