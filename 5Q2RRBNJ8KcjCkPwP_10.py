"""


Create a function that takes a list of character inputs from a Tic Tac Toe
game. Inputs will be taken from player1 as `"X"`, player2 as `"O"`, and empty
spaces as `"#"`. The program will return the **winner** or **tie** results.

### Examples

    tic_tac_toe([
      ["X", "O", "O"],
      ["O", "X", "O"],
      ["O", "#", "X"]
    ]) ➞ "Player 1 wins"
    tic_tac_toe([
      ["X", "O", "O"],
      ["O", "X", "O"],
      ["X", "#", "O"]
    ]) ➞ "Player 2 wins"
    tic_tac_toe([
      ["X", "X", "O"],
      ["O", "X", "O"],
      ["X", "O", "#"]
    ]) ➞ "It's a Tie"

### Notes

N/A

"""

from numpy import transpose, diag
def tic_tac_toe(inputs):
  table = inputs
  sym_table = [_[::-1] for _ in table]
  lines = []
  for a in table:
    lines.append(set(a))
  for b in transpose(table):
    lines.append(set(b))
  lines.append(set(diag(table)))
  lines.append(set(diag(sym_table)))
  return 'Player 1 wins' if {'X'} in lines else 'Player 2 wins' if {'O'} in lines else 'It\'s a Tie'

