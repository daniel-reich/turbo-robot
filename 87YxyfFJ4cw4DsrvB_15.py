"""


Create a function that takes in parameter `n` and generates an `n x n` (where
`n` is odd) **concentric rug**.

The center of a concentric rug is `0`, and the rug "fans-out", as show in the
examples below.

### Examples

    generate_rug(1) ➞ [
      [0]
    ]
    
    generate_rug(3) ➞ [
      [1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]
    ]
    
    generate_rug(5) ➞ [
      [2, 2, 2, 2, 2],
      [2, 1, 1, 1, 2],
      [2, 1, 0, 1, 2],
      [2, 1, 1, 1, 2],
      [2, 2, 2, 2, 2]
    ]
    
    generate_rug(7) ➞ [
      [3, 3, 3, 3, 3, 3, 3],
      [3, 2, 2, 2, 2, 2, 3],
      [3, 2, 1, 1, 1, 2, 3],
      [3, 2, 1, 0, 1, 2, 3],
      [3, 2, 1, 1, 1, 2, 3],
      [3, 2, 2, 2, 2, 2, 3],
      [3, 3, 3, 3, 3, 3, 3]
    ]

### Notes

  * `n >= 0`.
  * Always increment by 1 each "layer" outwards you travel.

"""

import random
import math
​
def generate_rug(n):
​
  if n == 1:
    return [[0]]
  height = int(math.floor(n/2))
  toReturn = []
  for row in range(0,n):
    if row >= int(math.ceil(n/2)):
      toReturn.append(toReturn[n-1-row])
    else:
      toReturn.append([])
      for column in range(0,n):
        if column >= (math.ceil(n/2)):
          toReturn[row].append(toReturn[row][n-1-column])
        else:
          for _ in range(0, n-1):
            if row == _ or column == _:
              toReturn[row].append(height-_)
              break
      
  return toReturn

