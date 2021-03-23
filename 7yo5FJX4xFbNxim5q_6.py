"""


Harry is a postman. He's got a post office with a size of `n*m(a matrix / 2D
list)`. Each slot at the 2D list represents the number of letters in that
spot. Harry can only go right and down. He starts at (0, 0), and ends at (n-1,
m-1). `n` represents the height, and `m` the length. Return the maximum amount
of letters he can pick up. He can only pick up letters if he is on that spot.

### Examples

    harry([[5, 2], [5, 2]]) ➞ 12
    # (5+5+2)
    harry([
      [1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15]
    ]) ➞ 72
    # (1+6+11+12+13+14+15)
    harry([[]]) ➞ -1

### Notes

Like you saw in example 3, if the matrix is empty, return `-1`.

"""

def harry(po):
  if not po[0]:
    return -1
  n = len(po)-1
  m = len(po[0])-1
  if not (n or m):
    return po[0][0]
  elif not n:
    return po[n][m] + harry([i[:-1] for i in po])
  elif not m:
    return po[n][m] + harry(po[:-1])
  else:
    return po[n][m] + max(harry(po[:-1]), harry([i[:-1] for i in po]))

