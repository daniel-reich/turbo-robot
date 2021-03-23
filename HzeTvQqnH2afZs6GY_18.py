"""


Create a function that takes in **size** and **direction** and generates a
**diagonal rug**.

The size is the `n` parameter, and all rugs are square `n x n`. The direction
is whether the diagonal part begins on the left or the right side.

### Examples

    generate_rug(4, "left") ➞ [
      [0, 1, 2, 3],
      [1, 0, 1, 2],
      [2, 1, 0, 1],
      [3, 2, 1, 0]
    ]
    
    generate_rug(5, "right") ➞ [
      [4, 3, 2, 1, 0],
      [3, 2, 1, 0, 1],
      [2, 1, 0, 1, 2],
      [1, 0, 1, 2, 3],
      [0, 1, 2, 3, 4]
    ]
    
    generate_rug(1, "left") ➞ [
      [0]
    ]
    
    generate_rug(2, "right") ➞ [
      [1, 0],
      [0, 1]
    ]

### Notes

  * `n > 0`
  * A `1 x 1` rug is trivially `[[0]]` (same for left and right).

"""

import numpy as np
​
def generate_rug(n, direction):
  rug = []
  pivot = 0
  for i in range(n):
    row = np.zeros(n)
    
    for j in range(0, pivot):
      row[pivot - j - 1] = j + 1
    
    for j in range(pivot, n):
      row[j] = j - pivot
      
    pivot += 1
    
    row = list(row)
    if direction == "right":
      row.reverse()
      
    rug.append(row)
    
  return rug

