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

def determinant(a):
    if len(a) == 1:
        return a[0][0]
    return sum((-1) ** i * a[0][i]* determinant([row[:i] + row[i + 1:] for row in a[1:]])for i in range(len(a)))

