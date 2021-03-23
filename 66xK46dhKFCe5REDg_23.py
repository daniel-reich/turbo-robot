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
    def win_test(board):
        if any([1 if row.count("X")==3 else 0 for row in board]):return True
        if any([1 if row.count("X")==3 else 0 for row in [list(i) for i in zip(*board)][::-1]]):return True
        if all([1 if board[y][y]=="X" else 0 for y in range(3) ]):return True
        if all([1 if board [2-y][y]=="X" else 0 for y in range(3) ]):return True
        return False
    board,to_test=[row.split("|") for row in board],[]    
    for y in range(3):
        for x in range(3):
            if board[y][x]==" ":
                to_test.append((y,x))
    for pos in to_test:        
        board[pos[0]][pos[1]]="X"        
        if win_test(board): return [pos[0]+1,pos[1]+1]
        board[pos[0]][pos[1]]=" "
    return False

