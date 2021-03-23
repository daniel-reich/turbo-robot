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

import copy
​
def x_and_o(board):
  board = [board_string.split('|') for board_string in board]
  for x in range(1, 4):
    for y in range(1, 4):
      if can_win(board, x, y):
        return [y, x]
        
  return False
  
def can_win(board, x, y):
  if board[y - 1][x - 1] != ' ':
    return False
    
  temp_board = copy.deepcopy(board)
  temp_board[y - 1][x - 1] = 'X'
  return board_is_won(temp_board)
  
def board_is_won(board):
  return any([
    all_are_x(board[0]),
    all_are_x(board[2]),
    all_are_x(board[y][0] for y in range(3)),
    all_are_x(board[y][2] for y in range(3)),
    all_are_x(board[x][x] for x in range(3)),
    all_are_x(board[x][2 - x] for x in range(3))
  ])
  
def all_are_x(itr):
  return all(c == 'X' for c in itr)

