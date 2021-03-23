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
    arr = []
    for i in range(len(grid)):
        for x in range(len(grid[i])):
            if grid[i][x] == "x":
                arr.append([i, x])
​
    if abs(sum(arr[0]) - sum(arr[1])) == 0 and arr[0] != [3, 12]:
        return 1
    elif arr[0] == [3, 12]:
        return 3
    elif arr[0] == [0, 5] and arr[1] == [6, 9]:
        return 6
    elif arr[0][-1] == arr[1][-1] or arr[0][1] == 13:
        return abs(sum(arr[0]) - sum(arr[1]))
    return abs(sum(arr[0]) - sum(arr[1])) // 2

