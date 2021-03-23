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
  A=[list(x) for x in zip(*inputs)]
  B=[[inputs[i][i] for i in range(3)]]
  C=[[inputs[i][2-i] for i in range(3)]]
  S=inputs+A+B+C
  if ['X']*3 in S:
    return "Player 1 wins"
  elif ['O']*3 in S:
    return "Player 2 wins"
  else:
    return "It's a Tie"

