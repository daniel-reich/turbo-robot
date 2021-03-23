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

import numpy as np
def x_and_o(board):
  grid = np.array([[string[i] for i in range(0,5,2)] for string in board])
  grid2 = np.rot90(grid)
  indices = [[i // 3, i % 3] for i in range(0,9) if grid[i//3][i%3] == " "]
  def diagonal_can_win(board):
    return np.diag(board).tolist().count("X") == 2
  def can_win(i,j):
    if grid.tolist()[i].count("X") == 2:
      return True
    elif grid2.tolist()[2-j].count ("X") == 2:
      return True
    elif i == 1 and j == 1:
      return diagonal_can_win(grid) or diagonal_can_win(grid2)
    elif i == j:
      return diagonal_can_win(grid)
    elif i + j == 2:
      return diagonal_can_win(grid2)
    else:
      return False
  print(grid)
  print(grid2)
  for el in indices:
    if can_win(el[0],el[1]):
      return [el[0] + 1, el[1] + 1]
  return False

