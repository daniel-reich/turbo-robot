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

def check_horizontal(lst):
    for i in lst:
        if len(set(i)) != 1:
            return False
    return True
​
def check_vertical(lst):
    for i in range(0,len(lst[0])):
        vertical = []
        for y in range(len(lst)):
            vertical.append(lst[y][i])
        if len(set(vertical)) != 1:
            return False
    return True
        
def check_diagonal_right(lst):
    for i in range(0,len(lst)):
        for y in range(0,len(lst[i])):
            if i > 0 and i < len(lst)-1 and y == 0:
                if lst[i][y] != lst[i-1][y+1]:
                    return False
            elif i > 0 and i < len(lst)-1 and y == len(lst[i])-1:
                if lst[i][y] != lst[i+1][y-1]:
                    return False
            elif i > 0 and i < len(lst)-1 and y > 0 and y < len(lst[i])-1:
                if lst[i][y] != lst[i-1][y+1] or lst[i][y] != lst[i+1][y-1]:
                    return False
    return True
​
def check_diagonal_left(lst):
    for i in range(0,len(lst)):
        for y in range(0,len(lst[i])):
            if i > 0 and i < len(lst)-1 and y == 0:
                if lst[i][y] != lst[i+1][y+1]:
                    return False
            elif i > 0 and i < len(lst)-1 and y == len(lst[i])-1:
                if lst[i][y] != lst[i-1][y-1]:
                    return False
            elif i > 0 and i < len(lst)-1 and y > 0 and y < len(lst[i])-1:
                if lst[i][y] != lst[i-1][y-1] or lst[i][y] != lst[i+1][y+1]:
                    return False
    return True
​
def is_wristband(lst):
    return check_horizontal(lst) or check_vertical(lst) or check_diagonal_left(lst) or check_diagonal_right(lst)

