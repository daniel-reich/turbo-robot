"""


Given a 3x3 matrix of a completed tic-tac-toe game, create a function that
returns whether the game is a win for `"X"`, `"O"`, or a `"Draw"`, where `"X"`
and `"O"` represent themselves on the matrix, and `"E"` represents an empty
spot.

### Examples

    tic_tac_toe([
      ["X", "O", "X"],
      ["O", "X",  "O"],
      ["O", "X",  "X"]
    ]) ➞ "X"
    
    tic_tac_toe([
      ["O", "O", "O"],
      ["O", "X", "X"],
      ["E", "X", "X"]
    ]) ➞ "O"
    
    tic_tac_toe([
      ["X", "X", "O"],
      ["O", "O", "X"],
      ["X", "X", "O"]
    ]) ➞ "Draw"

### Notes

Make sure that if **O** wins, you return the letter `"O"` and not the integer
**0** (zero) and if it's a draw, make sure you return the capitalised word
`"Draw"`. If you return `"X"` or `"O"`, make sure they're capitalised too.

"""

def tic_tac_toe(board):
    f = lambda *a: board[a[0]][a[1]] == board[a[2]][a[3]] == board[a[4]][a[5]]
​
    horizontal = [(0, 0, 0, 1, 0, 2), (1, 0, 1, 1, 1, 2), (2, 0, 2, 1, 2, 2)]
    vertical = [(0, 0, 1, 0, 2, 0), (0, 1, 1, 1, 2, 1), (0, 2, 1, 2, 2, 2)]
    diagonal = [(0, 0, 1, 1, 2, 2), (-1, -1, -2, -2, -3, -3)]
    
    for direction in horizontal + vertical + diagonal:
        if f(*direction):
            return board[direction[0]][direction[1]]
​
    return "Draw"

