"""


Write a function that returns `True` if the knights are placed on a chessboard
such that **no knight can capture another knight**. Here, `0`s represent empty
squares and `1`s represent knights.

### Examples

    cannot_capture([
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 1, 0],
      [0, 1, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 1, 0, 0, 0]
    ]) ➞ True
    
    cannot_capture([
      [1, 0, 1, 0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 0, 1],
      [0, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 1, 0, 0, 1, 0, 1],
      [1, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0, 1, 0, 1],
      [1, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 1, 0, 1, 0, 1]
    ]) ➞ False

### Notes

  * Knights can be present in any of the 64 squares.
  * No other pieces except knights exist.

"""

import numpy as np
testboard = [
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]
                             ]
# testboard = np.array(testboard)
# def get_horses(np):
#   horse_positions = []
#   for x, i in enumerate(testboard):
#     for y, j in enumerate(i):
#       if j == 1:
#         horse_positions.append((x, y))
#       else:
#         pass
#   return horse_positions
​
def get_horses(board):
  x = np.where(board == 1)
  y = list(zip(x[0], x[1]))
  return(y)
​
​
​
​
​
def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return True 
    else: 
        return False
​
knight_moves = [(-1, 2), (-1, -2), (-2, 1), (-2, 1), (1,-2), (1, 2), (2,-1), (2, 1)]
​
def possible_moves(current_pos):
  pos_moves = []
  x, y = current_pos
  for i, j in knight_moves:
    pos_moves.append((x+i, y+j))
  return pos_moves
​
​
def cannot_capture(list_of_lists):
  board = np.array(list_of_lists)
  horse_positions = get_horses(board)
  for horse in horse_positions:
    moves = possible_moves(horse)
    if common_member(moves, horse_positions):
      return False
    else:
      pass
  return True
​
​
print(cannot_capture(testboard))

