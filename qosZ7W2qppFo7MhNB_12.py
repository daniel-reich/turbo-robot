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
    a, b = [], []
    for i in range(len(grid)):
        if grid[i].count('x') == 1:
            if not a:
                a = [i, grid[i].index('x')]
            else:
                b = [i, grid[i].index('x')]
        elif grid[i].count('x') == 2:
            a = [i, grid[i].index('x')]
            b = [i, grid[i].rfind('x')]
    if b[0] == a[0]:
        return abs(b[1] - a[1]) // 2
    if abs(b[1] - a[1]) < b[0] - a[0]:
        return b[0] - a[0]
    return (b[0] - a[0]) + (abs(b[1] - a[1]) - (b[0] - a[0])) // 2

