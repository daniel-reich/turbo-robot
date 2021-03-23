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
  maxpatch = 0
  if len(lst[0]) == 0:
    return maxpatch
  for y in range(len(lst)):
    for x in range(len(lst)):
      if lst[y][x]%2 == 1:
        for z in range(len(lst[y])-x+1):
          if y+z <= len(lst):
            if all([all([lst[i][j]%2 == 1 for j in range(x,x+z)]) for i in range(y,y+z)]):
              maxpatch = max(maxpatch,z)
  return maxpatch

