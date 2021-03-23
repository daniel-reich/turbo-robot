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

def rotate_transform(arr, num):
  k = (-num)%4
  for _ in range(k):
    rot(arr)
  return arr
​
def rot(arr):
  for i in range(len(arr)):
    for j in range(i):
      arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
  arr.reverse()

