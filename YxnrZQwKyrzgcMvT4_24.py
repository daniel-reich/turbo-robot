"""


Create a function to rotate a two-dimensional matrix of `N * N` integer
elements `num` times, where if `num` is positive, the rotation is
**clockwise** , and if not, **counterclockwise**.

### Examples

    rotate_transform([
      [2, 4],
      [0, 0]
    ], 1) ➞ [
      [0, 2],
      [0, 4]
    ]
    rotate_transform([
      [2, 4],
      [0, 0]
    ], -1) ➞ [
      [4, 0],
      [2, 0]
    ]

### Notes

N/A

"""

def rotate_transform(lst, num):
  l = [0]*len(lst)
  m = [[0 for i in range(len(lst))] for j in range(len(lst))]
  for i in range(0, len(lst)):
    for j in range(0, len(lst)):
      if num > 0:
        m[i][j] = lst[len(lst)-j-1][i]
      else:
        m[i][j] = lst[j][len(lst)-i-1]  
  if num > 1:
    return rotate_transform(m, num - 1)
  elif num < 1:
    return rotate_transform(m, num + 1)
  else:
    return m

