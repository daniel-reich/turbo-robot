"""


A wristband can have 4 patterns:

  1. **horizontal** : each item in a row is identical.
  2.  **vertical** : each item in each column is identical.
  3.  **diagonal left** : each item is identical to the one on it's upper left or bottom right.
  4.  **diagonal right** : each item is identical to the one on it's upper right or bottom left.

You are shown an **incomplete section** of a wristband.

Write a function that returns `True` if the section can be correctly
classified into one of the 4 types, and `False` otherwise.

### Examples

    is_wristband([
      ["A", "A"],
      ["B", "B"],
      ["C", "C"]
    ]) ➞ True 
    # Part of horizontal wristband.
    
    is_wristband([
      ["A", "B"],
      ["A", "B"],
      ["A", "B"]
    ]) ➞ True 
    # Part of vertical wristband.
    
    is_wristband([
      ["A", "B", "C"],
      ["C", "A", "B"],
      ["B", "C", "A"],
      ["A", "B", "C"]
    ]) ➞ True
    # Part of diagonal left wristband.
    
    is_wristband([
      ["A", "B", "C"],
      ["B", "C", "A"],
      ["C", "A", "B"],
      ["A", "B", "A"]
    ]) ➞ True
    # Part of diagonal right wristband.

### Notes

N/A

"""

def is_wristband(lst):
    
    horizontal = list(dict.fromkeys([len(list(dict.fromkeys(i))) for i in lst]))#horizontal
    vertical = list(dict.fromkeys([len(list(dict.fromkeys(i))) for i in [[j[i] for j in lst] for i in range(len(lst[0]))]])) #vertical
    leftright = list(dict.fromkeys([len(list(dict.fromkeys(i))) for i in [[c for c in r if c is not None] for r in zip(*[([None] * (len(lst) - 1))[i:] + r + ([None] * (len(lst) - 1))[:i] for i, r in enumerate(lst)])]]))
    rightleft = list(dict.fromkeys([len(list(dict.fromkeys(i))) for i in [[c for c in r if c is not None] for r in zip(*[([None] * (len(lst) - 1))[:i] + r + ([None] * (len(lst) - 1))[i:] for i, r in enumerate(lst)])]]))
​
    return True if [1] in [horizontal, vertical, leftright, rightleft] else False

