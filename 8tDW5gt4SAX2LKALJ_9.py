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

def cross(r, c, rlen, clen): 
    return [(row, col) for row, col in [[r + 1, c + 1], [r + 1, c - 1], [r - 1, c + 1], [r - 1, c - 1]] \
                if 0 <= row < rlen and 0 <= col < clen]
        
def plus(r, c, rlen, clen): 
    return [(row, col) for row, col in [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]] \
                if 0 <= row < rlen and 0 <= col < clen]
​
def bomb_cells_set(grid):
    bcs = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != '0':
                bcs.add((r, c))
    return bcs
​
def detonate_bomb(grid, row, col):
    dirs = cross if grid[row][col] == 'x' else plus
    grid[row][col] = '0'
    for r, c in dirs(row, col, len(grid), len(grid[0])):
        if grid[r][c] != '0':
            detonate_bomb(grid, r, c)
​
def min_bombs_needed(grid):
    bcs = bomb_cells_set(grid)
    if len(bcs) == 0:
        return 0
    nb = 0
    for cell in bcs:
        if grid[cell[0]][cell[1]] != '0':
            nb += 1
            detonate_bomb(grid, *cell)
    return nb

