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
    y = len(grid)
    try:
        x = len(grid[0])
    except IndexError:
        return []
    new_grid = []
    for o in range(y):
        new_grid.append([])
        for p in range(x):
            new_grid[o].append(0)
    for y_span in range(y):
        for x_span in range(x):
            current_tile_total = 0
            for i in range(3):
                for j in range(3):
                    replace_y = i + y_span - 1
                    replace_x = j + x_span - 1
​
                    if replace_y < 0 or replace_y >= y:
                        continue
                    elif replace_x < 0 or replace_x >= x:
                        continue
                    else:
                        current_tile_total = grid[replace_y][replace_x] + current_tile_total
            new_grid[y_span][x_span] = current_tile_total
    return(new_grid)

