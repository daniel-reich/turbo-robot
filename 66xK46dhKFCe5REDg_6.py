"""


Given a list containing three strings, representing the rows of an O's and X's
board from top to bottom, return the row and column position of the winning
move for X's. Return `False` if the game cannot be won.

### Examples

    x_and_o(board = [" | | ", " |X| ", "X| | "]) ➞  [1, 3]
    
    # Board becomes:
    #    |   |
    #    |X |
    # X |   |
    
    x_and_o(board = ["X|X|O", "O|X| ", "X|O| "]) ➞ [3, 3]
    
    # Board becomes:
    # X|X|O
    # O|X|
    # X|O|

### Notes

There is no 0 index for the row or column.

"""

BIN = (16449, 68, 4176, 257, 20740, 272, 5121, 1028, 17424)
​
def x_and_o(board):
    brd = tuple(zip(range(9), '|'.join(board)[::2], BIN))
    brdsum = sum(s for i,c,s in brd if c=='X')
    for i,c,s in brd:
        if c == ' ' and 2*s & brdsum:
            return [i//3 + 1, i%3 + 1]
    return False

