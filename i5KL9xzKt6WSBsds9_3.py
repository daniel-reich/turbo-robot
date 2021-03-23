"""


Create a function that takes the name of a chess piece, its position and a
target position. The function should return `True` if the piece can move to
the target and `False` if it can't.

The possible inputs are "Pawn", "Knight", "Bishop", "Rook", "Queen" and
"King".

### Examples

    can_move("Rook", "A8", "H8") ➞ True
    
    can_move("Bishop", "A7", "G1") ➞ True
    
    can_move("Queen", "C4", "D6") ➞ False

### Notes

  * Do not include pawn capture moves and en passant.
  * Do not include castling.
  * Remember to include pawns' two-square move on the second rank!
  * Look for patterns in the movement of the pieces.

"""

def can_move(piece, current, target):
    alpha_num_dct = { 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    c_c = alpha_num_dct.get(current[0]) # current_column
    c_r = int(current[1]) # current_row
    t_r = int(target[1]) # target_column
    t_c = alpha_num_dct.get(target[0]) #target_row
​
    if piece == "Pawn":
        # pawn can move one row forward in the same column
        # Exception: If pawn is on row 2, it can move either one row forward ot two rows in same column
        if c_c == t_c:
            if (c_r == 2 and t_r in [3, 4])\
                or (t_r - c_r == 1):
                return True
        return False
​
    if piece == "Rook":
        # rook can move any number of rows/columns staying on the same column/row
        return c_c == t_c or c_r == t_r
​
    if piece == "Knight":
        # Knight can move 3 rows/columns and 1 column/row
        return abs(c_c - t_c) - abs(c_r - t_r) in [-1, 1]
​
    if piece == "Bishop":
        # Bishop can move same number of rows with same number of columns
        return abs(c_c - t_c) == abs(c_r - t_r)
​
    if piece == "Queen":
        # Queen can move like either rook or bishop
        return c_c == t_c or c_r == t_r or (abs(c_c - t_c) == abs(c_r - t_r))
​
    if piece == "King":
        # King can move one step
        return abs(c_c - t_c) in [1,0] and abs(t_r - c_r) in [1, 0]

