"""


Create a function which creates a square dartboard of side length `n`. The
value of a number should increase, the closer it is to the centre of the
board.

### Examples

    make_dartboard(3) ➞ [
      111,
      121,
      111
    ]
    
    make_dartboard(8) ➞ [
      11111111,
      12222221,
      12333321,
      12344321,
      12344321,
      12333321,
      12222221,
      11111111
    ]
    
    make_dartboard(5) ➞ [
      11111,
      12221,
      12321,
      12221,
      11111
    ]

### Notes

If the size given is an even number, the centre should be made up of the 4
highest values.

"""

def make_dartboard(n):
  board = [[1]*n]
  
  for i in range(n//2):
    next_row = [board[-1][j]+1 if j in range(i+1,n-i-1) else board[-1][j] for j in range(len(board[-1]))]
    board.append(next_row)
  board += board[:n-len(board)][::-1]
  
  return [int(''.join(str(i) for i in row)) for row in board]

