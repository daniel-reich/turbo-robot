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
    g = [list(i) for i in g]
    stack = [[x, y]]
    
    while stack:
        x, y = stack.pop()
        if g[x][y] != 'o':
            continue
        g[x][y] = '+'
        stack += [[x, y-1], [x-1, y], [x+1, y], [x, y+1]]
        
    return [''.join(i) for i in g]

