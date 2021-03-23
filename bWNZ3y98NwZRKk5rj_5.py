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

solution = {(0, 1): 2, (0, 2): 1, (1, 2): 0,  # first row
            (3, 4): 5, (3, 5): 4, (4, 5): 3,  # second row
            (6, 7): 8, (6, 8): 7, (7, 8): 6,  # third row
            (0, 3): 6, (0, 6): 3, (3, 6): 0,  # first column
            (1, 4): 7, (1, 7): 4, (4, 7): 1,  # second column
            (2, 5): 8, (2, 8): 5, (5, 8): 2,  # third column
            (0, 8): 4, (4, 8): 0, (0, 4): 8,  # diagonal top left to bottom right
            (2, 4): 6, (4, 6): 2, (2, 6): 4,  # diagonal top right to bottom left
            }
​
def block_player(a, b):
    return solution[(a, b)]

