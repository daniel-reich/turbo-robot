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
    ht = len(arr)
    ln = len(arr[0])
​
    for h in range(ht):
        for l in range(ln):
            if arr[h][l] == 1:
                arr[h][l] = 2
​
    for h in range(ht):
        for l in range(ln):
            if arr[h][l] == 2:
                for i in range(ht):
                    if arr[i][l] == 0:
                        arr[i][l] = 1
                for j in range(ln):
                    if arr[h][j] == 0:
                        arr[h][j] = 1
​
    for h in range(ht):
        for l in range(ln):
            if arr[h][l] == 2:
                arr[h][l] = 1
​
    return arr

