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
  if num>0:
    c=0
    while c<num:
      lst=[list(x)[::-1] for x in zip(*lst)]
      c+=1
    return lst
  else:
    c=0
    while c<abs(num):
      lst=[list(x) for x in zip(*lst)][::-1]
      c+=1
    return lst

