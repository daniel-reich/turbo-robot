"""


In linear algebra, the transpose of a matrix is an operator which flips a
matrix over its diagonal; that is, it switches the row and column indices of
the _matrix A_ by producing another matrix, often denoted by _A^T_.

Create a function that takes a 2D matrix `m` and returns a 2D matrix (matrix
A^T).

### Examples

    makeTranspose([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]) ➞ [
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9]
    ]
    
    makeTranspose([
      [1, 2],
      [3, 4],
      [5, 6]
    ]) ➞ [
      [1, 3, 5],
      [2, 4, 6]
    ]
    
    makeTranspose([
      ["a", "b"]
    ]) ➞ [
      ["a"],
      ["b"]
    ]

### Notes

N/A

"""

class Matrix:
  class Space:
​
    def __init__(self, val, row, col):
      self.v = val
      self.r = row
      self.c = col
​
  def __init__(self, mtx):
    self.mtx = mtx
​
    self.spaces = {}
​
    for r in range(len(mtx)):
      for c in range(len(mtx[0])):
        self.spaces['{},{}'.format(r,c)] = Matrix.Space(mtx[r][c], r, c)
  
  def transpose(self):
    nm = []
    
    if len(self.mtx) == len(self.mtx[0]):
      for r in range(len(self.mtx)):
        row = []
        for c in range(len(self.mtx[0])):
          row.append(self.spaces['{},{}'.format(c, r)].v)
        nm.append(row)
    else:
      for c in range(len(self.mtx[0])):
        row = []
        for r in range(len(self.mtx)):
          row.append(self.spaces['{},{}'.format(r, c)].v)
        nm.append(row)
​
    return Matrix(nm)
​
​
def make_transpose(matrix):
​
  matrix = Matrix(matrix)
  transposed = matrix.transpose()
​
  return transposed.mtx

