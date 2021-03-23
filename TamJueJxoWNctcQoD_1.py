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

def both(n1, n2):
    return (n1 > 0 and n2 > 0) or (n1 == 0 and n2 == 0) or (n1 < 0 and n2 < 0)

