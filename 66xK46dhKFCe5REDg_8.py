"""


Given a list containing three strings, representing the rows of an O's and X's
board from top to bottom, return the row and column position of the winning
move for X's. Return `False` if the game cannot be won.

### Examples

    x_and_o(board = [" | | ", " |X| ", "X| | "]) ➞  [1, 3]
    
    # Board becomes:
    #    |   |
    #    |X |
    # X |   |
    
    x_and_o(board = ["X|X|O", "O|X| ", "X|O| "]) ➞ [3, 3]
    
    # Board becomes:
    # X|X|O
    # O|X|
    # X|O|

### Notes

There is no 0 index for the row or column.

"""

def x_and_o(board):
  board = [row.split("|") for row in board]
  blanks = [[i,j] for i in [0,1,2] for j in [0,1,2] if board[i][j]==" "]
  for [i,j] in blanks:
    if [board[i][k] for k in [0,1,2]].count("X") == 2: return [i+1,j+1]
    if [board[k][j] for k in [0,1,2]].count("X") == 2: return [i+1,j+1]
    if i==j and [board[k][k] for k in [0,1,2]].count("X") == 2: return [i+1,j+1]
    if i+j==2 and [board[k][2-k] for k in [0,1,2]].count("X")==2: return [i+1,j+1]
  return False

