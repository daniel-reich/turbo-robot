"""


Write a function that replaces every row and column that contains at least one
**1** into a row/column that is filled **entirely** with **1s**.

Solve this **without** returning a copy of the input list.

### Examples

    ones_infection([
      [0, 0, 1],
      [0, 0, 0],
      [0, 0, 0]
    ]) ➞ [
      [1, 1, 1],
      [0, 0, 1],
      [0, 0, 1]
    ]
    
    ones_infection([
      [1, 0, 1, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 0]
    ]) ➞ [
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 0]
    ]
    
    ones_infection([
      [0, 1, 0, 1],
      [0, 0, 0, 0],
      [0, 1, 0, 0]
    ]) ➞ [
      [1, 1, 1, 1],
      [0, 1, 0, 1],
      [1, 1, 1, 1]
    ]

### Notes

  * You must **mutate** the original matrix.
  * Input matrices will have at least row and one column.
  *  **Bonus** : Solve this **without** using any higher-order functions.

"""

def ones_infection(arr):
  nRows = len(arr)
  nCols = len(arr[0])
  outrow = []
  outcol = []
  for row in range(nRows):
    for col in range(nCols):
      if arr[row][col] == 1:
        outrow.append(row)
        outcol.append(col)
  for row in range(nRows):
    if row in outrow:
      arr[row] = [1]*nCols
    else:
      arr[row] = [0]*nCols
      for col in range(nCols):
        if col in outcol:
          arr[row][col] = 1
  return arr

