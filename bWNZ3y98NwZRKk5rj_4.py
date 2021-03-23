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
    a_row, a_col = a // 3, a % 3
    b_row, b_col = b // 3, b % 3
    d_1, d_2 = {0, 4, 8}, {2, 4, 6}
    if a_row == b_row:
        return a_row * 3 + 3 - a_col - b_col
    elif a_col == b_col:
        return (3 - a_row - b_row) * 3 + a_col
    elif a in d_1 and b in d_1:
        return (d_1 - {a} - {b}).pop()
    elif a in d_2 and b in d_2:
        return (d_2 - {a} - {b}).pop()

