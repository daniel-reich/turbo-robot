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

def tic_tac_toe(inputs):
  lines = inputs + list(map(list, zip(*inputs))) \
    + [[inputs[i][i] for i in range(3)], [inputs[2-i][i] for i in range(3)]]
  if ['X', 'X', 'X'] in lines: return "Player 1 wins"
  if ['O', 'O', 'O'] in lines: return "Player 2 wins"
  return "It's a Tie"

