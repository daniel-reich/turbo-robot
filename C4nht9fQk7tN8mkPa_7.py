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
  i, j = (0, 0)
  while i < 8:
    j = 0
    while j < 8:
      if board[i][j] == 1:
        if 0 <= (j-2) < 8:
          if 0 <= (i-2) < 8:
            if board[i-1][j-2] == 1:
              return False
            elif board[i-2][j-1] == 1:
              return False
          if 0 <= (i+2) < 8:
            if board[i+2][j-1] == 1:
              return False
            elif board[i+1][j-2] == 1:
              return False
      
        if 0 <= (j+2) < 8:
          if 0 <= (i-2) < 8:
            if board[i-1][j+2] == 1:
              return False
            elif board[i-2][j+1] == 1:
              return False
          if 0 <= (i+2) < 8:
            if board[i+2][j+1] == 1:
              return False
            elif board[i+1][j+2] == 1:
              return False
      j += 1
    i += 1
  return True

