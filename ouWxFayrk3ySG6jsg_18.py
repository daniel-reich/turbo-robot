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
        for j in range(3):
            if board[i][j] == "O" or board[i][j] == "X":
                t = True
    if t:
        tout = [board[0][2] + board[1][1] + board[2][0], board[0][0] + board[1][1] + board[2][2]]
        for i in range(3):
            b = ""
            c = ""
            for j in range(3):
                b += board[j][i]
                c += board[i][j]
            tout.append(b)
            tout.append(c)
        for t in tout:
            if t[0] == t[1] == t[2]:
                return t[0]

