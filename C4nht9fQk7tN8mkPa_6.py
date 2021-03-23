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

import itertools
def cannot_capture(board):
  moves = list(itertools.product([1,-1],[2,-2])) + list(itertools.product([2,-2],[1,-1]))
  
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 1:
        for move in moves:
          if (0 <= i + move[0] <= len(board)-1) and (0 <= j + move[1] <= len(board[i])-1):
            if board[i+move[0]][j+move[1]] == 1:
              return False
  return True

