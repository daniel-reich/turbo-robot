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
    if not grid:
        return grid
    else:
        rows = len(grid)
        spotlight_grid = []
        total_sum = 0
    
        for _ in range(0, rows):
            spotlight_grid.append([])
    
        for i in grid:
            i.insert(0,0)
            i.append(0)
        grid[:0] = ([[0] * len(grid[0])])
        grid.append([0] * len(grid[0]))
    
        for i, row_item in enumerate(grid):
            if row_item != grid[0]:
                for n, col_item in enumerate(grid[i]):
                    if n != 0 and n != len(grid[i])-1:
                        for x in range(-1,2):
                            total_sum += grid[i+x][n] + grid[i+x][n-1] + grid[i+x][n+1]
    
                        spotlight_grid[i-1].append(total_sum)
                        total_sum = 0
    
        return spotlight_grid

