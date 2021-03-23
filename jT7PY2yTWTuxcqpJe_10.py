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

def spiral_order(m):
  spr=[]
  while m:
    spr+=m.pop(0)
    m = list(zip(*m))[::-1]
  return spr

