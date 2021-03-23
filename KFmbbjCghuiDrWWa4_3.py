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
  xcount = lambda board: str(board).count('X')
  ocount = lambda board: str(board).count('O')
  
  #Rule 1: There must be either an equal amout of Xs and Os or 1 less O than Xs
  
  if ocount(board) not in [xcount(board), xcount(board) - 1]:
    return False
  
  #Rule 2: There cannot be 2 winning conditions:
  
  cols = [''.join([board[r][c] for r in range(3)]) for c in range(3)]
  
  if ('XXX' in board or 'XXX' in cols) and ('OOO' in board or 'OOO' in cols):
    return False
  
  return True

