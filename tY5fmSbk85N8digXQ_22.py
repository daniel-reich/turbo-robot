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
    z,n=len(arr[0]),len(arr)
    rows=[x for x in range(len(arr)) for y in range(z) if arr[x][y]==1]
    cols=[y for x in range(len(arr)) for y in range(z) if arr[x][y]==1]
    for x in range(len(arr)):
        lst1=[]
        for y in range(z):
            if x in rows or y in cols:
                lst1.append(1)
            if x not in rows and y not in cols:
                lst1.append(0)
        arr.append(lst1)
    for m in range(n) :
        arr.pop(0)
    return (arr)

