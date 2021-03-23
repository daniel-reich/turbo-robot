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

import numpy as np
def subtract_matrix(lst1, lst2):
    lst1 = list(map(lambda x:list(map(lambda y:int(y),x)),np.array(lst1)))
    lst2 = list(map(lambda x:list(map(lambda y:float(y),x)),np.array(lst2)))
    ans = list(np.subtract(lst1,lst2))
    return list(map(lambda x:list(x), ans))

