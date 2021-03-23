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

def find_neighbors(g, r, c):
    n_rows, n_cols = len(g), len(g[0])
    if g[r][c] == '+':
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    elif g[r][c] == 'x':
        neighbors = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
    return [(r + tpl[0], c + tpl[1]) for tpl in neighbors
            if 0 <= r + tpl[0] < n_rows and
            0 <= c + tpl[1] < n_cols and
            g[r + tpl[0]][c + tpl[1]] in '+x']
​
​
def all_explode(grid):
    chain = [[(0, 0)]]
    n_total_bombs = sum(c in '+x' for row in grid for c in row)
    activate = True
    n_activated_bombs = 1
    while activate:
        activate = False
        previous_link = chain[-1]
        new_link = []
        for p_tpl in previous_link:
            for new_tpl in find_neighbors(grid, *p_tpl):
                already_in = False
                for lst in chain:
                    if new_tpl in lst:
                        already_in = True
                        break
                if not already_in:
                    new_link.append(new_tpl)
                    n_activated_bombs += 1
        if new_link:
            chain.append(new_link)
            activate = True
    return n_total_bombs == n_activated_bombs

