"""


Given a matrix of m * n elements (m rows, n columns), return all elements of
the matrix in spiral order.

### Examples

    spiral_order([
      [ 1, 2, 3 ],
      [ 4, 5, 6 ],
      [ 7, 8, 9 ]
    ]) ➞ [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    spiral_order([
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]) ➞ [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

### Notes

NA

"""

def spiral_order(m):
    res = []
    while m:
        res += m[0]
        m = m[1:]
        if not m:
            break
        right_wall = []
        for r, row in enumerate(m):
            right_wall.append(row[-1])
            m[r] = row[:-1]
        res += right_wall
        if not m:
            break
        res += m[-1][::-1]
        m = m[:-1]
        if not m:
            break
        left_wall = []
        for r in range(len(m) - 1, -1, -1):
            left_wall.append(m[r][0])
            m[r] = m[r][1:]
        res += left_wall
    return res

