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
    ans = 0
    h, w = len(grid), len(grid[0])
    grid = [[0] * (w+2)] + [[0]+row+[0] for row in grid]+ [[0] * (w+2)]
    for row in range(1, h+1):
        for col in range(1, w+1):
            if grid[row][col] == 1:
                ans += 4 - sum([grid[row-1][col], grid[row+1][col], \
                                grid[row][col-1], grid[row][col-1]])
    return ans

