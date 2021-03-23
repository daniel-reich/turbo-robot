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
  nL = 2*(grid[0].count("o") + grid[0].count("x")) -1
  
  pos = []
  sameLine = False
  for i in range(nL):
    aux = grid[i].split("x")
    Yshift = 0.5*abs(((nL+1)/2-1) -i)
    if len(aux) == 3:
      sameLine = True
      pos = pos + [[i, aux[0].count("o") + Yshift]]
      pos = pos + [[i, aux[0].count("o") + 1 + aux[1].count("o") + Yshift]]
    elif len(aux) == 2:
      pos = pos + [[i, aux[0].count("o") + Yshift]]
  deltaX2 = abs(pos[1][1]*2 - pos[0][1]*2)//1
  deltaY = abs(pos[1][0] - pos[0][0])
  if sameLine:
    return deltaX2//2
  elif deltaX2 <= deltaY:
    return deltaY
  else:
    return deltaY + (deltaX2-deltaY)//2

