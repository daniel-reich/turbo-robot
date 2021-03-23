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
  rows = board[:]
  cols = list(map(list, zip(*board)))
  diag1 = [[board[i][i] for i in range(3)]]
  diag2 = [[board[i][2-i] for i in range(3)]]
  P = rows + cols + diag1 + diag2
  for p in P:
    if len(set(p)) == 1:
      return p[0]

