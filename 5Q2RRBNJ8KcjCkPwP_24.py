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
    for i in range(0, 3):
        if all(inputs[i][j] == inputs[i][0] for j in range(1, 3)):
            return "Player 1 wins" if inputs[i][0] == "X" else "Player 2 wins"
    for j in range(0, 3):
        if all(inputs[i][j] == inputs[0][j] for i in range(1, 3)):
            return "Player 1 wins" if inputs[i][0] == "X" else "Player 2 wins"
    if all(inputs[i][i] == inputs[0][0] for i in range(1, 3)):
        return "Player 1 wins" if inputs[0][0] == "X" else "Player 2 wins"
    if all(inputs[i][2-i] == inputs[0][2] for i in range(1, 3)):
        return "Player 1 wins" if inputs[0][2] == "X" else "Player 2 wins"
    return "It's a Tie"

