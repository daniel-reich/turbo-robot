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
    winner = {"X":"Player 1 wins","O":"Player 2 wins"}
    columns = list(map(list,zip(*inputs)))
    diag1 = [[inputs[i][i] for i in range(3)]]
    diag2 = [[inputs[::-1][i][i] for i in range(3)]]
    ans = [i for i in columns + diag1 + diag2 + inputs if len(set(i)) == 1]
    return winner[ans[0][0]] if len(ans) == 1 else "It's a Tie"

