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
  ans, c = [], 0
  while matrix:
    if c%4==0: new = matrix.pop(0)
    if c%4==1: new = [row.pop(-1) for row in matrix]
    if c%4==2: new = matrix.pop(-1)[::-1]
    if c%4==3: new = [row.pop(0) for row in matrix]
    ans+= new
    c+= 1
  return ans

