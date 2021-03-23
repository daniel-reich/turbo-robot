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
  sy, sx = len(po), len(po[0])
  if sx == 0: return -1
  
  dp = [0] * (sy * sx)
  dp[0] = po[0][0]
  
  for y in range(0, sy):
    for x in range(0, sx):
      n = [po[y][x]]
      if y: n.append(dp[(y-1) * sx + x] + po[y][x])
      if x: n.append(dp[y * sx + (x-1)] + po[y][x])
      dp[y * sx + x] = max(n)
​
  return dp.pop()

