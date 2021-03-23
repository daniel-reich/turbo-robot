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

sub_matrix = lambda A, i, j: [[A[r][c] for c in range(len(A)) if c != j] for r in range(len(A)) if r != i]
def determinant(A):
    if len(A) == 1: return A[0][0]
    det, sign = 0, 1
    for c in range(len(A)):
        det += A[0][c] * determinant(sub_matrix(A, 0, c)) * sign
        sign = -sign
    return det

