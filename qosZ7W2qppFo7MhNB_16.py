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
    p = []; c = len(grid); mid = (c + 1) / 2
    for [m, i] in list(zip(*[grid, range(c)])):
        grid[i] = ''.join([k for k in m if k != ' '])
    [p.append([i, abs(mid - (i + 1)) * 0.5 + j]) if le == 'x' else 0 for [m, i] in
     list(zip(*[grid, range(c)])) for [le, j] in list(zip(*[m, range(len(m))]))]
    li, co = abs(p[1][0] - p[0][0]), abs(p[1][1] - p[0][1])
    return round(li + co - min(li / 2, co))

