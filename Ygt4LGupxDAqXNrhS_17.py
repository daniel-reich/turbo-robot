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
  res = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      res[i][j] = around(grid,i,j)+grid[i][j]
  return res
  
def around(arr,x,y):
  total = 0
  if x-1>-1:
    total+=arr[x-1][y]
  if x-1>-1 and y-1>-1:
    total+=arr[x-1][y-1]
  if x-1>-1 and y+1<len(arr[0]):
    total+=arr[x-1][y+1]
  if x+1<len(arr):
    total+=arr[x+1][y]
  if x+1<len(arr) and y-1>-1:
    total+=arr[x+1][y-1]
  if x+1<len(arr) and y+1<len(arr[0]):
    total+=arr[x+1][y+1]
  if y-1>-1:
    total+=arr[x][y-1]
  if y+1<len(arr[0]):
    total+=arr[x][y+1]
  return total

