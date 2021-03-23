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
    pad = [[0] * (len(grid[0]) + 2)]
    grid_2 = pad + [[0] + i + [0] for i in grid] + pad
    check = [-1,1]
    length = 0
    for i in range(1,len(grid_2)-1):
        for j in range(1,len(grid_2[0])-1): 
            if grid_2[i][j] == 1:
                for k in check:
                    if grid_2[i+k][j] == 0:
                        length += 1
                    if grid_2[i][j+k] == 0:
                        length +=1
    return length

