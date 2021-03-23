"""


Create a function that takes a Tic-tac-toe board and returns `"X"` if the X's
are placed in a way that there are three X's in a row or returns `"O"` if
there is three O's in a row.

### Examples

    who_won([
      ["O", "X", "O"],
      ["X", "X", "O"],
      ["O", "X", "X"]
    ]) ➞ "X"
    
    who_won([
      ["O", "O", "X"],
      ["X", "O", "X"],
      ["O", "X", "O"]
    ]) ➞ "O"

### Notes

  * There are no Ties.
  * All places on the board will have either "X" or "O".
  * Check **Resources** for more info.

"""

def who_won(board):
  if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
      return 'X'
  if board[1][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
      return 'X' 
  if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
      return 'X'
  if board[0][1] == 'X':
    if board[1][1] == 'X' and board[2][1] == 'X':
      return 'X'
    else:
      return 'O'
  elif board[0][0] == 'X':
    if board[1][1] == 'X' and board[2][2]=='X'or board[1][0] == 'X' and board[2][0] == 'X':
      return 'X'
    else:
      return 'O'
  elif board[0][2] == 'X':
    if board[1][1] == 'X' and board[2][0]=='X'or board[1][2]=='X' and board[2][2] == 'X':
      return 'X'
    else:
      return 'O'

