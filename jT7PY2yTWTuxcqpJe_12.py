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
    is_valid = lambda r, c: 0<=r<len(matrix) and 0<=c<len(matrix[0]) and matrix[r][c]!=-1
    order, dirns = [], [(0,1), (1,0), (0,-1), (-1,0)]
    r,c,d = 0,0,0
    while matrix[r][c] != -1:
        order.append(matrix[r][c])
        matrix[r][c] = -1
        nr, nc = r+dirns[d][0], c+dirns[d][1]
        if not is_valid(nr, nc):
            d = (d+1)%4
            nr, nc = r+dirns[d][0], c+dirns[d][1]
        r,c = nr,nc
    return order

