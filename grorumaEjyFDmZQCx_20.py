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
  
  for i in lst:
    print(i)
  horizontal=lst
  horizontal=[i for i in horizontal if len(set(i))==1]
  if len(horizontal)==len(lst): 
    print('check')
    return True
  vertical=set([str(i) for i in lst])
  if len(vertical)==1: return True
  rightdiag=True
  for i in range(len(lst)-1):
    for x in range(len(lst[i])-1):
      if lst[i][x]!=lst[i+1][x+1]: 
        print(lst[i][x],lst[i+1][x+1])
        rightdiag=False
        break
    if rightdiag==False: break
  if rightdiag==True: 
    return True
  leftdiag=True
  for i in range(len(lst)-1):
    for x in range(1,len(lst[i])):
      if lst[i][x]!=lst[i+1][x-1]: 
        print(lst[i][x],lst[i+1][x-1])
        leftdiag=False
        break
      print(lst[i][x],lst[i+1][x-1])
    if leftdiag==False: break
  if leftdiag==True: return True
  return False

