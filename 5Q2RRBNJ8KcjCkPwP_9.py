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

def tic_tac_toe(board):
  rows = board
  cols = list(map(list, zip(*board)))
  diag1 = [[board[i][i] for i in range(3)]]
  diag2 = [[board[i][-i-1] for i in range(3)]]
  
  combs = rows + cols + diag1 + diag2
  if ['X', 'X', 'X'] in combs:
    return 'Player 1 wins'
  elif ['O', 'O', 'O'] in combs:
    return 'Player 2 wins'
  else:
    return "It's a Tie"

