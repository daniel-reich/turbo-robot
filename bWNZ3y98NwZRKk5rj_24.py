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

def block_player(*a):
  d={
    (0,1):2,(0,2):1,(0,4):8,(0,8):4,(0,3):6,(0,6):3,
    (1,4):7,(1,7):4,(1,0):2,(1,2):0,
    (2,0):1,(2,1):0,(2,5):8,(2,8):5,(2,4):6,(2,6):4,
    (3,0):1,(3,1):0,(3,4):5,(3,5):4,
    (4,1):7,(4,7):1,(4,2):6,(4,6):2,(4,0):8,(4,8):0,(4,3):5,(4,5):3,
    (5,4):3,(5,3):4,(5,2):8,(5,8):2,
    (6,0):3,(6,3):0,(6,4):2,(6,2):4,(6,7):8,(6,8):7,
    (7,1):4,(7,4):1,(7,6):8,(7,8):6,
    (8,0):4,(8,4):0,(8,6):7,(8,7):6,(8,5):2,(8,2):5
    }
  return d[a]

