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
  arr = [[j for j in i] for i in g]
  arr[x][y] = "+"
  while True:
    changes = 0
    for i in range(0,len(arr)):
      for j in range(0,len(arr[0])):
        if arr[i][j] == "o":
          if any(arr[a][b] == "+" for a,b in zip([i-1,i,i,i+1],[j,j-1,j+1,j])):
            arr[i][j] = "+"
            changes += 1
    if changes == 0:
      return [''.join(j for j in i) for i in arr]

