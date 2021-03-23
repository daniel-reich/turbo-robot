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
  fc,ft,rc,rt = ord(current[0])-64,ord(target[0])-64,int(current[1]),int(target[1])
  if piece == 'Pawn':
    return ft == fc and (rt-rc == 1 or (rt == 4 and rc == 2))
  elif piece == 'Knight':
    return ((rt == rc+1 or rt == rc-1) and (ft == fc+2 or ft == fc-2)) or ((rt == rc+2 or rt == rc-2) and (ft == fc+1 or ft == fc-1))
  elif piece == 'Bishop':
    return (rt-rc == ft-fc) or (fc+ft == rc+rt)
  elif piece == 'Rook':
    return rt == rc or ft == fc
  elif piece == 'King':
    return fc-1 <= ft <= fc+1 and rc-1 <= rt <= rc+1
  else:
    return can_move('Bishop',current,target) or can_move('Rook',current,target)

