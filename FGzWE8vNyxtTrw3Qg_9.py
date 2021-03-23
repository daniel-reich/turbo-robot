"""


The function is given a rectangular matrix consisting of zeros and ones. Count
the number of different regions and return the result. A separate region is a
collection of ones interconnected horizontally and vertically. A region can
have holes in it.

### Examples

    num_regions([
      [1, 1, 1, 1, 0],
      [1, 1, 0, 1, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0]
    ]) ➞ 1
    num_regions([
      [1, 1, 1, 1, 0],
      [1, 0, 0, 1, 0],
      [1, 1, 1, 1, 0],
      [0, 0, 0, 0, 1]
    ]) ➞ 2
    
    # The region on the upper left looks like a doughnut.
    num_regions([
      [1, 1, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 1, 0, 1],
      [0, 0, 0, 1, 1]
    ]) ➞ 3

### Notes

N/A

"""

def get_nbrs(grid, r, c):
  nbrs = [[r+dr, c+dc] for dr, dc in [[-1,0],[0,1],[1,0],[0,-1]]]
  return [[nr, nc] for nr, nc in nbrs if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1]
​
def is_region(grid, r, c):
  if grid[r][c] != 1: return False
  # set all interconnected cells in region to 0
  # using backtracking to cells with multiple neighbours
  stack = []
  while True:
    grid[r][c] = 0
    nbrs = get_nbrs(grid, r, c)
    if not nbrs:
      if not stack: break
      r, c = stack.pop()
    else:
      if len(nbrs) > 1: stack.append([r, c])
      r, c = nbrs[0]
  return True
​
def num_regions(grid):
  return sum(1 for r in range(len(grid)) for c in range(len(grid[0])) if is_region(grid, r, c))

