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

def all_explode(grid):
​
    def hov(grid, row, col, x, y):
        if grid[x][y] == '0':
            return
        if grid[x][y] == 'x':
            return dia(grid, row, col, x, y)
        grid[x][y] = '0'
​
        if x != 0:
            hov(grid, row, col, x-1, y)
        if x < row-1:
            hov(grid, row, col, x+1, y)
        if y != 0:
            hov(grid, row, col, x, y-1)
        if y != col-1:
            hov(grid, row, col, x, y+1)
​
    def dia(grid, row, col, x, y):
        if grid[x][y] == '0':
            return
        if grid[x][y] == '+':
            return hov(grid, row, col, x, y)
        grid[x][y] = '0'
​
        if x != 0 and y != 0:
            dia(grid, row, col, x-1, y-1)
        if x < row-1 and y != col-1:
            dia(grid, row, col, x+1, y+1)
        if x != 0 and y != col-1:
            dia(grid, row, col, x-1, y+1)
        if x < row-1 and y != 0:
            dia(grid, row, col, x+1, y-1)
​
    row = len(grid)
    col = len(grid[0])
​
    if grid[0][0] == '+':
        hov(grid, row, col, 0, 0)
    if grid[0][0] == 'x':
        dia(grid, row, col, 0, 0)
​
    for i in grid:
        for j in i:
            if j == '+' or j == 'x':
                return False
    else:
        return True

