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
    if grid == []:
        return []
    H, W = len(grid), len(grid[0])
    if H == 0:
        return []
    if W == 0:
        return [[]]
    ans = [[0 for _ in range(W)] for __ in range(H)]
    for row in range(H):
        for col in range(W):
            S = 0
            if row > 0:
                S += sum(grid[row-1][max(0, col-1):min(W, col+2)])
            S += sum(grid[row][max(0, col-1):min(W, col+2)])
            if row < H - 1:
                S += sum(grid[row+1][max(0, col-1):min(W, col+2)])
            ans[row][col] = S
    return ans

