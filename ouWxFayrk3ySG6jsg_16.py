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
  row = [i[0] for i in board if len(set(i))==1]
  col = [k[0] for k in [[i[j] for i in board] for j in range(3)] if len(set(k))==1]
  dia1 = [board[0][0]] if len(set([board[i][i] for i in range(3)]))==1 else []
  dia2 = [board[1][1]] if len(set([board[i][2-i] for i in range(3)]))==1 else []
  s = row + col + dia1 + dia2
  return s[0]

