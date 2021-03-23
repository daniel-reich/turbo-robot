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

position_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
position_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
def can_move(piece, current, target):
    x, y, m, n = position_alphabet.index(
        current[0]), position_alphabet.index(target[0]), int(current[1]), int(target[1])
​
    def Rook(current, target):
        return True if current[0] == target[0] or current[1] == target[1] else False
​
    def Bishop():
        return True if abs(x - y) == abs(m - n) else False
​
    if piece == "Rook":
        return Rook(current, target)
​
    if piece == "Bishop":
        return Bishop()
​
    if piece == "Queen":
        return Bishop() or Rook(current, target)
​
    if piece == "Knight":
        return True if (abs(x - y) == 1 and abs(m - n) == 2) or (abs(m - n) == 1 and abs(x - y) == 2) else False
​
    if piece == "Pawn":
        return True if ((x == y) and ((n - m == 1) or (n - m == 2))) else False
​
    if piece == "King":
        return True if ((abs(x - y) == 1 or abs(x - y) == 0) and (abs(m - n) == 1 or abs(m - n) == 0)) else False

