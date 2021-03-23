"""


In this challenge you will be given a rectangular list representing a "map"
with three types of spaces:

  *  **"+" bombs:** When activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
  *  **"x" bombs:** When activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
  * Empty spaces "0".

Consider the grid:

    [
      ["+", "+", "0", "x", "x", "+", "0"],
      ["0", "+", "+", "x", "0", "+", "x"]
    ]

If the top left "+" bomb explodes, the resulting chain reaction will blow up
bombs in the order given by the numbers below:

    [
      ["1", "2", "0", "x", "6", "8", "0"],
      ["0", "3", "4", "5", "0", "7", "8"]
    ]

Note that there are two 8's since two of the bombs explode at the same time.
Also, note that one of the "x" bombs in the top row does not explode.

Write a function that determines if the chain reaction started when the _top
left bomb_ explodes destroys all bombs or not.

### Examples

    all_explode([
      ["+", "+", "+", "+", "+", "+", "x"]
    ]) ➞ True
    
    all_explode([
      ["+", "+", "+", "+", "+", "0", "x"]
    ]) ➞ False
    
    all_explode([
      ["+", "+", "0", "x", "x", "+", "0"],
      ["0", "+", "+", "x", "0", "+", "x"]
    ]) ➞ False
    
    all_explode([
      ["x", "0", "0"],
      ["0", "0", "0"],
      ["0", "0", "x"]
    ]) ➞ False
    
    all_explode([
      ["x", "0", "x"],
      ["0", "x", "0"],
      ["x", "0", "x"]
    ]) ➞ True

### Notes

  * Both "+" and "x" bombs have an "explosion range" of 1.
  * Part #2 can be [found here](https://edabit.com/challenge/8tDW5gt4SAX2LKALJ).

"""

dir_h = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir_d = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
​
def set_off_bomb(grid, r, c):
  if grid[r][c] == '0':
    return
  dirs = []
  if grid[r][c] == '+':
    dirs = dir_h
  if grid[r][c] == 'x':
    dirs = dir_d
  grid[r][c] = '0'
  for r2, c2 in [(r+dir[0], c+dir[1]) for dir in dirs if 0<=r+dir[0]<len(grid) and 0<=c+dir[1]<len(grid[0])]:
    set_off_bomb(grid, r2, c2)
​
def all_explode(grid):
  set_off_bomb(grid, 0, 0)
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] != '0':
        return False
  return True

