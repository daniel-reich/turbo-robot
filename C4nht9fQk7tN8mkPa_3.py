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
  def check_plays(col_n, row_n):
    plays = [(col_n - 1, row_n + 2), (col_n - 1, row_n - 2),
             (col_n + 1, row_n + 2), (col_n + 1, row_n - 2),
             (col_n + 2, row_n - 1), (col_n - 2, row_n - 1),
             (col_n + 2, row_n + 1), (col_n - 2, row_n + 1)]
​
    for play in plays:
      try:
        if play[0]<0 or play[1]<0:
          continue
        elif board[play[1]][play[0]] == 1:
          return True
      except IndexError:
        continue
    return False
​
  for row_n, l in enumerate(board):
    for col_n, field in enumerate(l):
      if field == 1:
        if check_plays(col_n, row_n):
          return False
  return True

