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

import math
​
def hex_distance(grid):
  A, B = find_start_end(grid)
  Ax, Ay = A
  Bx, By = B
  
  steps = 0
  while Ax != Bx or Ay != By:
    if Ay < By:
      Ay += 1
      Ax += math.copysign(1, Bx - Ax)
    elif Ay > By:
      Ay -= 1
      Ax += math.copysign(1, Bx - Ax)
    else:
      Ax += math.copysign(1, Bx - Ax) * 2
      
    steps += 1
    
  return steps
  
def find_start_end(grid):
  return [ (x, y) for y, string in enumerate(grid)
                  for x, char in enumerate(string)
                  if char == 'x' ]

