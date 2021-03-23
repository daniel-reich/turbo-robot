"""


Create a function that takes **a character from a to h** as the column number
and **an integer from 1 to 8** as the row number which together represent the
location of a queen on a normal-sized chess board. Return this two dimensional
8x8 list.

This list must consist of zeroes and ones. The ones are placed in positions
where the queen can move in one move and zeroes represent positions on the
board where it cannot.

### Examples

    check_board("a", 1) ➞ [
      [1, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 1, 0],
      [1, 0, 0, 0, 0, 1, 0, 0],
      [1, 0, 0, 0, 1, 0, 0, 0],
      [1, 0, 0, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 0],
      [1, 1, 0, 0, 0, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1]
    ]
    
    check_board("h", 4) ➞ [
      [0, 0, 0, 1, 0, 0, 0, 1],
      [0, 0, 0, 0, 1, 0, 0, 1],
      [0, 0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 0],
      [0, 0, 0, 0, 0, 0, 1, 1],
      [0, 0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 1, 0, 0, 1]
    ]
     
    check_board("c", 8) ➞ [
      [1, 1, 0, 1, 1, 1, 1, 1],
      [0, 1, 1, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 0, 1, 0],
      [0, 0, 1, 0, 0, 0, 0, 1],
      [0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0]
    ]

### Notes

The queens' current position is a zero as it is impossible to move to this
position during one turn, because the queen is already there.

"""

def check_board(col, row):
    board = [[0 for c in range(8)] for r in range(8)]
    row, col = 8 - row, ord(col) - 97
    for c in range(col + 1, 8):
        board[row][c] = 1
    for c in range(col - 1, -1, -1):
        board[row][c] = 1
    for r in range(row + 1, 8):
        board[r][col] = 1
    for r in range(row - 1, -1, -1):
        board[r][col] = 1
    r, c = row + 1, col + 1
    while r < 8 and c < 8:
        board[r][c] = 1
        r += 1
        c += 1
    r, c = row - 1, col + 1
    while r >= 0 and c < 8:
        board[r][c] = 1
        r -= 1
        c += 1
    r, c = row + 1, col - 1
    while r < 8 and c >= 0:
        board[r][c] = 1
        r += 1
        c -= 1
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        board[r][c] = 1
        r -= 1
        c -= 1
    return board

