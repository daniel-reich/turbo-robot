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

def determinant(matrix):
    det = 0
    if len(matrix) == 1:
        det += matrix[0][0]
    else:
        for i in range(0, len(matrix)):
            det += ((-1) ** (i))*matrix[i][0] * determinant([matrix[j][1:] for j in range(0, len(matrix)) if j != i])
    return det

