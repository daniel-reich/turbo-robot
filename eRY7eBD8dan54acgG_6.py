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
  for x in range(len(lst)):
    for y in range(len(lst)-1):
      if lst[x][y] != lst[x][y+1]:
        continue
      else:
        return False
  return True

