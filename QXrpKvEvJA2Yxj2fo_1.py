"""


Create a function that returns the number of arguments it was called with.

### Examples

    num_args() ➞ 0
    
    num_args("foo") ➞ 1
    
    num_args("foo", "bar") ➞ 2
    
    num_args(True, False) ➞ 2
    
    num_args({}) ➞ 1

### Notes

  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def num_args(*args, **kwargs):
  return len(args) + len(kwargs)

