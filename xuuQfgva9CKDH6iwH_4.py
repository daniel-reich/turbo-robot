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
    H, W = len(g), len(g[0])
    if g[x][y] != 'o':
        return g
    g = [list(r) for r in g]
    queue = [(x, y)]
    while len(queue) > 0:
        x, y = queue.pop(0)
        g[y][x] = '+'
        for x2, y2 in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if 0 <= x2 < W and 0 <= y2 < H and g[y2][x2] == 'o' and (x2, y2) not in queue:
                queue.append((x2, y2))
    return [''.join(r) for r in g]

