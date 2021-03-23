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
    filler = [[0] * (len(grid[0]) + 2)]
    grid2 = filler + [[0] + i + [0] for i in grid] + filler
    c = [-1,0,1]
    ans = []
    for j in range(1,len(grid2)-1):
        aux = []
        for i in range(1,len(grid2[0])-1):
            temp = (grid2[j+k][i+l] for l in c for k in c)
            aux.append(sum(temp))
        ans.append(aux)
    return ans

