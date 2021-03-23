"""


Given a grid of numbers, return a grid of the **Spotlight Sum** of each
number. The spotlight sum can be defined as the total of all numbers
immediately surrounding the number on the grid, including the number in the
total.

### Examples

    spotlight_map([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]) ➞ [
      [12, 21, 16],
      [27, 45, 33],
      [24, 39, 28]
    ]
    spotlight_map([
      [2, 6, 1, 3, 7],
      [8, 5, 9, 4, 0]
    ]) ➞ [
      [21, 31, 28, 24, 14],
      [21, 31, 28, 24, 14]
    ]
    spotlightMap([[3]]) ➞ [[3]]

### Notes

  * Note that all numbers have a spotlight sum, including numbers on the edges.
  * All inputs will be valid grid (all rows will have the same length).

"""

def spotlight_map(grid):
  ret = [[j for j in i] for i in grid]
  for x in range(len(ret)):
    for y in range(len(ret[x])):
      ret[x][y] = checkUpDown(grid,x,y)
  return ret
  
def checkUpDown(grid,x,y):
  ret = grid[x][y]
  ret+=checkLeftRight(grid,x,y)
  if x>0:
    ret+=grid[x-1][y]
    ret+=checkLeftRight(grid,x-1,y)
  if x<len(grid)-1:
    ret+=grid[x+1][y]
    ret+=checkLeftRight(grid,x+1,y)
  return ret
  
def checkLeftRight(grid,x,y):
  ret = 0
  if y>0:
    ret+=grid[x][y-1]
  if y<len(grid[x])-1:
    ret+=grid[x][y+1]
  return ret

