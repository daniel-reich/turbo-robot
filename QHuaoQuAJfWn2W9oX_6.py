"""


Create a function that takes **a character from a to h** as the column number
and **an integer from 1 to 8** as the row number which together represent the
location of a queen on a normal-sized chess board. Return this two dimensional
8x8 list.

This list must consist of zeroes and ones. The ones are placed in positions
where the queen can move in one move and zeroes represent positions on the
board where it cannot.

### Examples

    check_board("a", 1) ➞ [
      [1, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 1, 0],
      [1, 0, 0, 0, 0, 1, 0, 0],
      [1, 0, 0, 0, 1, 0, 0, 0],
      [1, 0, 0, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 0],
      [1, 1, 0, 0, 0, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1]
    ]
    
    check_board("h", 4) ➞ [
      [0, 0, 0, 1, 0, 0, 0, 1],
      [0, 0, 0, 0, 1, 0, 0, 1],
      [0, 0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 0],
      [0, 0, 0, 0, 0, 0, 1, 1],
      [0, 0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 1, 0, 0, 1]
    ]
     
    check_board("c", 8) ➞ [
      [1, 1, 0, 1, 1, 1, 1, 1],
      [0, 1, 1, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 0, 1, 0],
      [0, 0, 1, 0, 0, 0, 0, 1],
      [0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0]
    ]

### Notes

The queens' current position is a zero as it is impossible to move to this
position during one turn, because the queen is already there.

"""

def check_board(col, row):
  r = ord(col) - ord('a')
  c = 8 - row
​
  def on_treat(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
      return True
    if abs(x1 - x2) == abs(y1 - y2):
      return True
    return False
​
  rows = [[0 for _ in range(8)] for _ in range(8)]
  for i in range(8):
    for j in range(8):
      if on_treat(i, j, c, r):
        rows[i][j] = 1
  rows[c][r] = 0
  return rows

