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
    n, m = len(po), len(po[0])
    if n == 0 or m == 0:
        return -1
    if n == 1 and m == 1:
        return po[0][0]
    for c in range(1, m):
        po[0][c] += po[0][c-1]
    for r in range(1, n):
        po[r][0] += po[r-1][0]
    for r in range(1, n):
        for c in range(1, m):
            po[r][c] += max(po[r-1][c], po[r][c-1])
    return po[-1][-1]
