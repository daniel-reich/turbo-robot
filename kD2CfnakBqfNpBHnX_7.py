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

def islands_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    grid = [[0]*(cols+4)]*2 + [[0, 0] + i + [0, 0] for i in grid] + [[0]*(cols+4)]*2
​
    perimeter = 0
    for r in range(1, rows + 3):
        for c in range(1, cols + 3):
            if grid[r][c] == 0:
                for i, j in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    if grid[r+i][c+j] == 1:
                        perimeter += 1
    return perimeter

