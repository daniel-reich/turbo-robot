"""


Create a function that takes a two-dimensional list as an argument and returns
a one-dimensional list with the values of the original 2d list that are
arranged by spiralling through it (starting from the top-left).

### Examples

    spiral_transposition([
      [7, 2],
      [5, 0]
    ])
    
    ➞ [7, 2, 0, 5]
    
    spiral_transposition([
      [1, 2, 3],  
      [4, 5, 6],
      [7, 8, 9]
    ])
    
    ➞ [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    spiral_transposition([
      [1, 1, 1],  
      [4, 5, 2],
      [3, 3, 2] 
    ])
    
    ➞ [1, 1, 1, 2, 2, 3, 3, 4, 5]

### Notes

If you do not understand the instructions, write the 3x3 list example on a
piece of paper and trace the output through it.

"""

import numpy as np
​
def array_delete(lst, element):    # deletes all of a given element from array without flattening it
  new_matrix = lst[:]
  for row in new_matrix:
    if element in row:
      while element in row:
        row.remove(element)
  for row in new_matrix:
    if len(row) == 0:
      new_matrix.remove(row)
  return np.array(new_matrix)
  
output = []
​
def spiral_transposition(lst):
  row_count = len(lst)
  col_count = len(lst[0])
  matrix = np.array(lst, dtype = object)
  global output
  
  # Top row, left to right
  for i in range(col_count):
    output.append( matrix[0, i] )
    matrix[0, i] = 'x'  
  
  # Right column, up to down
  for i in range(1, row_count):
    output.append( matrix[i, -1] )
    matrix[i, -1] = 'x'
  
  # Bottom row, right to left
  
  for i in range(col_count-2, -1, -1):
    output.append( matrix[-1, i] )
    matrix[-1, i] = 'x'
    
  # Left column, down to up
  for i in range(row_count-2, 0, -1):
    output.append( matrix[i, 0] )
    matrix[i, 0] = 'x'
    
  # Eliminate dummy 'x' values from matrix, do recursion until all elements have been taken into account
  
  remaining_matrix = array_delete( matrix.tolist(), 'x')
  
  if remaining_matrix.tolist() == [[]]:
    Output = output
    output = []   # reset the global variable
    return Output
    
  elif len( remaining_matrix.tolist() ) == 1:
    output.append( remaining_matrix.tolist()[0][0] )
    Output = output
    output = []
    return Output
  
  else:
    return spiral_transposition( remaining_matrix.tolist() )

