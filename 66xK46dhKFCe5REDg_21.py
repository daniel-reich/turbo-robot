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
    matrix, codes = [], {'X': 1, 'O': -1, ' ': 0}
    for s in board:
        matrix.append([codes[c] for c in s.split('|')])
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                if sum(matrix[i]) == 2 \
                        or matrix[0][j] + matrix[1][j] + matrix[2][j] == 2:
                    return [i + 1, j + 1]
                if i == 1 and j == 1:
                    if matrix[0][0] + matrix[2][2] == 2 \
                            or matrix[2][0] + matrix[0][2] == 2:
                        return [i + 1, j + 1]
                if i == 0 and j == 0:
                    if matrix[1][1] + matrix[2][2] == 2:
                        return [i + 1, j + 1]
                if i == 0 and j == 2:
                    if matrix[1][1] + matrix[2][0] == 2:
                        return [i + 1, j + 1]
                if i == 2 and j == 0:
                    if matrix[1][1] + matrix[0][2] == 2:
                        return [i + 1, j + 1]
                if i == 2 and j == 2:
                    if matrix[1][1] + matrix[0][0] == 2:
                        return [i + 1, j + 1]
    return False

