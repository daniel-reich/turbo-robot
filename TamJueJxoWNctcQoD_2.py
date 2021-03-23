"""


Write a function that returns `True` if both numbers are:

  * Smaller than `0`, OR ...
  * Greater than `0`, OR ...
  * Exactly `0`

Otherwise, return `False`.

### Examples

    both(6, 2) ➞ True
    
    both(0, 0) ➞ True
    
    both(-1, 2) ➞ False
    
    both(0, 2) ➞ False

### Notes

Inputs will always be two numbers.

"""

def both(a,b):
  return a * b > 0 or a == b == 0

