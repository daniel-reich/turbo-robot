"""


The function is given a list of three strings representing a board. The
characters can be `"X", "O", " "`. The first player writes `"X"` at first
turn. If a player has three marks in a row, column or a diagonal, the game
stops. Given the board evaluate if this state can be achieved in line with the
rules, return `True / False`.

### Examples

    validate_tic_tac_toe(["X  ", "   ", "   "]) ➞ True
    # X goes first.
    
    validate_tic_tac_toe(["O  ", "   ", "   "]) ➞ False
    # O cannot go first.
    
    validate_tic_tac_toe(["X X", " O ", "   "]) ➞ True
    # Two X and one O is a possible state.
    
    validate_tic_tac_toe(["XOX", " X ", "   "]) ➞ False
    # Three X and one O is not a possible state.
    # Players have to go one after another.

### Notes

N/A

"""

def count_wins(board, player):
    win = player * 3
    cnt = 0
    for i in range(3):
        if board[i] == win:
            cnt += 1
        if board[0][i]+board[1][i]+board[2][i] == win:
            cnt += 1
    diag = [board[i][i] for i in range(3)]
    if diag == win:
        cnt += 1
    diag = [board[i][2-i] for i in range(3)]
    if diag == win:
        cnt += 1
    return cnt
​
def validate_tic_tac_toe(board):
    flat = board[0] + board[1] + board[2]
    cntO = flat.count('O')
    cntX = flat.count('X')
    if not cntX in [cntO, cntO+1]:
        return False    # number of marks not valid
    winsO = count_wins(board, 'O')
    winsX = count_wins(board, 'X')
    if winsO * winsX > 0:
        return False    # there can be only one winning player
    return True

