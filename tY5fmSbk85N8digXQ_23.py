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
​
  col_indexes = []
  row_indexes = []
​
  for n in range(len(arr)):
    for num in range(len(arr[n])):
      item = arr[n][num]
      if item == 1:
        col_indexes.append(num)
        row_indexes.append(n)
  
  rl = len(arr[0])
  
​
  for n in range(0, len(arr)):
    if n in row_indexes:
      for num in range(0, rl):
        arr[n][num] = 1
    else:
      for num in range(0, rl):
        if num in col_indexes:
          arr[n][num] = 1
          
  return arr

