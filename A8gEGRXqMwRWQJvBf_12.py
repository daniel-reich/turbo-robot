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
  r1 = board[0]
  r2 = board[1]
  r3 = board[2]
  c1 = [board[0][0], board[1][0], board[2][0] ]
  c2 = [board[0][1], board[1][1], board[2][1] ]
  c3 = [board[0][2], board[1][2], board[2][2] ]
  d1 = [board[0][0], board[1][1], board[2][2]]
  d2 = [board[0][2], board[1][1], board[2][0]]
  all_poss = [r1,r2,r3,c1,c2,c3,d1,d2]
  for a in all_poss:
    if a.count('X') == 3:
      return 'X'
    elif a.count('O') == 3:
      return 'O'
  return "Draw"

