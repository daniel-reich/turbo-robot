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
  # Sum of indices is key. 
  # All numbers with even row+col must equal each other
  # All numbers with odd row+col must equal each other
  # evens cannot equal odds
  n = len(lst)
  for row in range(n):
    for col in range(n):
      if (row + col) % 2 == 0:   # indices sum to an even number
        if lst[row][col] != lst[0][0]:
          return False
      elif (row + col) % 2 == 1:   # indices sum to an odd number
        if lst[row][col] != lst[0][1]: 
          return False
  if lst[0][0] == lst[0][1]:
    return False
  return True

