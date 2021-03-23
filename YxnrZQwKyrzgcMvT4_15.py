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

from copy import deepcopy
def rotate_transform(l, n):
    l_ = deepcopy(l)
    if n%4 >= 1 :
        for k in range(n%4):
            for i in range(len(l)):
                for j in range(len(l)):
                    l_[j][len(l)-i-1]= l[i][j]
        return rotate_transform(l_, (n%4)-1)
    return l_

