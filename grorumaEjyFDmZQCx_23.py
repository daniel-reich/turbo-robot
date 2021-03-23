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
    rows = all(len(set(row)) == 1 for row in lst)
    cols = all(len(set(col)) == 1 for col in list(map(list,zip(*lst))))
    diag1 = all(len(set(diag)) == 1 for diag in [[row[i-j] for i,row in enumerate(lst) if 0 <= i-j < len(row)] for j in range(-len(lst[0])+1,len(lst))])
    diag2 = all(len(set(diag)) == 1 for diag in [[row[j-i] for i,row in enumerate(lst) if 0 <= j-i < len(row)] for j in range(len(lst[0])+len(lst)-1)])
    return any([rows,cols,diag1,diag2])

