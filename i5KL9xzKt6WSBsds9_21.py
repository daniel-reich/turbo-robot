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
  destruct = lambda square: (ord(square[0]) - ord('A'), int(square[1])-1)
  x0, y0 = destruct(current)
  x1, y1 = destruct(target)
  dx, dy = x1 - x0, y1 - y0 
  if piece == "King":
    return (dx == 0 and abs(dy) == 1) or (dy == 0 and abs(dx) == 1) \
      or (abs(dx) == abs(dy) == 1)
  if piece == "Queen":
    return (dx == 0 and abs(dy) >= 1) or (dy == 0 and abs(dx) >= 1) \
      or (abs(dx) == abs(dy) >= 1)
  if piece == "Bishop":
    return (abs(dx) == abs(dy) >= 1)
  if piece == "Knight":
    return (abs(dx) == 2 and abs(dy) == 1) or (abs(dx) == 1 and abs(dy) == 2)
  if piece == "Rook":
    return (dx == 0 and abs(dy) >= 1) or (dy == 0 and abs(dx) >= 1)
  return dx == 0 and (dy == 1 or (y0 == 1 and dy == 2))

