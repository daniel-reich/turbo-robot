"""


[Langton's ant](https://en.wikipedia.org/wiki/Langton%27s_ant) is a two-
dimensional Turing machine invented in the late 1980s. The ant starts out on a
grid of black and white cells and follows a simple set of rules that has
complex emergent behavior.

![Langton's ant](https://edabit-
challenges.s3.amazonaws.com/LangtonsAntAnimated.gif)

The ant can travel in any of the four cardinal directions on each step. The
ant moves according to the following rules:

  * At a white square (1), turn 90° right, flip the color of the square, and move forward one unit.
  * At a black square (0), turn 90° left, flip the color of the square, and move forward one unit.
  * The grid has no limits and therefore if the ant moves outside the borders, the grid should be expanded with 0s, respectively maintaining the rectangle shape.

Create a function **Langton's Ant** with the following parameters:

    grid - a two-dimensional list of 1s and 0s
    # representing white and black cells respectively
    
    column - horizontal position of the ant
    
    row - ant's vertical position
    
    n - number of iterations
    
    direction - ant's current direction
    # 0 - north, 1 - east, 2 - south, 3 - west
    # default value will be 0

... and returns the **state** of the grid after `n` iterations.

### Examples

    langtons_ant([[1]], 0, 0, 1, 0) ➞ [[0, 0]]
    # Initially facing north (0), at the first iteration the ant turns
    # right because it stands on a white square, 1. After that, it flips
    # the square and moves forward.
    
    langtons_ant([[0]], 0, 0, 1, 0) ➞ [[0, 1]]
    
    langtons_ant([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 2, 2, 10, 1) ➞ [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]]

### Notes

N/A

"""

class Coord:
  def __init__(self, x, y):
    self.x, self.y = x, y
  def __add__(self, other):
    return Coord(self.x + other.x, self.y + other.y)
    
def extend_grid(pos, grid):
  w, h = len(grid[0]), len(grid)
  if pos.y >= h:
    grid.append([0 for _ in range(w)])
  elif pos.x >= w:
    for row in grid:
      row.append(0)
  elif pos.y < 0:
    pos.y = 0
    grid.insert(0, [0 for _ in range(w)])
  elif pos.x < 0:
    pos.x = 0
    for row in grid:
      row.insert(0, 0)
      
directions = (Coord(0, -1), Coord(1, 0), Coord(0,1), Coord(-1, 0))
def langtons_ant(grid, column, row, n, dir_idx=0):
  p = Coord(column, row)
  for _ in range(n):
    dir_idx = (dir_idx + 1) % 4 if grid[p.y][p.x] else (dir_idx - 1) % 4
    grid[p.y][p.x] = int(not grid[p.y][p.x])
    p = p + directions[dir_idx]
    extend_grid(p, grid)
  return grid

