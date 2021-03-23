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
  a = 'ABCDEFGH'
  cc, tc = current[0], target[0]
  cr, tr = int(current[1]), int(target[1])
  if piece == 'Rook':
    return rook(cc, tc, cr, tr)
  elif piece == 'Pawn':
    return current[0] == target[0] and ((cr == 2 and 3 <= tr and tr <= 4) or tr - cr == 1)
  elif piece == 'Knight':
    if abs(cr - tr) == 1:
      return abs(a.index(cc) - a.index(tc)) == 2 
    return abs(a.index(cc) - a.index(tc)) == 1 and abs(cr - tr) == 2
  elif piece == 'Bishop':
    return bishop(cc, tc, cr, tr, a)
  elif piece == 'Queen':
    return rook(cc, tc, cr, tr) or bishop(cc, tc, cr, tr, a)
  else: 
    return abs(cr-tr) <= 1 and abs(a.index(cc) - a.index(tc)) <= 1
    
def rook(cc, tc, cr, tr):
  return cc == tc or cr == tr
​
def bishop(cc, tc, cr, tr, a):
  return abs(cr - tr) == abs(a.index(cc) - a.index(tc))

