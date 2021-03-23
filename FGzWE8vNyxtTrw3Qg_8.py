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

def num_regions(grid):
    regions = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                regions += 1
                grid[row][col] = 0
                check(grid,row,col)
    return regions
​
def check(grid,row,col):
    if col + 1 < len(grid[0]):
        if grid[row][col + 1] == 1:
            grid[row][col + 1] = 0
            check(grid,row,col + 1)
    if row + 1 < len(grid):
        if grid[row + 1][col] == 1:
            grid[row + 1][col] = 0
            check(grid,row + 1,col)
    if col - 1 >= 0:
        if grid[row][col - 1] == 1:
            grid[row][col - 1] = 0
            check(grid,row,col - 1)
    if row - 1 >= 0:
        if grid[row - 1][col] == 1:
            grid[row - 1][col] = 0
            check(grid,row - 1,col)
    return None

