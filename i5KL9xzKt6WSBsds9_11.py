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
    l = 'ABCDEFGH'
    d = [abs(l.index(target[0]) - l.index(current[0])), abs(int(target[1]) - int(current[1]))]
    rule1 = (target[0] == current[0] and int(target[1]) - int(current[1]) in [1, 2])
    try:
        rule2 = (d[0] / d[1] == 1)
    except ZeroDivisionError:
        rule2 = False
    rule3 = ((d[0] == 2 and d[1] == 1) or (d[0] == 1 and d[1] == 2))
    rule4 = (target[0] == current[0] or target[1] == current[1])
    rule5 = (d[0] <= 1 and d[1] <= 1)
    if rule1 and piece == 'Pawn':
        return True
    if rule2 and piece == 'Bishop':
        return True
    if rule3 and piece == 'Knight':
        return True
    if rule4 and piece == 'Rook':
        return True
    if rule5 and piece == 'King':
        return True
    if (rule2 or rule4) and piece == 'Queen':
        return True
    return False

