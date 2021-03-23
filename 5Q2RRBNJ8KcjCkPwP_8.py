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

def isWinner(inputs):
  for l in inputs + list(zip(*inputs)):
    if len(set(l)) == 1: return l[0]
  if inputs[0][0] == inputs[1][1] == inputs[2][2]: return inputs[1][1]
  if inputs[2][0] == inputs[1][1] == inputs[0][2]: return inputs[1][1]
  return ""
  
def tic_tac_toe(inputs):
  res = isWinner(inputs);
  return ("Player " + str(1 + int(res == 'O')) + " wins") if res else "It's a Tie"

