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
  pl = {"X": "1","O": "2" }
  for i in range(3):
    if inputs[i][0] == inputs[i][1] and inputs[i][1] == inputs[i][2]:
      return "Player " + pl[inputs[i][0]] + " wins"
    elif inputs[0][i] == inputs[1][i] and inputs[1][i] == inputs[2][i]:
      return "Player " + pl[inputs[0][i]] + " wins"
  if inputs[0][0] == inputs[1][1] and inputs[1][1] == inputs[2][2]:
    return "Player " + pl[inputs[1][1]] + " wins"
  elif inputs[0][2] == inputs[1][1] and inputs[1][1] == inputs[2][0]:
    return "Player " + pl[inputs[1][1]] + " wins"
  else:
    return "It's a Tie"

