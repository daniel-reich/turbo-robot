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
    if not grid: return []
    row = len(grid); col = len(grid[0]); add = 0; res = [[0 for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            add += grid[i][j]
            if i-1 >= 0:
                add += grid[i-1][j]
                if j-1 >= 0: add += grid[i-1][j-1]
                if j+1 < col: add += grid[i-1][j+1]
            if i+1 < row:
                add += grid[i+1][j]
                if j-1 >= 0: add += grid[i+1][j-1]
                if j+1 < col: add += grid[i+1][j+1]
            if j-1 >= 0: add += grid[i][j-1]
            if j+1 < col: add += grid[i][j+1]
            res[i][j] = add; add = 0
    return res

