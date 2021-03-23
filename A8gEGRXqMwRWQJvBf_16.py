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
    fdiag = []
    rdiag = []
    for i in range(len(board)):
        
        row = board[i]
        #if rows are same value
        if all(val == row[0] for val in row):
            return row[0]
        
        #calculate column
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
            
            #front diagonal is where i=j
            if i == j:
                fdiag.append(board[j][i])
                
                #reverse diagonal middle case
                if i == 1:
                    rdiag.append(board[j][i])
            #reverse diagonal other cases
            if (j == 0 and i == 2) or (j == 2 and i == 0):
                rdiag.append(board[j][i])
                
        #if col is the same
        if all(val == col[0] for val in col):
            return col[0]
        
    #if front diagonal is same
    if all(val == fdiag[0] for val in fdiag):
        return fdiag[0]
    #if reverse diagonal is same
    if all(val == rdiag[0] for val in rdiag):
        return rdiag[0]
        
    return 'Draw'

