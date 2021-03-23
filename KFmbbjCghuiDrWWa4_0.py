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

wins = [{(0, 0), (0, 1), (0, 2)}, {(1, 0), (1, 1), (1, 2)},
        {(2, 0), (2, 1), (2, 2)}, {(0, 0), (1, 0), (2, 0)},
        {(0, 1), (1, 1), (2, 1)}, {(0, 2), (1, 2), (2, 2)},
        {(0, 0), (1, 1), (2, 2)}, {(2, 0), (1, 1), (0, 2)}]
def validate_tic_tac_toe(board):
    cross = set()
    nulls = set()
    for r, row in enumerate(board):
        for c, v in enumerate(row):
            if v == "X":
                cross.add((r, c))
            elif v == "O":
                nulls.add((r, c))
    n_cross = len(cross)
    n_nulls = len(nulls)
    cross_wins = sum(s <= cross for s in wins)
    nulls_wins = sum(s <= nulls for s in wins)
    return ((cross_wins in (1, 2) and nulls_wins == 0
             and n_cross == n_nulls + 1)
            or (nulls_wins in (1, 2) and cross_wins == 0
                and n_cross == n_nulls)
            or (cross_wins == 0 and nulls_wins == 0 and
                n_cross in (n_nulls, n_nulls + 1)))

