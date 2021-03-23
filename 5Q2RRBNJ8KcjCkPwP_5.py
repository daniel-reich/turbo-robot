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
    c = [list(i) for i in zip(*inputs)]
    dlr = [[inputs[0][0], inputs[1][1], inputs[2][2]]]
    drl = [[inputs[2][0], inputs[1][1], inputs[0][2]]]
    for i in inputs + c + dlr + drl:
        if set(i) == {'X'}:
            return 'Player 1 wins'
        elif set(i) == {'O'}:
            return 'Player 2 wins'
    return "It's a Tie"

