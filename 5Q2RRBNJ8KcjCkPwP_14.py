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
winner = {'X':"1",'O':"2"}
​
def tic_tac_toe(inputs):
  inputs_np = np.array(inputs)
  inputs_diag = np.diag(inputs_np).tolist()
  inputs_col = np.rot90(inputs_np)
  inputs_col_lst = inputs_col.tolist()
  inputs_diag2 = np.diag(inputs_col).tolist()
  if len(set(inputs_diag)) == 1:
    return "Player {} wins".format(winner[inputs[0][0]])
  elif len(set(inputs_diag2)) == 1:
    return "Player {} wins".format(winner[inputs[0][2]])
  else:
    for i in range(0,3):
      if len(set(inputs[i])) == 1:
        return "Player {} wins".format(winner[inputs[i][0]])
      elif len(set(inputs_col_lst[i])) == 1:
        return "Player {} wins".format(winner[inputs_col_lst[i][0]])
    return "It's a Tie"

