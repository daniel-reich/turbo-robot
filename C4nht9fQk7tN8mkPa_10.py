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

def cannot_capture(board):
  positions = []
  # get positions of all knights
  [[positions.append((row_num, col_num)) if col == 1 else None for col_num, col in enumerate(row)] for row_num, row in enumerate(board)]
  # get all possible moves for all knights
  p_dict = {}
​
  for p in positions:
    p_dict[p] = getAllMoves(p[0], p[1])
  
  # compare all possible moves to each knight position
  # if match; return False else return True
  all_possible_moves = []
  for row in p_dict.values():
    all_possible_moves.extend(row)
  
  for value in all_possible_moves:
    if value in positions:
      return False
  return True
  
def getAllMoves(x, y):
    m1 = [1, -1]
    m2 = [2, -2]
    moves = []
    [[moves.append((x + i, y + k)) for i in m1] for k in m2]
    [[moves.append((x + k, y + i)) for i in m1] for k in m2]
    return moves

