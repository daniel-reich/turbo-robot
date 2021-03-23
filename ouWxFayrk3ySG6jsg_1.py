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

ROWS = (16449, 257, 5121, 68, 20740, 1028, 4176, 272, 17424)
def who_won(board):
    s = sum(r for x, r in zip(sum(board,[]), ROWS) if x=='X')
    return 'X' if s & 21845 & s >> 1 else 'O'

