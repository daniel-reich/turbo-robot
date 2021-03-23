"""


Create a function that returns `True` if the two-dimensional `n x n` input
array has a **checker-board pattern**.

### Examples

    is_checkerboard([
      [1, 1],
      [0, 1]
    ]) ➞ False
    
    is_checkerboard([
      [0, 1],
      [1, 0]
    ]) ➞ True
    
    is_checkerboard([
      [1, 0, 1, 0, 1],
      [0, 1, 0, 1, 0],
      [1, 0, 1, 0, 1],
      [0, 1, 0, 1, 0],
      [1, 0, 1, 1, 1]
    ]) ➞ False
    
    is_checkerboard([
      [1, 0, 1, 0, 1],
      [0, 1, 0, 1, 0],
      [1, 0, 1, 0, 1],
      [0, 1, 0, 1, 0],
      [1, 0, 1, 0, 1]
    ]) ➞ True

### Notes

  * An element in the array adheres to the checker-board pattern if the elements directly to the left, right, top and below are of a different type, and the elements on the diagonal direction are of the same type.
  * The element in the upper-left corner can be either `0` or `1`.

"""

def is_checkerboard(lst):
    i = 1
    while i <= len(lst) - 1:
        if i == len(lst) - 1:
            for j in range(len(lst[i])):
                if (lst[i][j] == 0 and lst[i-1][j] != 1) or (lst[i][j] == 1 and lst[i-1][j] != 0):
                    return False
        else:
            for j in range(len(lst[i])):
                if (lst[i][j] == 0 and lst[i-1][j] != 1) or (lst[i][j] == 1 and lst[i-1][j] != 0) or (lst[i][j] == 0 and lst[i+1][j] != 1) or (lst[i][j] == 1 and lst[i+1][j] != 0):
                    return False
        i += 2
    return True

