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

from operator import xor
def boolean_and(lst):
    a = lst[0]
    for i in range(1, len(lst)):
        a = (a and lst[i])
    return a
​
​
def boolean_or(lst):
    a = lst[0]
    for i in range(1, len(lst)):
        a = (a or lst[i])
​
    return a
​
​
​
​
​
def boolean_xor(lst):
    a = lst[0]
    for i in range(1, len(lst)):
        a = xor(a,lst[i])
​
    return a

