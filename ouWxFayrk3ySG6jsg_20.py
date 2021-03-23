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
  for i in board:
    l = []
    for j in i:
      l.append(j)
    if l[0] == l[1] and l[0] == l[2]:
      return l[0]
        
  if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
    return board[0][0]
  board.reverse()
  if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
    return board[0][0]
  if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
    return board[0][0]
  if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
    return board[0][1]
  if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
    return board[0][2]

