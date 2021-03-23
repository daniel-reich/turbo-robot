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
  result = 0
  for x in range(len(A)):
    result += ((-1) ** x) * A[x][0] * determinant([A[y][1:] for y in range(len(A)) if y != x])
  return result

