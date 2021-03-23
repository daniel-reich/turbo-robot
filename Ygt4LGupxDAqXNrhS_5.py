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
    rows, cols = len(grid), 0
    if rows > 0:
        cols = len(grid[0])
    if rows < 2 and cols < 2:
        return grid
    res = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            for v, h in [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1),
                         (-1, -1), (-1, 1), (1, -1)]:
                if 0 <= r + v < rows and 0 <= c + h < cols:
                    res[r][c] += grid[r + v][c + h]
    return res

