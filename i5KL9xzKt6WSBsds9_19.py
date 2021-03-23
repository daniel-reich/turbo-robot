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
    h_diff = ord(target[0]) - ord(current[0])
    v_diff = int(target[1]) - int(current[1])
    if piece == 'Pawn':
        return h_diff == 0 and (v_diff == 1
                                or (current[1] == '2' and v_diff == 2))
    elif piece == 'Knight':
        return ((abs(h_diff) == 2 and abs(v_diff) == 1)
                or (abs(h_diff) == 1 and abs(v_diff) == 2))
    elif piece == 'Bishop':
        return abs(h_diff) == abs(v_diff)
    elif piece == 'Rook':
        return h_diff == 0 or v_diff == 0
    elif piece == 'Queen':
        return h_diff == 0 or v_diff == 0 or (abs(h_diff) == abs(v_diff))
    elif piece == 'King':
        return ((h_diff == 0 and abs(v_diff) == 1)
                or (v_diff == 0 and abs(h_diff) == 1)
                or abs(h_diff) == abs(v_diff) == 1)

