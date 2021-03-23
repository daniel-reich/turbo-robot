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
    d1,d2 = [],[]
    for i in range(3):
        col = [board[0][i],board[1][i],board[2][i]]
        if board[i].count('X')==3 or col.count('X')==3:return 'X'
        if board[i].count('O')==3 or col.count('O')==3:return 'O'
        d1 += [board[i][i]]
        d2 += [board[i][2-i]]
    if d1.count('X')==3:return 'X' 
    if d1.count('O')==3:return 'O'  
    return 'Draw'

