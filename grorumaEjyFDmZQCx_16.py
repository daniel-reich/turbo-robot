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

import numpy as np
def contains_set(lst):
  rows = list(map(lambda x: len(set(x))==1,lst))
  return all(rows)
def diagonal(lst):
  diagonals = list(map(lambda x: np.diag(lst,k = x),range(-len(lst)+1,len(lst[0])-1)))
  return contains_set(diagonals)
def is_wristband(lst):
  if contains_set(lst):
    return True
  elif contains_set(zip(*lst)):
    return True
  elif diagonal(lst):
    return True
  else:
    array = np.array(lst,str)
    array = np.rot90(array)
    return diagonal(array)

