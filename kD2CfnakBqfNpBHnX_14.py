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
  res = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j]==1:
        res+=neighbors(grid,i,j)
  return res
  
def neighbors(grid,x,y):
  total = 4
  if x-1>=0 and grid[x-1][y]==1:
    total-=1
  if x+1<len(grid) and grid[x+1][y]==1:
    total-=1
  if y-1>=0 and grid[x][y-1]==1:
    total-=1
  if y+1<len(grid[0]) and grid[x][y+1]==1:
    total-=1
  return total

