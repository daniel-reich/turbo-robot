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

import copy
​
def check_board(board, symbol):
    win_pos = [symbol] * 3
    for row in board:
        if row == win_pos:
            return True
    if [board[i][i] for i in range(3)] == win_pos or \
       [board[2-i][i] for i in range(3)] == win_pos:
        return True
    for c in range(3):
        col = [board[r][c] for r in range(3)]
        if col == win_pos:
            return True
    return False
​
def x_and_o(board):
    for i in range(3):
        board[i] = board[i].split('|')
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                new_board = copy.deepcopy(board)
                new_board[row][col] = 'X'
                if check_board(new_board, 'X'):
                    return [row + 1, col + 1]
    return False

