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
  ret = 0
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      if grid[x][y]==1:
        if x==0:
          ret+=1
        if y==0:
          ret+=1
        if x>0 and grid[x-1][y]==0:
          ret+=1
        if y>0 and grid[x][y-1]==0:
          ret+=1
        if x<len(grid)-1 and grid[x+1][y]==0:
          ret+=1
        if y<len(grid[x])-1 and grid[x][y+1]==0:
          ret+=1
        if x==len(grid)-1:
          ret+=1
        if y==len(grid[x])-1:
          ret+=1
  return ret

