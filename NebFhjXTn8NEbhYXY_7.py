"""


Create a function that takes an integer and return `True` if it's divisible by
100, otherwise return `False`.

### Examples

    divisible(1) ➞ False
    
    divisible(1000) ➞ True
    
    divisible(100) ➞ True

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def divisible(num):
  if num%100==0:
    return True  
  else:
    return False

