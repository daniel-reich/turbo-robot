"""


Create a function that takes an array of numbers, and returns the size of the
biggest square patch of odd numbers. See examples for a clearer picture.

### Examples

    odd_square_patch([
      [1, 2, 4, 9],
      [4, 5, 5, 7],
      [3, 6, 1, 7]
    ]) ➞ 2
    
    # The 2x2 square at the lower right
    # ([5, 7] on the 2nd row, [1, 7] on the third).
    
    odd_square_patch([[1, 2, 4, 9]]) ➞ 1
    
    # An array with a single row can only have a square patch of
    # maximum size 1x1 containing a single odd element.
    
    odd_square_patch([[2, 4, 6]]) ➞ 0

### Notes

N/A

"""

def odd_square_patch(lst):
  w = len(lst[0])
  h = len(lst)
  def idx_of(x, y):
    return y * w + x
  lst = [v % 2 for row in lst for v in row]
  if len(lst) == 0:
    return 0
  expanded  = True
  while expanded:
    expanded = False
    for i in range(w - 1):
      for j in range(h - 1):
        if lst[idx_of(i,j)] > 0:
          newSize  = min(lst[idx_of(i+1, j)], lst[idx_of(i+1, j+1)], lst[idx_of(i, j+1)]) + 1
          if newSize > lst[idx_of(i, j)]:
            expanded = True
            lst[idx_of(i, j)] = newSize
  return max(lst)

