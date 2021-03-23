"""


The function is given a map with `1` representing land, `0` representing
water. A land cell can have four neighbors along its edges. Compute the total
perimeter of shore-lines that are defined by land cells touching water or the
outer edges of the map. Each cell edge has a length equal to `1`. An isolated
cell without neighbors has a total perimeter length of `4`.

### Examples

    islands_perimeter([
      [0, 1, 0, 0],
      [1, 1, 1, 0],
      [0, 1, 0, 0],
      [1, 1, 0, 0]
    ]) ➞ 16
    islands_perimeter([
      [1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 0, 1, 1, 0, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1],
    ]), 42)
    islands_perimeter([
      [1, 0]
    ]) ➞ 4

### Notes

N/A

"""

import numpy as np
def islands_perimeter(grid):
  a = np.array(grid)
  a = np.pad(a, (1, 1), 'constant', constant_values=(0, 0))
  cc = 0
​
  for i in range(1,a.shape[0]-1):
      for j in range(1,a.shape[1]-1):
          if a[i][j]==1:
              cc -= ((a[i][j-1]+a[i][j+1]+a[i-1][j]+a[i+1][j])-4)
  return cc

