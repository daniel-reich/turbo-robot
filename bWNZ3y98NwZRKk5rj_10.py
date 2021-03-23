"""


Create a function that returns a number which can block the player from
reaching 3 in a row in a game of Tic Tac Toe. The number given as an argument
will correspond to a grid of Tic Tac Toe: topleft is 0, topright is 2,
bottomleft is 6, and bottomright is 8.

  * Create a function that takes two numbers `a`, `b` and returns another number.
  * This number should be the final one in a line to block the player from winning.

### Examples

    block_player(0, 3) ➞ 6
    
    block_player(0, 4) ➞ 8
    
    block_player(3, 5) ➞ 4

### Notes

The values given will always have two filled squares in a line.

"""

def block_player(a, b):
  i = [[0,1,2],[3,4,5],[6,7,8]]
  for x in range(9):
    y = sorted([x,a,b])
    if (y[2]-y[1]) == (y[1]-y[0]):
      if (y[1]-y[0]) == 2:
        if y[1] != 4:
          pass
        else:
          return x
      else: 
        return x
    else:
      pass

