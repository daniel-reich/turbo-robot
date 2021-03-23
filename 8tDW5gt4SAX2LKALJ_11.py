"""


This is a sequel to [Chain Reaction (Part
#1)](https://edabit.com/challenge/bf3QRDxH9Ns2SZWZw), with the same setup, but
a different flavor.

As in the previous part, you will be given a rectangular array representing a
"map" with three types of spaces:

  * "+" bombs: when activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
  * "x" bombs: when activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
  * Empty spaces "0".

The goal is simple: **given a map, return the minimum number of bombs that
need to be set off for all bombs to be destroyed by the chain reaction**.

Let's look at some examples:

    [
      ["+", "+", "+", "0", "+", "+", "+"],
      ["+", "+", "+", "0", "0", "+", "+"]
    ]

For the map above, the answer is `2`; to explode all bombs you just need to
set off one "+" bomb in the right cluster and one in the left cluster.

    [
      ["x", "0", "x"],
      ["x", "x", "x"]
    ]

For the map above, the answer is `3`; clearly setting off the three bottom "x"
bombs is enough, and no less than three bombs suffice.

    [
      ["x", "x", "x", "0", "x"],
      ["x", "x", "x", "x", "x"],
      ["x", "x", "x", "0", "x"]
    ]

For the map above, the answer is `3`; setting off the three rightmost bombs in
the middle row will do the trick.

### Examples

    min_bombs_needed([
      ["+", "+", "+", "0", "+", "+", "+"],
      ["+", "+", "+", "0", "0", "+", "+"]
    ]) ➞ 2
    
    min_bombs_needed([
      ["x", "0", "x"],
      ["x", "x", "x"]
    ]) ➞ 3
    
    min_bombs_needed([
      ["x", "x", "x", "0", "x"],
      ["x", "x", "x", "x", "x"],
      ["x", "x", "x", "0", "x"]
    ]) ➞ 3

### Notes

  * Note that both "+" and "x" bombs have an "explosion range" of 1.
  * To limit the difficulty, in this challenge each map will have only "+" or only "x" bombs. The more challenging case of maps with both "+" and "x" bombs will be [part 3](https://edabit.com/challenge/LLieA2XafALFxXRT5)!
  * Figuring out what to do is half the fun, but if you'd prefer to just handle the coding, a hint on to how to attack this challenge can be found in the comments.

"""

def min_bombs_needed(grid):
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
    cnt = 0
​
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '+':
                hov(grid, row, col, i, j)
                cnt += 1
            if grid[i][j] == 'x':
                dia(grid, row, col, i, j)
                cnt += 1
​
    return cnt

