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
    rook = {pos for dist in range(-8,9)
                for pos in [(0, dist), (dist, 0)]}
    bishop = {pos for dist in range(-8,9)
                for pos in [(dist, dist), (dist, -dist)]}
    moves = {'Pawn': {(0,1)},
             'King': {(col, row) for col in [-1,0,1] for row in [-1,0,1]},
             'Knight': {(col,  row) for row in [-2,-1,1,2]
                        for col in [-2,-1,1,2] if abs(col)!=abs(row)},
             'Bishop': bishop, 'Rook': rook, 'Queen': bishop | rook}
    
    (c1,r1),(c2,r2) = current,target
    move = ord(c2)-ord(c1), ord(r2)-ord(r1) 
    return move in moves[piece]

