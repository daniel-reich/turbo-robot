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
  width, height = len(lst[0]), len(lst)
  max_size = 0
  
  for x in range(width):
    for y in range(height):
      max_size = max(largest_odd_square_patch(lst, x, y), max_size)
      
  return max_size
  
def largest_odd_square_patch(lst, column, row):
  width, height = len(lst[0]), len(lst)
  
  try_size = 0
  for x in range(column, width):
    if lst[row][x] % 2 == 0:
      break
    try_size += 1
    
  try_size = min(try_size, height - row)
  for y in range(row, row + try_size):
    if lst[y][column] % 2 == 0:
      try_size = y - row
      break
      
  return try_size \
    if all(lst[y][x] % 2 != 0
      for x in range(column, column + try_size)
      for y in range(row, row + try_size)) \
    else 0

