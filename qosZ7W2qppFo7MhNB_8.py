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

from itertools import dropwhile
import re
def hex_distance(grid):
  def new_string(i):
    return grid[1][:i] + "x" + grid[1][i+1::]
  grid = list(dropwhile(lambda k: not "x" in k, grid))
  grid = list(dropwhile(lambda k: not "x" in k, grid[::-1]))[::-1]
  if len(grid) == 1:
    try:
      return len(re.findall(r'xo*(?=x)',grid[0].replace(' ',''))[0])
    except IndexError:
      return 0
  if grid[0].index("x") == grid[-1].index("x"):
    return len(grid) - 1
  if grid[0].index("x") == grid[0].index("o") - 1:
    grid[1] = new_string(grid[0].index("x")+1)
  elif not "o" in grid[0][grid[0].index("x")::]:
    grid[1] = new_string(grid[0].index("x")-1)
  elif grid[0].index("x") < grid[-1].index("x"):
    grid[1] = new_string(grid[0].index("x")+1)
  else:
    grid[1] = new_string(grid[0].index("x")-1)
  return 1 + hex_distance(grid[1::])

