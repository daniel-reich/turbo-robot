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

import numpy as np
​
def tic_tac_toe(inputs):
  i = np.array(inputs)
  lines = np.r_[i, i.T, [np.diag(i)], [np.diag(np.rot90(i))]]
  return {"X": "Player 1 wins", "O": "Player 2 wins"}.get(([l[0] for l in lines if len(set(l)) == 1] or ["_"])[0], "It's a Tie")

