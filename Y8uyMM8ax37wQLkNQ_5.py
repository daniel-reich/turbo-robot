"""


Write a function that accepts an integer `n` and returns an `n * n` spiral
matrix.

### Examples

    matrix(2) ➞ [
      [1, 2],
      [4, 3]
    ]
    
    matrix(3) ➞ [
      [1, 2, 3],
      [8, 9, 4],
      [7, 6, 5]
    ]
    
    matrix(4) ➞ [
      [1,  2,  3,  4],
      [12, 13, 14, 5],
      [11, 16, 15, 6],
      [10,  9,  8, 7]
    ]

### Notes

In the examples, traverse the matrix in the clock-wise direction to observe
the spiral pattern.

"""

def matrix(n):
    result =[]
    for _ in range(n):
        result.append([0 for _ in range(n)])
    k = 1
    row = 0
    column = n
    while row < n/2:
        for j in range(n - column, column):
            result[row][j] = k
            k += 1
        for i in range(row + 1, n - row):
            result[i][column-1] = k
            k += 1
        for j in range(column - 2, n - column-1, -1):
            result[n-row-1][j] = k
            k += 1
        for i in range(n - 2- row, row, -1):
            result[i][n - column] = k
            k += 1
        row += 1
        column -= 1
    return result

