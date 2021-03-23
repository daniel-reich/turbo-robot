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

def rec_tint(i, j, grid, n_rows, n_cols, n_regions, tint = None):
    if grid[i][j] != 1:
        return(n_regions)
    if tint == None:
        n_regions += 1 
    tint = n_regions
    grid[i][j] = tint
    if i > 0: n_regions = rec_tint(i - 1, j, grid, n_rows, n_cols, n_regions, tint)
    if i < n_rows - 1: n_regions = rec_tint(i + 1, j, grid, n_rows, n_cols, n_regions, tint)
    if j > 0: n_regions = rec_tint(i, j - 1, grid, n_rows, n_cols, n_regions, tint)
    if j < n_cols - 1: n_regions = rec_tint(i, j + 1, grid, n_rows, n_cols, n_regions, tint)
    return(n_regions)
    
def num_regions(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])
    n_regions = 1
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 1:
                n_regions = rec_tint(i, j, grid,
                                     n_rows, n_cols, n_regions)
    return(n_regions - 1)

