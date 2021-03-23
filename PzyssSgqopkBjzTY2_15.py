"""


A maze can be represented by a 2D matrix, where `0`s represent **walkeable**
areas, and `1`s represent walls. You start on the upper left corner and the
exit is on the most lower right cell.

Create a function that returns `true` if you can walk from one end of the maze
to the other. You can only move up, down, left and right. You **cannot move
diagonally**.

### Examples

    can_exit([
      [0, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 1, 0, 1, 1],
      [1, 0, 0, 0, 0, 1, 1],
      [1, 1, 1, 1, 0, 0, 1],
      [1, 1, 1, 1, 1, 0, 0]
    ]) ➞ true
    
    can_exit([
      [0, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 0, 0, 1, 1],
      [1, 0, 0, 0, 0, 1, 1],
      [1, 1, 0, 1, 0, 0, 1],
      [1, 1, 0, 0, 1, 1, 1]
    ]) ➞ false
    
    # This maze only has dead ends!
    
    can_exit([
      [0, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 1]
    ]) ➞ false
    
    # Exit only one block away, but unreachable!
    
    can_exit([
      [0, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 0]
    ]) ➞ true

### Notes

  * In a maze of size `m x n`, you enter at `[0, 0]` and exit at `[m-1, n-1]`.
  * There can be dead ends in a maze - one exit path is sufficient.

"""

import numpy as np
​
waiting = []
​
def chkNxt(a):
    isTrue = True
    b = []
    rows, cols = np.array(a).shape
    while rows >= 1 and cols >= 1:
        if rows == 1 and cols == 1:
            return True
        if rows > 1:
            if cols > 1:
                if (a[0][1] != 0):
                    if (a[1][0] != 0):
                        isTrue = False
                        return False
                    else: 
                        a = a[1:]
                else:
                    if (a[1][0] == 0):
                        print('print waiting')
                        print(waiting)
                        waiting.append(a[1:])
                        print(waiting)
                    for i in range(len(a)):
                        b.append(a[i][1:])
                    a = b
                    b = []
            else:
                if a[1][0] != 0:
                    isTrue = False
                    return False
                else:
                    a = a[1:]
        else:
            if (a[0][1] != 0):
                return False
            else:
                for i in range(len(a)):
                    b.append(a[i][1:])
                a = b
                b = []
        # print(a)
        if (np.array(a).ndim == 1):
            if a[0] == 0:
                return True
            else:
                return False
        rows, cols = np.array(a).shape
​
​
def can_exit(arr):
    global waiting
    waiting = []
    waiting.append(arr)
    for a in waiting:
        if ((a[0][0] != 0) or (a[-1][-1] != 0)):
            return False
        res = chkNxt(a)
        if res == True:
            return True
    return False

