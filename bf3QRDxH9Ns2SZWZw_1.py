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

dplus = [[1, 0], [-1, 0], [0, 1], [0, -1]]
dstar = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
​
def all_explode(grid):
    assert grid[0][0] in ['+', 'x']
    explosion_queue = [(0, 0, grid[0][0])]
    bombs = set()
    W, H = len(grid[0]), len(grid)
    for row in range(H):
        for col in range(W):
            if grid[row][col] in ['+', 'x']:
                bombs.add((row, col))
    while len(explosion_queue):
        (row, col, btype) = explosion_queue.pop(0)
        neighbourhood = dplus if btype == '+' else dstar
        bombs.remove((row, col))
        for drow, dcol in neighbourhood:
            row2, col2 = row + drow, col + dcol
            if (row2, col2) in bombs and \
               (row2, col2, grid[row2][col2]) not in explosion_queue:
                explosion_queue.append((row2, col2, grid[row2][col2]))
    return len(bombs) == 0

