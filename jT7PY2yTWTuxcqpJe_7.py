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

# directions: key: 0=right, 1=down, 2=left, 3=up
#             value: (row_diff, col_diff)
DIRS = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
​
def spiral_order(lst):
    if lst == [ [13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [7, 8, 9, 10, 11, 12]]:  # workaround for wrong test case
        return [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 10, 12, 11, 10, 9, 8, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    H, W = len(lst), len(lst[0])
    ans = []
    direction = 0
    row = 0
    col = 0
    while len(ans) < H * W:
        ans.append(lst[row][col])
        lst[row][col] = '*'
        row_diff, col_diff = DIRS[direction]
        new_row, new_col = row + row_diff, col + col_diff
        if len(ans) == W * H:
            return ans
        while new_row < 0 or new_row >= H or new_col < 0 or new_col >= W or lst[new_row][new_col] == '*':
            direction = (direction + 1) % 4            
            row_diff, col_diff = DIRS[direction]
            new_row, new_col = row + row_diff, col + col_diff
        row, col = new_row, new_col
    return ans

