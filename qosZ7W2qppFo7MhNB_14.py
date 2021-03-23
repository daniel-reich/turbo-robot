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

def scan(grid):
  p1 = None
  p2 = None
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j]=='x':
        if p1==None:
          p1 = [i,j]
        else:
          p2 = [i,j]
          return p1,p2
          
def hex_distance(grid):
  for g in grid: print(g)
  p1,p2 = scan(grid)
  dy = p2[0]-p1[0]
  dx = max(abs(p2[1]-p1[1])-dy,0)//2
  return dx+dy

