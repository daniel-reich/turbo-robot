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

def checkBounds(lst, r, c):
    rows = len(lst)
    cols = len(lst[0])
    if((r >= 0) and (r < rows) and
       (c >= 0) and (c < cols)):
        return True
    return False
    
def checkPointsH(lst):
    res = []
    rows = len(lst)
    cols = len(lst[0])
​
    for r in range(0, rows):
        res.append((r, 0))
​
    for pnt in res:
        val = lst[pnt[0]][pnt[1]]
        r = pnt[0]
        for c in range(1, cols):
            if(lst[r][c] != val):
                return False
    return True
    
​
def checkPointsV(lst):
    res = []
    rows = len(lst)
    cols = len(lst[0])
​
    for c in range(0, cols):
        res.append((0, c))
​
    for pnt in res:
        val = lst[pnt[0]][pnt[1]]
        c = pnt[1]
        for r in range(1, rows):
            if(lst[r][c] != val):
                return False
    return True
​
def checkPointsL2R(lst):
    res = []
    rows = len(lst)
    cols = len(lst[0])
​
    for r in range(rows - 2, 0, -1):
        res.append((r,0))
    for c in range(0, cols):
        res.append((0,c))
    
    for pnt in res:
        val = lst[pnt[0]][pnt[1]]
        r = pnt[0]
        c = pnt[1]
        while True:
            r += 1
            c += 1
            if(not checkBounds(lst, r, c)):
                break
            if(lst[r][c] != val):
                return False
            
    return True
​
def checkPointsR2L(lst):
    res = []
    rows = len(lst)
    cols = len(lst[0])
​
    for c in range(1, cols):
        res.append((0,c))
    for r in range(1, rows - 1):
        res.append((r,cols-1))
    print(res)
    
    for pnt in res:
        val = lst[pnt[0]][pnt[1]]
        r = pnt[0]
        c = pnt[1]
        while True:
            r += 1
            c -= 1
            if(not checkBounds(lst, r, c)):
                break
            if(lst[r][c] != val):
                return False
            print("{} {} {} ".format(val, r, c))
    return True
​
def is_wristband(lst):
    rows = len(lst)
    cols = len(lst[0])
​
    # Horizontal
    if(checkPointsH(lst)):
        return True
​
    # Vertical
    if(checkPointsV(lst)):
        return True
​
    # L2R
    if(checkPointsL2R(lst)):
        return True
​
    # R2L
    if(checkPointsR2L(lst)):
        return True
    return False

