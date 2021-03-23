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

def trans(lst):
    return list(zip(*lst))[::-1]
def spiral_order(matrix):
  lst1=[]
  while matrix:
    lst1+=matrix.pop(0)
    matrix=trans(matrix)
  return lst1

