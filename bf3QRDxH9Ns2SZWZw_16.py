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

from collections import deque
​
​
def explode(idx, bombtype, max_x, max_y):
    x, y = idx
    chain = {'+': [(1, 0), (0, 1), (0, -1), (-1, 0)],
             'x': [(1, 1), (-1, 1), (1, -1), (-1, -1)],
             '0': [(0, 0)]}
    return [(x+i, y+j) for i, j in chain[bombtype]
            if 0 <= x+i <= max_x and 0 <= y+j <= max_y]
​
​
def all_explode(grid):
    max_x, max_y = len(grid[0]) - 1, len(grid) - 1
    queue = deque([(0, 0)])
    avail_bombs = sum(i == '+' or i == 'x' for row in grid for i in row)
    exploded = [(j, i) for i, row in enumerate(grid)
                for j, v in enumerate(row) if v == '0']
    while queue:
        x, y = queue.pop()
        new_explosions = explode((x, y), grid[y][x], max_x, max_y)
        for explosion in new_explosions:
            if explosion not in exploded:
                avail_bombs -= 1
                if not avail_bombs:
                    return True
                exploded.append(explosion)
                queue.appendleft(explosion)
    return False

