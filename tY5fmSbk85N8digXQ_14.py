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
  temp = [0] * len(arr)
  for i in range(len(temp)):
    temp[i] = [0] * len(arr[0])
  for i in range(len(arr)):
    for x in range(len(arr[i])):
      if 1 in arr[i] or 1 in [a[x] for a in arr]:
        temp[i][x] = 1
  for i in range(len(arr)):
    for x in range(len(arr[i])):
      if temp[i][x] == 1:
        arr[i][x] = 1
  return arr

