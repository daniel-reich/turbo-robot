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
  g=[list(x) for x in g]
  A=[(i,j) for i in range(len(g)) for j in range(len(g[0]))]
  S=[x for x in A if g[x[0]][x[1]]=='o']
  d={x:[] for x in S}
  for s in S:
    for a in A:
      if s!=a and (abs(s[0]-a[0])==1 and s[1]==a[1]) or (abs(s[1]-a[1])==1 and s[0]==a[0]):
        if g[a[0]][a[1]]!='x':
          d[s].append(a)
  qu=[(x,y)]
  done={(x,y)}
  res=[]
  while qu:
    k=qu.pop(0)
    res.append(k)
    for x in d[k]:
      if x not in done:
        qu.append(x)
        done.add(x)
  for x in res:
    g[x[0]][x[1]]='+'
  return [''.join(x) for x in g]

