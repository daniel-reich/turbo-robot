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
    d = [''.join(row[i] for i, row in enumerate(inputs)), ''.join(inputs[j][i] for i,j in enumerate(range(2,-1,-1)))]
    r = [''.join(row) for row in inputs] + [''.join(row) for row in list(zip(*inputs))] + d
    return "Player 1 wins" if 'XXX' in r else "Player 2 wins" if 'OOO' in r else "It's a Tie"

