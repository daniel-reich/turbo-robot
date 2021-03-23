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

# re-use solution from other challenges:
​
def check_triple(triple):
    # check whether a triple of values is a winning position:
    return len(set(triple)) == 1 and triple[0] != 's'
​
def isSolved(board):
    # first check if there's a winner:
    # check rows:
    for row in board:
        if check_triple(row):
            return row[0]
    # check columns:
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if check_triple(column):
            return column[0]
    # check diagonals:
    if check_triple([board[i][i] for i in range(3)]):
        return board[0][0]
    if check_triple([board[i][2-i] for i in range(3)]):
        return board[2][0]
    #
    # no winner:
    return "Draw"
​
def tic_tac_toe(inputs):
    ans = isSolved(inputs)
    if ans == "Draw":
        return "It's a Tie"
    return "Player 1 wins" if ans == "X" else "Player 2 wins"
​
def ticTacToe(inputs):
    return tic_tac_toe(inputs)

