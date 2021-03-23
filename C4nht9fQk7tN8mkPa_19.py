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

def knight(b, i, j):
  if i > 1:
    if j >0:
      if b[i-2][j-1] == 1:
        return True
    if j < len(b[i])-1:
      if b[i-2][j+1] == 1:
        return True
  if i < len(b)-2:
    if j >0:
      if b[i+2][j-1] == 1:
        return True
    if j < len(b[i])-1:
      if b[i+2][j+1] == 1:
        return True
  if i > 0:
    if j >1:
      if b[i-1][j-2] == 1:
        return True
    if j < len(b[i])-2:
      if b[i-1][j+2] == 1:
        return True
  if i < len(b)-1:
    if j >1:
      if b[i+1][j-2] == 1:
        return True
    if j < len(b[i])-2:
      if b[i+1][j+2] == 1:
        return True
def cannot_capture(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 1:
        if knight(board,i,j):
          return False
  return True

