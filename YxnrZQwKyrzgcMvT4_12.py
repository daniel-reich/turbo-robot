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

def rotate_transform(M, num):
    if abs(num) % 4 == 0:
        return M
    if num > 0:
        for _ in range(num % 4):
            M = [row[::-1] for row in [list(i) for i in zip(*M)]]
        return M
    return rotate_transform(M, 4-abs(num))

