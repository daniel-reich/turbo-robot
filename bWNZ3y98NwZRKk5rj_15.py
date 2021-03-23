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
  straight = [[0,1,2],[3,4,5],[6,7,8]]
  inverse = [list(x) for x in zip(*straight)]
  diagonals = [[0,4,8],[2,4,6]]
  lst = straight+inverse+diagonals
  res = [x for x in lst if a in x and b in x][0]
  return [x for x in res if a!=x!=b][0]

