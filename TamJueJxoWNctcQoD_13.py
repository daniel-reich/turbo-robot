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

def both(num1,num2):
    if num1 > 0 and num2 > 0:
        return True
    if num1< 0 and num2 < 0:
        return True
    if num1 == 0 and num2 == 0:
        return True
    else:
        return False
both(0,2)

