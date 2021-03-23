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
    grid = [x.split("|") for x in board]
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == " ":
                grid[r][c] = "X"
                if check(grid):
                    return [r + 1, c + 1]
                else: 
                    grid[r][c] = " "
    return False            
​
def check(x):
    r = any([set(i) == {"X"} for i in x])
    c = any([set(i) == {"X"} for i in zip(*x)])
    d1 = set([x[i][i] for i in range(len(x))]) == {"X"}
    d2 = set([x[i][len(x) - 1 - i] for i in range(len(x))]) == {"X"}
    return r or c or d1 or d2

