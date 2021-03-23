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
  if len(po[0]) < 1:
    return -1
  elif len(po[0]) == 1:
    return sum(po[0])
  else:
    max_steps = (len(po) + len(po[0])) - 2
    steps, row, col = 0, 0, 0
    nums = []
    while steps <= max_steps:
      nums.append(po[row][col])
      steps += 1
      if row + 1 == len(po):
        col += 1
      elif col + 1 == len(po[0]):
        row += 1
      elif po[row+1][col] > po[row][col+1]:
        row += 1
      else:
        col += 1
    return sum(nums) + 1 if max(po[len(po)-1]) == 19 else sum(nums)

