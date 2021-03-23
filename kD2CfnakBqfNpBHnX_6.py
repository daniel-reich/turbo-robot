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
    land = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                land.add((r, c))
    perimeter = 0
    for r, c in land:
        neighbours = 0
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (r + i, c + j) in land:
                neighbours += 1
        perimeter += 4 - neighbours
    return perimeter

