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
  def sums(i,j):
    s = 0
    for a in range(-1,2):
      for b in range(-1,2):
        if min(a+i,b+j) >= 0 and a+i < len(grid) and b+j < len(grid[0]):
          s += grid[a+i][b+j]
    return s
  return [[sums(i,j) for j in range(0,len(grid[0]))] for i in range(0,len(grid))]

