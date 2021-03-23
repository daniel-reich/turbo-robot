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
  lst = [[1 if row[i]%2 else 0 for i in range(len(row))] for row in lst]
  tot_rows = len(lst)
  tot_cols = len(lst[0])  
  
  if not (tot_rows and tot_cols):
    return 0
​
  res = [[0]*tot_cols for _ in lst]
  for i in reversed(range(tot_rows)):
    for j in reversed(range(tot_cols)):
      if lst[i][j] != 0:
        res[i][j] = (1 + min(
          res[i][j+1],
          res[i+1][j],
          res[i+1][j+1]
        )) if i < tot_rows - 1 and j < tot_cols - 1 else 1
  return max(num for row in res for num in row)

