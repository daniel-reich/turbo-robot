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
  a = check_horizontal(lst)
  b = check_vertical(lst)
  c = check_left_diagonal(lst)
  d = check_right_diagonal(lst)
​
  if (a+b+c+d>0):
    return True
  else:
    return False
  
def check_horizontal(lst):
  for i in range(0,len(lst)):
    for j in range(0,len(lst[i])-1):
      if(lst[i][j] != lst[i][j+1]):
        return 0
  return 1
  
def check_vertical(lst):
  for i in range(0,len(lst[0])):
    for j in range(0,len(lst)-1):
      if(lst[j][i] != lst[j+1][i]):
        return 0
  return 1
​
def check_left_diagonal(lst):
  for i in range(0,len(lst)-1):
    for j in range(0,len(lst[0])-1):
      if(lst[i][j] != lst[i+1][j+1]):
        return 0
  return 1
    
def check_right_diagonal(lst):
  for i in range(0,len(lst)-1):
    for j in range(0,len(lst[0])-1):
      if(lst[len(lst)-i-1][j] != lst[len(lst)-i-2][j+1]):       
        return 0
  return 1

