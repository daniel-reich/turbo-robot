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

def check_board(letter, number):
  board = [ [ 0 for i in range(8) ] for j in range(8) ]
  letters = 'abcdefgh'
  board[8 - number][letters.index(letter)] = 'Q'
  dist_left = letters.index(letter)   # the four "dist" variables tell how far the Queen is from the 4 edges of the board
  dist_right = 7 - dist_left
  dist_down = number - 1
  dist_up = 8 - number
  for i in range(8):    # put 1's in all squares that are in same row as Q
    if board[8 - number][i] == 0:
      board[8 - number][i] = 1
  for i in range(8):    # put 1's in all squares that are in same column as Q
    if board[i][letters.index(letter)] == 0:
      board[i][letters.index(letter)] = 1
      
    # now, want to fill in the diagonals:
    
    # start with quadrant 1: up and right
  limit = min(dist_up, dist_right)
  for i in range(1, limit+1):
    board[8 - number - i][letters.index(letter) + i] = 1
  
    # quadrant 2: up and left
  limit = min(dist_up, dist_left)
  for i in range(1, limit+1):
    board[8 - number - i][letters.index(letter) - i] = 1
  
    # quadrant 3: down and left
  limit = min(dist_down, dist_left)
  for i in range(1, limit+1):
    board[8 - number + i][letters.index(letter) - i] = 1
  
    # quadrant 4: down and right
  limit = min(dist_down, dist_right)
  for i in range(1, limit+1):
    board[8 - number + i][letters.index(letter) + i] = 1
  board[8 - number][letters.index(letter)] = 0
  return board

