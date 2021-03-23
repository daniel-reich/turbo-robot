"""


Given a matrix of m * n elements (m rows, n columns), return all elements of
the matrix in spiral order.

### Examples

    spiral_order([
      [ 1, 2, 3 ],
      [ 4, 5, 6 ],
      [ 7, 8, 9 ]
    ]) ➞ [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    spiral_order([
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]) ➞ [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

### Notes

NA

"""

def spiral_order(matrix):
    if not matrix:
        return None
    path = []
    first_column = []
    while matrix:
        try:
            path += matrix.pop(0)
            for i in range(len(matrix)):
                path += [matrix[i].pop()]
                first_column.append(matrix[i].pop(0))
            path = path + matrix.pop()[::-1]
            path = path + first_column[::-1]
            first_column = []
        except:
            if first_column:
                path += firstcolumn
    return path

