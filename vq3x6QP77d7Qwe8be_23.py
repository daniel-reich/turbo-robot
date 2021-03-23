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
  def get_square(y,x,n):
    if y + n > len(lst) or x + n > len(lst[0]):
      return False
    for r in range (y,y+n):
      for c in range (x,x+n):
        if lst[r][c] % 2==0:
          return False
    return True
  max_square = 0
  for row in range (len(lst)):
    for column in range (len(lst[0])):
      size = 1
      while True:
        if not get_square(row,column,size):
          if size-1 > max_square:
            max_square = size-1
          break
        size += 1
  return max_square

