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

def chk(arr,tar):
  if any(row.count(tar) == 3 for row in arr):
    return True
  if any(row.count(tar) == 3 for row in zip(*arr)):
    return True
  if all(arr[i][i] == tar for i in range(3)):
    return True
  new_arr = [row[::-1] for row in arr]
  if all(new_arr[i][i] == tar for i in range(3)):
    return True
  return False
​
def tic_tac_toe(inputs):
  if chk(inputs,'X'):
    return "Player 1 wins"
  elif chk(inputs,'O'):
    return "Player 2 wins"
  return "It's a Tie"

