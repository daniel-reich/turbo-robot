"""


Create a function that returns `True` if an integer is evenly divisible by 5,
and `False` otherwise.

### Examples

    divisible_by_five(5) ➞ True
    
    divisible_by_five(-55) ➞ True
    
    divisible_by_five(37) ➞ False

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def divisible_by_five(n):
  if (n % 5 == 0):
    return True
  else:
    return False

