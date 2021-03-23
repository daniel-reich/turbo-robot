"""


You will be given a matrix representing a field `g` and two numbers `x`, `y`
coordinate.

There are three types of possible characters in the matrix:

  * `x` representing a rock.
  * `o` representing a dirt space.
  * `+` representing a grassed space.

You have to simulate grass growing from the position `(x, y)`. Grass can grow
in all four directions (up, left, right, down). Grass can only grow on dirt
spaces and can't go past rocks.

Return the simulated matrix.

### Examples

    simulate_grass([
      "xxxxxxx",
      "xooooox",
      "xxxxoox"
      "xoooxxx"
      "xxxxxxx"
    ], 1, 1) ➞ [
      "xxxxxxx",
      "x+++++x",
      "xxxx++x"
      "xoooxxx"
      "xxxxxxx"
    ]

### Notes

There will always be rocks on the perimeter

"""

def simulate_grass(g, x, y):
  if g[x][y] == 'x': return g
  grid = [list(l) for l in g]
  n,m = len(grid),len(grid[0])
  
  stack = [(x,y)]
  grid[x][y] = '+'
  while stack:
    x,y = stack.pop()
    for z,w in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
      if 0<=z<n and 0<=w<m and grid[z][w]=='o':
        grid[z][w] = '+'
        stack.append((z,w))
  return [''.join(l) for l in grid]

