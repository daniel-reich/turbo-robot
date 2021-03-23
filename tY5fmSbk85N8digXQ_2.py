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

def ones_infection(mtx):
    memx = []
    memy = []
    n_r = len(mtx)
    n_c = len(mtx[0])
    
    for row in range(n_r):
        for col in range(n_c):
            if mtx[row][col] == 1:
                memy.append(row)
                memx.append(col)
​
    for y in range(n_r):
        if y in memy:
            for i in range(n_c):
                mtx[y][i] = 1
    for x in range(n_c):
        if x in memx:
            for i in range(n_r):
                mtx[i][x] = 1
    return mtx

