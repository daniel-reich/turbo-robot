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

def langtons_ant(grid, col, row, n, direction=0):
    # directions: 0 - north, 1 - east, 2 - south, 3 - west
    h, w = len(grid), len(grid[0])
    assert h == w, "We expect a square grid?? " + str(h) + " " + str(w)
    for _ in range(n):
        direction = (direction + 1) % 4 if grid[row][col] == 1 else (direction - 1)  % 4
        grid[row][col] = 1 - grid[row][col]
        if direction == 0:
            # go north:
            if row == 0:
                # we have to expand the grid to the north, ant is in (new) row 0:
                grid = [[0] * w] + grid
                h += 1
            else:
                row -= 1
        elif direction == 2:
            # go south:
            if row == h - 1:
                # we have to expand the grid to the south, ant is in (new) row h-1:
                grid = grid + [[0] * w]
                h += 1
                row += 1
            else:
                row += 1
        elif direction == 1:
            # go east:
            if col == w - 1:
                # we have to expand the grid to the east, ant is in (new) col w-1:
                grid = [row + [0] for row in grid]
                w += 1
                col += 1
            else:
                col += 1
        elif direction == 3:
            # go west:
            if col == 0:
                grid = [[0] + row for row in grid]
                w += 1
            else:
                col -= 1
    return grid

