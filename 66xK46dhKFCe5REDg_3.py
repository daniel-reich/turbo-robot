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

def transpose(lst):
    return [list(x) for x in zip(*lst)]
​
​
def check_win(board) -> bool:
    for row, column in zip(board, transpose(board)):
        if row.count('X') == 3 or column.count('X') == 3:
            return True
​
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    return diagonal1.count('X') == 3 or diagonal2.count('X') == 3
​
​
def x_and_o(board):
    board = [row.split('|') for row in board]
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            temp = [[j for j in i] for i in board]
            temp[i][j] = 'X'
            if item.isspace():
                temp[i][j] = 'X'
                if check_win(temp):
                    return [i+1, j+1]
    else:
        return False

