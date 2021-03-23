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

def whoWon(b):
  cols = [list(i) for i in zip(*b)]
  dia1 = [[b[0][0], b[1][1], b[2][2]]]
  dia2 = [[b[2][0], b[1][1], b[0][2]]]
  for i in b + cols + dia1 + dia2:
    if set(i) == {'X'}:
      return 'X'
  return 'O'

