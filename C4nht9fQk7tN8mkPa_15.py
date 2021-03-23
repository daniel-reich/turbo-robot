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
  for i in range(8):
    for j in range(8):
      if board[i][j] == 1:
        if helper(board,i,j):
          return False
  return True
      
def helper(board,row,col):
  rslt = [chk(board,row+2,col+1),chk(board,row+2,col-1),
          chk(board,row-2,col+1),chk(board,row-2,col-1),
          chk(board,row+1,col+2),chk(board,row+1,col-2),
          chk(board,row-1,col+2),chk(board,row-1,col-2)]
  return any(rslt)
  
def chk(board,row,col):
  if(row < 0 or col < 0 or row > 7 or col > 7):
    return False
  else:
    return board[row][col] == 1

