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

def hex_distance(grid):
  diag = len(grid)
  side = diag//2+1
  grid = ["".join(i.split()) for i in grid]
  grid = grid[:side] + [i.rjust(diag) for i in grid[side:]]
  (x1, y1), (x2, y2) = [
    (x, y) for y,row in enumerate(grid) for x,i in enumerate(row) if i=="x"
  ]
  dx = x2 - x1
  dy = y2 - y1
  return max(dx,dy) if dx >=0 else dy-dx

