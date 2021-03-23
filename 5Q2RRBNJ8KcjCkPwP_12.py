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
  row = [i for i in inputs]
  col = [[inputs[i][j] for i in range(3)] for j in range(3)]
  dia = [[inputs[i][i] for i in range(len(inputs))], [inputs[i][len(inputs)-1-i] for i in range(len(inputs))]]
  a = [i[0] for i in row + col + dia if len(set(i))==1]
  return "Player {} wins".format([1,2][a[0]!="X"]) if a!=[] else "It's a Tie"

