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
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]
  else:
    s = 0
    for i in range(len(A)):
      B = [[A[row][col] for col in range(1,len(A))] for row in range(len(A)) if row!=i ]
      s += ((-1)**i)*A[i][0]*determinant(B)
    return s

