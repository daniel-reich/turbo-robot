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
  n,m = len(lst),len(lst[0])
  dic = {(i,j):lst[i][j] for j in range(m) for i in range(n)}
  
  dirs = [(1,0),(0,1),(1,1),(1,-1)]
  
  return any(all(len(set(dic[(i+r*k,j+r*l)] for r in range(max(n,m)+2) if (i+r*k,j+r*l) in dic))==1 for (i,j) in dic) for (k,l) in dirs)

