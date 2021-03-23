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
  #map string index to board position
  colIndex = {0:1, 2:2, 4:3}
  #check rows
  winRow = 1
  for rowI, rowS in enumerate(board, start=1):
    if rowS.count('X') == 2 and rowS.count(' ') == 1:
      return [rowI, colIndex[rowS.index(' ')]]
  #check column
  transpose = [list(row) for row in zip(*board)]
  for colI in [0,2,4]:
    colS = transpose[colI]
    if colS.count('X') == 2 and colS.count(' ') == 1:
      return[colS.index(' ') + 1, colIndex[colI]]
  #check diag
  diag1 = [board[0][0], board[1][2], board[2][4]]
  if diag1.count('X') == 2 and diag1.count(' ') == 1:
    return [diag1.index(' ') + 1, diag1.index(' ') + 1]
    
  diag2 = [board[0][4], board[1][2], board[2][0]]
  if diag2.count('X') == 2 and diag2.count(' ') == 1:
    return [diag2.index(' ') + 1, 3 - diag2.index(' ')]
  
  return False

