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
  c = (ord(current[0])-64)*10 + int(current[1])
  t = (ord(target[0])-64)*10 + int(target[1])
  
  if piece == "Pawn":
    return t-c == 1
  elif piece == "Knight":
    return abs(t-c) in [8,12,19,21]
  elif piece == 'Bishop':
    return not abs(t-c)%11 or not abs(t-c)%9
  elif piece == 'Rook':
    return t//10 == c//10 or t%10 == c%10
  elif piece == 'Queen':
    return not abs(t-c)%11 or not abs(t-c)%9 or t//10 == c//10 or t%10 == c%10
  return abs(t//10 - c//10)<2 and abs(t%10 - c%10)<2

