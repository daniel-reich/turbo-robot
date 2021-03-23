"""


Create a function that returns the determinant of a given square matrix.

### Examples

    determinant([[3]]) ➞ 3
    
    determinant([[1, 0], [5, 4]]) ➞ 4
    
    determinant([[3, 0], [2, 2]]) ➞ 6
    
    determinant([[4, 8, 6], [2, 4, 3], [6, 2, 1]]) ➞ 0

### Notes

All inputs are square integer matrices.

"""

def determinant(A):
  if len(A) == 1:
    return A[0][0]
  elif len(A) == 2:
    return A[0][0] * A[1][1] - A[1][0] * A[0][1]
  
  det = 0
  for column, value in enumerate(A[0]):
    sign = 1 if column % 2 == 0 else -1
    det += sign * value * determinant([
      [
        column_value
        for column_no, column_value in enumerate(row)
        if column_no != column
      ]
      for row_no, row in enumerate(A)
      if row_no != 0
    ])
  return det

