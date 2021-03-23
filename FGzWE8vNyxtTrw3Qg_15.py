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

from collections import deque
def num_regions(grid):
  h, w = len(grid), len(grid[0])
  
  def in_bounds(x, y):
    return (0 <= x < w) and (0 <= y < h)
  
  def bfs(x0, y0):
    queue = deque([(x0, y0)])
    while queue:
      x, y = queue.pop()    
      grid[y][x] = 0
      for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if in_bounds(nx, ny) and grid[ny][nx] != 0:
          queue.appendleft((nx, ny))
  
  count = 0
  for y in range(h):
    for x in range(w):
      if grid[y][x]:
        count += 1
        bfs(x, y)
  return count

