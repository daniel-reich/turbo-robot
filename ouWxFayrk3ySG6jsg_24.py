"""


Create a function that takes a Tic-tac-toe board and returns `"X"` if the X's
are placed in a way that there are three X's in a row or returns `"O"` if
there is three O's in a row.

### Examples

    who_won([
      ["O", "X", "O"],
      ["X", "X", "O"],
      ["O", "X", "X"]
    ]) ➞ "X"
    
    who_won([
      ["O", "O", "X"],
      ["X", "O", "X"],
      ["O", "X", "O"]
    ]) ➞ "O"

### Notes

  * There are no Ties.
  * All places on the board will have either "X" or "O".
  * Check **Resources** for more info.

"""

def who_won(board):
    for x in range(len(board)):
​
        #Horizontal
        if len(set(board[x]))==1:
            return board[x][0]
        #Verticals
        if len(set([board[0][x],board[1][x],board[2][x]]))==1:
            return board[0][x]
​
        #Diagonals
    if len(set([row[i] for i,row in enumerate(board)])) ==1:
        return board[0][0]
​
    if len(set([row[-i-1] for i,row in enumerate(board)])) ==1:
        return board[2][0]

