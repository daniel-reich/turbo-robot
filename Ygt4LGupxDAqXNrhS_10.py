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

from itertools import permutations
def spotlight_map(grid):
  if not grid or not grid[0]:
    return grid
  lg,lg0 = len(grid),len(grid[0])
  dir = set(permutations([1,1,0,0,-1,-1],2))
  return [[sum(grid[i+x][j+y] for x,y in dir if 0 <= i+x < lg and 0 <= j+y < lg0) for j in range(lg0)] for i in range(lg)]

