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

from itertools import dropwhile
def num_regions(grid):
  count = 0
  def valid(i,j):
    try:
      return grid[i][j] == 1 if min(i,j) >= 0 else False
    except IndexError:
      return False
  def indices(i,j):
    return [(a+i,b+j) for a,b in zip([-1,0,0,1],[0,-1,1,0]) if valid(a+i,b+j)]
  while True:
    try:
      i = grid[0].index(1)
      grid[0][i] = 0
      queue = [(0,i)]
      while queue:
        current = queue[0]
        for index in indices(current[0],current[1]):
          grid[index[0]][index[1]] = 0
          queue.append(index)
        queue.pop(0)
      count += 1      
    except ValueError:
      grid = list(dropwhile(lambda x: not 1 in x, grid))
      if not grid:
        return count

