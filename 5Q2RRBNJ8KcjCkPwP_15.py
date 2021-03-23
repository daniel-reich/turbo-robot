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
    for row in inputs:
        s = set(row)
        if len(s) == 1:
            res = 1 if s.pop() == 'X' else 2
            return 'Player {} wins'.format(res)
    for col in zip(*inputs):
        s = set(col)
        if len(s) == 1:
            res = 1 if s.pop() == 'X' else 2
            return 'Player {} wins'.format(res)
    d1 = set(inputs[i][i] for i in range(3))
    if len(d1) == 1:
        res = 1 if d1.pop() == 'X' else 2
        return 'Player {} wins'.format(res)
    d2 = set(inputs[i][2 - i] for i in range(3))
    if len(d2) == 1:
        res = 1 if d2.pop() == 'X' else 2
        return 'Player {} wins'.format(res)
    return 'It\'s a Tie'

