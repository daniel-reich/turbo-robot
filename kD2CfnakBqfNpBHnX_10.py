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
  edges = 0
  for k in range(0,2):
    grid = np.rot90(np.array(grid)).tolist()
    edges += grid[0].count(1) + grid[-1].count(1)
    for a,b in zip(grid[:-1],grid[1::]):
      for j in range(0,len(grid[0])):
        if a[j] != b[j]:
          edges += 1
  return edges

