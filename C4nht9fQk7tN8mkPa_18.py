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
  for i in range(7):
    for j in range(8):
      if(i>5):
        if(j<=1):
          if(board[i][j]*board[i+1][j+2]==1):
            return False
        elif(j>5):
          if(board[i][j]*board[i+1][j-2]==1):
            return False
        else:
          if(board[i][j]*board[i+1][j+2]==1 or board[i][j]*board[i+1][j-2]==1):
            return False
      else:
        if(j<=1):
          if(board[i][j]*board[i+1][j+2]==1 or board[i][j]*board[i+2][j+1]==1):
            return False
        elif(j>5):
          if(board[i][j]*board[i+1][j-2]==1or board[i][j]*board[i+2][j-1]==1):
            return False
        else:
          if(board[i][j]*board[i+1][j+2]==1 or board[i][j]*board[i+1][j-2]==1 or board[i][j]*board[i+2][j+1]==1 or board[i][j]*board[i+2][j-1]==1):
            return False
  return True

