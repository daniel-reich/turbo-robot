"""


Two matrices must have an equal number of rows and columns to be subtracted.
In which case, the subtracted of two matrices A and B will be a matrix which
has the same number of rows and columns as A and B.

The result of the subtraction of A and B, denoted A - B is computed by
subtracting corresponding elements of A and B.

Create a function that takes 2 x 2D lists `lst1` and `lst2` as an argument and
returns a 2D list (matrix C). C = A-B.

### Examples

    subtract_matrix([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ], [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]) ➞ [
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]
    ]

### Notes

Treat strings of numbers as integers.

"""

def subtract_matrix(lst1, lst2):
  try:
    for i in range(0,len(lst1)):
      for j in range(0,len(lst1[0])):
        lst2[i][j] = lst1[i][j] - lst2[i][j]
    return lst2
  except TypeError:
    lst1 = [[float(ele) for ele in sub] for sub in lst1]
    lst2 = [[float(ele) for ele in sub] for sub in lst2]
    for i in range(0,len(lst1)):
      for j in range(0,len(lst1[0])):
        lst2[i][j] = lst1[i][j] - lst2[i][j]
    return lst2

