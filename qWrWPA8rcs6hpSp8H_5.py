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
  if len(A) == 2:
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]
  sol = 0
  for i in range(len(A[0])):
    lil_matrix = [row[0:i] + row[i+1:] for row in A[1:]]
    sol += (-1)**i*(A[0][i])*determinant(lil_matrix)
  return sol

