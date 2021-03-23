"""


The function is given a rectangular matrix consisting of zeros and ones. Count
the number of different regions and return the result. A separate region is a
collection of ones interconnected horizontally and vertically. A region can
have holes in it.

### Examples

    num_regions([
      [1, 1, 1, 1, 0],
      [1, 1, 0, 1, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0]
    ]) ➞ 1
    num_regions([
      [1, 1, 1, 1, 0],
      [1, 0, 0, 1, 0],
      [1, 1, 1, 1, 0],
      [0, 0, 0, 0, 1]
    ]) ➞ 2
    
    # The region on the upper left looks like a doughnut.
    num_regions([
      [1, 1, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 1, 0, 1],
      [0, 0, 0, 1, 1]
    ]) ➞ 3

### Notes

N/A

"""

def num_regions(m):
    parts = 0
    ones = set()
    H, W = len(m), len(m[0])
    for r in range(H):
        for c in range(W):
            if m[r][c] == 1:
                ones.add((r, c))
    while len(ones) > 0:
        parts += 1
        queue = [ones.pop()]
        while len(queue) > 0:
            row, col = queue.pop(0)
            for r, c in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
                if 0 <= r < H and 0 <= c < W and (r, c) in ones:
                    ones.remove((r, c))
                    queue.append((r, c))
    return parts

