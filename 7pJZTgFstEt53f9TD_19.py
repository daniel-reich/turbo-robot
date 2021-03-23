"""


Create a function that transposes a 2D matrix.

### Examples

    transpose_matrix([
      [1, 1, 1],
      [2, 2, 2],
      [3, 3, 3]
    ]) ➞ [
      [1, 2, 3],
      [1, 2, 3],
      [1, 2, 3]
    ]
    
    transpose_matrix([
      [5, 5],
      [6, 7],
      [9, 1]
    ]) ➞ [
      [5, 6, 9],
      [5, 7, 1]
    ]

### Notes

N/A

"""

import copy
def transpose_matrix(lst):
  rows = len(lst)
  cols = len(lst[0])
  new_lst = [[0 for x in range(rows)] for y in range(cols)]
  for row in range(len(lst)):
    for col in range(len(lst[0])):
      new_lst[col][row] = lst[row][col]
  return new_lst

