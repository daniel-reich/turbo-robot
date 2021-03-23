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
def make_chain(grid, row, col):
    chain = [[(row, col)]]
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
                if not already_in and new_tpl not in new_link:
                    new_link.append(new_tpl)
                    n_activated_bombs += 1
        if new_link:
            chain.append(new_link)
            activate = True
    return {tpl for link in chain for tpl in link}
​
​
def min_bombs_needed(grid):
    remaining_bombs = {(r, c) for r, row in enumerate(grid)
                       for c, val in enumerate(row) if val in '+x'}
    chain_count = 0
    while remaining_bombs:
        chain = make_chain(grid, *remaining_bombs.pop())
        remaining_bombs -= chain
        chain_count += 1
    return chain_count

