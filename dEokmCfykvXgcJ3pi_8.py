"""


Write two functions:

  1. `first_arg()` should return the first parameter passed in.
  2. `last_arg()` should return the last parameter passed in.

### Examples

    first_arg(1, 2, 3) ➞ 1
    
    last_arg(1, 2, 3) ➞ 3
    
    first_arg(8) ➞ 8
    
    last_arg(8) ➞ 8

### Notes

  * Return `None` if the function takes no parameters.
  * If the function only takes in one parameter, the `first_arg` and `last_arg` functions should return the same value.

"""

def first_arg(*args):
  if not args:
    return None
  return args[0]
​
def last_arg(*args):
  if not args:
    return None
  return args[-1]

