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
    x = (ord(target[0]) - 64) - (ord(current[0]) - 64)
    y = int(target[1]) - int(current[1])
​
    if piece == 'Pawn':
        return (x, y) == (0, 1)
    if piece == 'Knight':
        return sorted((x, y)) in ([-2, -1], [-2, 1], [-1, 2], [1, 2])
    if piece == 'Bishop':
        return abs(x) == abs(y)
    if piece == 'Rook':
        return x == 0 or y == 0
    if piece == 'Queen':
        return abs(x) == abs(y) or (x == 0 or y == 0)
    if piece == 'King':
        return sorted((abs(x), abs(y))) in ([0, 1], [1, 1])

