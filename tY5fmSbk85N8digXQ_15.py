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
  i = 0
  while i < len(arr):
    j = 0
    while j < len(arr[i]):
      if arr[i][j] == 1:
        arr[i][j] = 2
      j +=1
    i += 1
  
  i = 0
  while i < len(arr):
    j = 0
    while j < len(arr[i]):
      if arr[i][j] == 2:
        for k in range(len(arr)):
          if arr[k][j] == 0:
            arr[k][j] = 1
        for l in range(len(arr[i])):
          if arr[i][l] == 0:
              arr[i][l] = 1
      j += 1
    i += 1
  
  i = 0
  while i < len(arr):
    j = 0
    while j < len(arr[i]):
      if arr[i][j] == 2:
        arr[i][j] = 1
      j += 1
    i += 1
  
  return arr

