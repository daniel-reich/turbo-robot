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

def can_move(piece, start, end):
    '''
    Returns True if the (white??) chess piece's move from start to end is legal,
    otherwise False
    '''
​
    pawn = lambda s, e: s[0] == e[0] and (e[1] in (3,4) if s[1] == 2 else \
           e[1] == s[1] + 1)
    bishop = lambda s, e: abs(ord(s[0]) - ord(e[0])) == abs(s[1] - e[1])
    rook = lambda s, e: s[0] == e[0] or s[1] == e[1]
    queen = lambda s, e: bishop(s, e) or rook(s, e)
    king = lambda s, e: abs(ord(s[0]) - ord(e[0])) <= 1 and abs(s[1] - e[1]) <= 1
    knight = lambda s, e: abs(ord(s[0]) - ord(e[0])) == 2 and abs(s[1] - e[1]) == 1\
             or abs(ord(s[0]) - ord(e[0])) == 1 and abs(s[1] - e[1]) == 2
​
    return eval(piece.lower())((start[0],int(start[1])),(end[0],int(end[1])))

