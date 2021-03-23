"""


The function is given a list of three strings representing a board. The
characters can be `"X", "O", " "`. The first player writes `"X"` at first
turn. If a player has three marks in a row, column or a diagonal, the game
stops. Given the board evaluate if this state can be achieved in line with the
rules, return `True / False`.

### Examples

    validate_tic_tac_toe(["X  ", "   ", "   "]) ➞ True
    # X goes first.
    
    validate_tic_tac_toe(["O  ", "   ", "   "]) ➞ False
    # O cannot go first.
    
    validate_tic_tac_toe(["X X", " O ", "   "]) ➞ True
    # Two X and one O is a possible state.
    
    validate_tic_tac_toe(["XOX", " X ", "   "]) ➞ False
    # Three X and one O is not a possible state.
    # Players have to go one after another.

### Notes

N/A

"""

def validate_tic_tac_toe(board):
  rows = ",".join(board)
  cols = ",".join(["".join(board[r][c] for r in range(3)) for c in range(3)])
  diags = "".join([board[i][i] for i in range(3)]) + "," + "".join([board[2-i][i] for i in range(3)])
  if not 0<=rows.count('X')-rows.count('O')<=1:
    return False
  lines = rows + "," + cols + "," + diags
  cX, cO = lines.count("XXX"), lines.count("OOO")
  if cX and cO:
    return False
  return True

