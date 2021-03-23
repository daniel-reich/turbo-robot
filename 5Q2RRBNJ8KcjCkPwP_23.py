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

def tic_tac_toe(bd):
    d = {'X':'1', 'O':'2'}
    lor = []
    for row in bd:
        lor.append(row)
    tbd = map(list, zip(*bd))
    for row in tbd:
        lor.append(row)
    lor.append([bd[0][0], bd[1][1], bd[2][2]])
    lor.append([bd[0][2], bd[1][1], bd[2][0]])
    
    for row in lor:
        if row[0] == row[1] == row[2]:
            return 'Player ' + d[row[0]] + ' wins'
    return "It's a Tie"

