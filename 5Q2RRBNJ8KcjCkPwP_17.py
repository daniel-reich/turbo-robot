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
    a = check(inputs)
    b = check(zip(*inputs))
    c = [[inputs[i][i] for i in range(3)], [inputs[i][2 - i]for i in range(3)]]
    c = check(c)  
    return a or b or c or "It's a Tie"
    
def check(x):
    for i in x:
        if len(set(i)) == 1:
            return "Player {} wins".format(["2", "1"][set(i) == {"X"}])
    return ""

