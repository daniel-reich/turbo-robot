"""


Write a function that returns `True` if the knights are placed on a chessboard
such that **no knight can capture another knight**. Here, `0`s represent empty
squares and `1`s represent knights.

### Examples

    cannot_capture([
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 1, 0],
      [0, 1, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 1, 0, 0, 0]
    ]) ➞ True
    
    cannot_capture([
      [1, 0, 1, 0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 0, 1],
      [0, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 1, 0, 0, 1, 0, 1],
      [1, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0, 1, 0, 1],
      [1, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 1, 0, 1, 0, 1]
    ]) ➞ False

### Notes

  * Knights can be present in any of the 64 squares.
  * No other pieces except knights exist.

"""

def cannot_capture(board):
  checks = []
  def check_capture(x, y, board, line):
    if x >= 0 and x < len(board) and y >= 0 and y < len(line):
      return board[x][y]
  for i, line in enumerate(board):
    for j, cell in enumerate(line):
      if cell == 1:
        checks.append(check_capture(i+2, j+1, board, line))
        checks.append(check_capture(i+2, j-1, board, line))
        checks.append(check_capture(i-2, j+1, board, line))
        checks.append(check_capture(i-2, j-1, board, line))
        checks.append(check_capture(i+1, j+2, board, line))
        checks.append(check_capture(i+1, j-2, board, line))
        checks.append(check_capture(i-1, j+2, board, line))
        checks.append(check_capture(i-1, j-2, board, line))
  if 1 in checks:
    return False
  else:
    return True

