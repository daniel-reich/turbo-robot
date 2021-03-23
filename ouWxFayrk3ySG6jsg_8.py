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
    for i in range(3):
        if len(set(board[i]))==1:
            return board[i][0]
        if board[0][i]==board[1][i]==board[2][i]:
            return board[0][i]
    if board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0]:
        return board[1][1]
