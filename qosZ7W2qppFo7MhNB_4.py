"""


A **hexagonal grid** is a commonly used **game board design** based on
hexagonal tiling. In the following grid, the two marked locations have a
minimum distance of 6 because at least 6 steps are needed to reach the second
location starting from the first one.

![](https://edabit-challenges.s3.amazonaws.com/HiD.svg)

Write a function that takes a hexagonal grid with two marked locations as
input and returns their distance.

The input grid will be a list of strings in which each tile is represented
with `o` and the two marked locations with `x`.

### Examples

    hex_distance([
      "  o o  ",
      " o x o ",
      "  o x  ",
    ]) ➞ 1
    
    hex_distance([
      "  o o  ",
      " x o o ",
      "  o x  ",
    ]) ➞ 2
    
    hex_distance([
      "   o o o   ",
      "  o o o o  ",
      " o o o o o ",
      "  x o o x  ",
      "   o o o   ",
    ]) ➞ 3

### Notes

N/A

"""

# https://www.redblobgames.com/grids/hexagons/#distances
​
def get_marked_cube_coordinates(grid):
    grid = [row.split() for row in grid]
    marked = []
    n = len(grid)
    mid = grid[n // 2]
    m = len(mid)
    # middle row:
    x, y, z = -(m // 2), m // 2, 0
    for i in range(m):
        if mid[i] == 'x':
            marked.append((x, y, z))
        x += 1
        y -= 1
    # rows above middle row:
    offset = 0
    for r in range(n // 2 - 1, -1, -1):
        row = grid[r]
        offset += 1
        x, y, z = -(m // 2) + offset, m // 2, -offset
        for i in range(len(row)):
            if row[i] == 'x':
                marked.append((x, y, z))
            x += 1
            y -= 1
    # rows below middle row:
    offset = 0
    for r in range(n // 2 + 1, n):
        row = grid[r]
        offset += 1
        x, y, z = -(m // 2), m // 2 - offset, offset
        for i in range(len(row)):
            if row[i] == 'x':
                marked.append((x, y, z))
            x += 1
            y -= 1        
    assert len(marked) == 2, "No of marked cells is not equal to 2, it is: " + str(len(marked))
    return marked[0], marked[1]
​
def get_cube_distance(grid):
    a, b = get_marked_cube_coordinates(grid)
    return sum([abs(a[i] - b[i]) for i in range(3)]) // 2
​
def hex_distance(grid):
    return get_cube_distance(grid)

