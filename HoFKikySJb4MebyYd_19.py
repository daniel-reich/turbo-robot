"""


Suppose any `nxm` matrix of `0`s and `1`s can be transformed into a second
matrix, where each number in position `(i, j)` in the new matrix is the sum of
**1s** in row `i` and column `j` in the original matrix, **excluding itself**
(if it is a 1).

    [[1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0]]
    
    [1, 5, 2, 4, 1],
    [2, 4, 1, 3, 2],
    [2, 4, 1, 1, 2],
    [3, 2, 2, 2, 3],
    [2, 2, 1, 3, 2]
    # The 1 on the upper left corner has 1 other 1 in the same row as itself (excluding itself).
    # The 0 to the right of the 1 has 2 1's on the same row as itself, and 3 1's in the same column, etc.

Create a function that transforms the first matrix into its second matrix
equivalent.

### Examples

    transform_matrix([
      [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]
    ]) ➞ [
      [0, 2, 2],
      [2, 0, 2],
      [2, 2, 0]
    ]
    
    transform_matrix([
      [1, 1, 1],
      [0, 0, 1],
      [0, 0, 1]
    ]) ➞ [
      [2, 2, 4],
      [2, 2, 2],
      [2, 2, 2]
    ]
    
    transform_matrix([
      [1, 1, 1],
      [0, 1, 1],
      [0, 0, 1]
    ]) ➞ [
      [2, 3, 4],
      [3, 2, 3],
      [2, 3, 2]
    ]

### Notes

It might be easier to visualize this by drawing the grid of 0's and 1's out on
a sheet of paper, and drawing lines through a specific number's row and
column.

"""

def transform_matrix(lst):
  row_sums = [sum(r) for r in lst]
  col_sums = [sum([r[i] for r in lst]) for i in range(len(lst[0]))]
  out = []
  for i in range(len(lst)):
    out_r = []
    out.append(out_r)
    for j in range(len(lst[0])):
      out_r.append(row_sums[i] + col_sums[j] - 2* lst[i][j] )
  return out

