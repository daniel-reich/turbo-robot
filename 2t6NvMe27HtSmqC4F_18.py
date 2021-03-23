"""


Write three functions:

  1. boolean_and
  2. boolean_or
  3. boolean_xor

These functions should evaluate a list of `True` and `False` values, starting
from the leftmost element and evaluating pairwise.

### Examples

    boolean_and([True, True, False, True]) ➞ False
    # [True, True, False, True] => [True, False, True] => [False, True] => False
    
    boolean_or([True, True, False, False]) ➞ True
    # [True, True, False, True] => [True, False, False] => [True, False] => True
    
    boolean_xor([True, True, False, False]) ➞ False
    # [True, True, False, False] => [False, False, False] => [False, False] => False

### Notes

  * `XOR` is the same as `OR`, except that it excludes `[True, True]`.
  * Each time you evaluate an element at 0 and at 1, you collapse it into the single result.

"""

def boolean_and(lst):
  if len(lst) == 2:
    return lst[0] and lst[1]
  else:
    return boolean_and([lst[0] and lst[1]] + lst[2:])
​
def boolean_or(lst):
  if len(lst) == 2:
    return lst[0] or lst[1]
  else:
    return boolean_or([lst[0] or lst[1]] + lst[2:])
​
def boolean_xor(lst):
  if len(lst) == 2:
    return lst[0] != lst[1]
  else:
    return boolean_xor([lst[0] != lst[1]] + lst[2:])

