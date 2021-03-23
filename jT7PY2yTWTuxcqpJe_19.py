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
  outputlist=[]
  cleared=0
  end=len(matrix)
  while any(matrix):
    outputlist.extend(matrix[cleared])
    matrix[cleared].clear()
    cleared+=1
    n=1
    while n<end:
      outputlist.append(matrix[n].pop())
      n+=1
    while matrix[end-1]:
      outputlist.append(matrix[end-1].pop())
    n-=1
    while n>=1:
      outputlist.extend(matrix[n])
      n-=1
    return outputlist

