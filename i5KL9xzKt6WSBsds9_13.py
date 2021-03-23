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
    pawn1 = current[0] == target[0] and int(target[1]) == int(current[1]) + 1
    pawn2 = current[0] == target[0] == 'G' and int(target[1]) == int(current[1]) + 2
    knight1 = abs(int(target[1]) - int(current[1])) == 2 and abs(ord(target[0]) - ord(current[0])) == 1
    knight2 = abs(int(target[1]) - int(current[1])) == 1 and abs(ord(target[0]) - ord(current[0])) == 2
    rook = current[0] == target[0] or int(target[1]) == int(current[1])
    bishop = ord(target[0]) == ord(current[0]) + abs(int(target[1]) - int(current[1]))
    king = abs(int(target[1]) - int(current[1])) <= 1 and abs(ord(target[0]) - ord(current[0])) <= 1
   
    if piece == "Pawn":
        return pawn1 or pawn2
    if piece == "Knight":
        return knight1 or knight2
    elif piece == "Rook":
        return rook
    elif piece == "Bishop":
        return bishop
    elif piece == "King":
        return king
    elif piece == "Queen":
        return rook or bishop

