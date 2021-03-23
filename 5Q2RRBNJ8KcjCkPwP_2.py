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

def tic_tac_toe(b):
    cols = [list(i) for i in zip(*b)]
    dia1 = [[b[0][0], b[1][1], b[2][2]]]
    dia2 = [[b[2][0], b[1][1], b[0][2]]]
    for i in b + cols + dia1 + dia2:
        if set(i) == {'X'}:
            return 'Player 1 wins'
        if set(i) == {'O'}:
            return 'Player 2 wins'
    return "It's a Tie"

