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
    d = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            d[(i,j)] = grid[i][j]
    a = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
    
    for loc in d.keys():
        ctr = 0
        for k in range(len(a)):
            if (loc[0]+a[k][0],loc[1]+a[k][1]) in d:
                ctr += d[(loc[0]+a[k][0],loc[1]+a[k][1])]
        grid[loc[0]][loc[1]] = ctr    
    
    return grid

