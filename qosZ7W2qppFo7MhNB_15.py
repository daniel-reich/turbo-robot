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
    coords = [] 
    for i in range(len(grid)):
        if grid[i].count('x') == 2:
            return (grid[i].rindex('x') - grid[i].index('x'))//2
        if 'x' in grid[i]:
            coords.append((i, grid[i].index('x')))
    (y1, x1), (y2, x2) = coords
    if x2 == x1:
        return y2 - y1
    moves = 0
    while y1 < y2:
        x1 = x1 + 1 if x2 >= x1 else x1 - 1
        y1 += 1
        moves += 1
    return moves if x2 == x1 else moves + abs(x2 - x1)//2

