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
    knights = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 1:
                knights.append((row, col))
    for i in range(len(knights)):
        row1, col1 = knights[i]
        for j in range(i + 1, len(knights)):
            row2, col2 = knights[j]
            if sorted([abs(row1 - row2), abs(col1 - col2)]) == [1, 2]:
                return False
    return True

