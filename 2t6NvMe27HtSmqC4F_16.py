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
  if False in lst:
    return False
  else:
    return True
​
def boolean_or(lst):
  if True in lst:
    return True
  else:
    return False
def boolean_xor(lst):
  ret=lst[0]
  for x in range(1,len(lst)):
    if lst[x]==True:
      if ret==True:
        ret=False
      else:
        ret=True
    elif lst[x]==False:
      if ret==False:
        ret=False
      else:
        ret=True
    else:
      ret=True
  return ret

