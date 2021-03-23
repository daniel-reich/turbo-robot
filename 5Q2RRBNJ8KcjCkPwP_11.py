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
  player = 0
  if inputs[0][0]== inputs[1][1] and inputs[2][2]==inputs[0][0]:
    if inputs[0][0]=="X":
      player=1
    else:
      player=2
  elif inputs[0][2]==inputs[1][1] and inputs[2][0]==inputs[0][2]:
    if inputs[1][1]=="X":
      player=1
    else:
      player=2
  elif inputs[0][0]==inputs[0][1] and inputs[0][2]==inputs[0][0]:
    if inputs[0][0]=="X":
      player=1
    else:
      player=2
  elif inputs[1][0]==inputs[1][1] and inputs[1][2]==inputs[1][0]:
    if inputs[1][1]=="X":
      player=1
    else:
      player=2
  elif inputs[2][0]==inputs[2][1] and inputs[2][2]==inputs[2][0]:
    if inputs[2][2]=="X":
      player=1
    else:
      player=2
  elif inputs[0][0]==inputs[1][0] and inputs[2][0]==inputs[0][0]:
    if inputs[0][0]=="X":
      player=1
    else:
      player=2
  elif inputs[0][1]==inputs[1][1] and inputs[2][1]==inputs[0][1]:
    if inputs[1][1]=="X":
      player=1
    else:
      player=2
  elif inputs[0][2]==inputs[1][2] and inputs[2][2]==inputs[0][2]:
    if inputs[2][2]=="X":
      player=1
    else:
      player=2
  else:
    player=0
  
  if player==1:
    return "Player 1 wins"
  elif player==2:
    return "Player 2 wins"
  else:
    return "It's a Tie"

