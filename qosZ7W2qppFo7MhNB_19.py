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
  A=[]
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j]=='x':
        A.append((i,j))
  s1,s2=abs(A[1][0]-A[0][0]), abs(A[1][1]-A[0][1])
  if s1==0:
    d=s2//2
  else:
    if s2//s1==1 or s2==0:
      d=s1
    else:
      d=s1+((s2-s1)//2 if s1<s2 else 0)
  return abs(d)

