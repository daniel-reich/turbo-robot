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
  ranks = "ABCDEFGH"
  rankdiff = abs(ranks.index(target[0]) - ranks.index(current[0]))
  filediff = abs(int(target[1]) - int(current[1]))
  if piece == "Pawn":
    if current[1] == "2":
      return 1 <= filediff <= 2 and rankdiff == 0
    else:
      return filediff == 1 and rankdiff == 0
  if piece == "Knight":
    return (rankdiff == 2 and filediff == 1) or (rankdiff == 1 and filediff == 2)
  if piece == "Bishop":
    return rankdiff == filediff
  if piece == "Rook":
    return rankdiff == 0 or filediff == 0
  if piece == "Queen":
    return rankdiff == filediff or (rankdiff == 0 or filediff == 0)
  if piece == "King":
    return rankdiff < 2 and filediff < 2

