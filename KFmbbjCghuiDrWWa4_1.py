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

def validate_tic_tac_toe(b):
  count = sum('O X'.index(x) - 1 for x in ''.join(b))
​
  if not 0 <= count <= 1:
      return False
​
  b += [''.join(i[k] for i in b) for k in range(3)]
  b += [
      ''.join(b[k][k] for k in range(3)),
      ''.join(b[2 - k][k] for k in range(3))
  ]
​
  return 'XXX' not in b if count < 1 else 'OOO' not in b

