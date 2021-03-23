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
  row=8-row
  board=[[0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],]
  a='abcdefgh'
  col=a.index(col)
  board[row]=[1]*8
  for i in range(len(board)):
    board[i][col]=1
  board[row][col]=0
  for i in range(8):
    if row+i<8 and col+i<8: board[row+i][col+i]=1
  for i in range(8):
    if row-i>=0 and col+i<8: board[row-i][col+i]=1
  for i in range(8):
    if row+i<8 and col-i>=0: board[row+i][col-i]=1
  for i in range(8):
    if row-i>=0 and col-i>=0: board[row-i][col-i]=1
  board[row][col]=0
  print((col+1,row+1))
  for i in board:
    print(i)
  return board

