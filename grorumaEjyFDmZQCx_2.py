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
  h = len(lst)
  w = len(lst[0])
  if all(row.count(row[0]) == len(row) for row in lst):
    return True
  if all(col.count(col[0]) == len(col) for col in zip(*lst)):
    return True
    
  left = right = True
  for i in range(h):
    for j in range(w):
      if i > 0 and j > 0 and lst[i][j] != lst[i-1][j-1]:
        left = False
      if i > 0 and j < w-1 and lst[i][j] != lst[i-1][j+1]:
        right = False
    
  return left or right

