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
    '''
    Returns (r, c) if X can win by placing an X on the next move as per the
    instructions, otherwise False. r and c are row and col number (from 1 to 3)
    '''
    board = [row.split('|') for row in board]
    winner = lambda x: x.count('X') == 2 and x.count(' ') == 1
    lines = ((0,0,0,1,0,2),(1,0,1,1,1,2),(2,0,2,1,2,2),  # rows
             (0,0,1,0,2,0),(0,1,1,1,2,1),(0,2,1,2,2,2),  # cols
             (0,0,1,1,2,2),(0,2,1,1,2,0)) # diags
​
    for line in lines:
        a,b,c,d,e,f = line
        seq = board[a][b]+board[c][d]+board[e][f]
        if winner(seq):
            for j in range(0,7,2):
                if board[line[j]][line[j+1]] == ' ':
                    return [line[j]+1, line[j+1]+1]
​
    return False

