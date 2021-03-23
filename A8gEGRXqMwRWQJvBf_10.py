"""


Given a 3x3 matrix of a completed tic-tac-toe game, create a function that
returns whether the game is a win for `"X"`, `"O"`, or a `"Draw"`, where `"X"`
and `"O"` represent themselves on the matrix, and `"E"` represents an empty
spot.

### Examples

    tic_tac_toe([
      ["X", "O", "X"],
      ["O", "X",  "O"],
      ["O", "X",  "X"]
    ]) ➞ "X"
    
    tic_tac_toe([
      ["O", "O", "O"],
      ["O", "X", "X"],
      ["E", "X", "X"]
    ]) ➞ "O"
    
    tic_tac_toe([
      ["X", "X", "O"],
      ["O", "O", "X"],
      ["X", "X", "O"]
    ]) ➞ "Draw"

### Notes

Make sure that if **O** wins, you return the letter `"O"` and not the integer
**0** (zero) and if it's a draw, make sure you return the capitalised word
`"Draw"`. If you return `"X"` or `"O"`, make sure they're capitalised too.

"""

def tic_tac_toe(board):
  primary_diag = []
  secondary_diag = []
  horizontal = []
  vertical_0 = []
  vertical_1 = []
  vertical_2 = []
  
  for i in range(3):
    primary_diag.append(board[i][i])
    secondary_diag.append(board[i][-i - 1])
    horizontal.append("".join(board[i]))
    vertical_0.append(board[i][0])
    vertical_1.append(board[i][1])
    vertical_2.append(board[i][2])
  
  primary_diag = ["".join(primary_diag)]
  secondary_diag = ["".join(secondary_diag)]
  vertical_0 = ["".join(vertical_0)]
  vertical_1 = ["".join(vertical_1)]
  vertical_2 = ["".join(vertical_2)]
​
  lines = primary_diag + secondary_diag + horizontal + vertical_0 + vertical_1 + vertical_2
  
  if "XXX" in lines:
    return "X"
  elif "OOO" in lines:
    return "O"
  else:
    return "Draw"

