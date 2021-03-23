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
    diagonal_left=[]
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if i>0 and j>0:
                if lst[i][j]==lst[i-1][j-1]:
                    diagonal_left.append(True)
​
    diagonal_right=[]
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if i>0 and j>0:
                if lst[::-1][i][j]==lst[::-1][i-1][j-1]:
                    diagonal_right.append(True)
​
​
    is_horizontal=[]
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if j!=0 and lst[i][j]==lst[i][j-1]:
                is_horizontal.append(True)
​
    is_vertical=[]
​
    for j in range(len(lst[0])):
        for i in range(len(lst)):
            if i!=0 and lst[i][j]==lst[i-1][j]:
                is_vertical.append(True)
    if sum(is_horizontal)==(i+1)*(j):
        return True
    elif sum(is_vertical)==i*(j+1):
        return True
​
    elif sum(diagonal_left)==i*j:
        return True
    elif sum(diagonal_right)==i*j:
        return True
    else:
        return False

