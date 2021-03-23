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

def x_and_o(board):
    board = [i.split('|') for i in board]
​
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = 'X'
                row = board[r]
                col = [board[0][c], board[1][c], board[2][c]]
                d_1 = [board[0][0], board[1][1], board[2][2]]
                d_2 = [board[0][2], board[1][1], board[2][0]]
                if any(i == ['X', 'X', 'X'] for i in (row, col, d_1, d_2)):
                    return [r+1, c+1]
                board[r][c] = ' '
    return False

