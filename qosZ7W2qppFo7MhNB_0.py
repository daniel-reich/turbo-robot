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

def hex_distance(G):
  E = enumerate
  [x, y], [u, v] = [[x, y] for y, R in E(G) for x, c in E(R) if 'x' == c in R]
  for _ in range(v - y): x += x < u or -1
  return v + abs(x - u) / 2 - y
