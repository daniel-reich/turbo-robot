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

def is_pawn_move(start, end):
    return start[0] == end[0] and ord(end[1]) - ord(start[1]) <= 2
​
def is_knight_move(start, end):
    return sorted([abs(ord(end[0]) - ord(start[0])), abs(ord(end[1]) - ord(start[1]))]) == [1, 2]
​
def is_bishop_move(start, end):
    return abs(ord(end[0]) - ord(start[0])) == abs(ord(end[1]) - ord(start[1]))
​
def is_rock_move(start, end):
    return min(abs(ord(end[0]) - ord(start[0])), abs(ord(end[1]) - ord(start[1]))) == 0
​
def is_queen_move(start, end):
    return is_bishop_move(start, end) or is_rock_move(start, end)
​
def is_king_move(start, end):
    return max(abs(ord(end[0]) - ord(start[0])), abs(ord(end[1]) - ord(start[1]))) == 1
​
def can_move(figure, start, end):
    figures = ["Pawn", "Knight", "Bishop", "Rook", "Queen", "King"]
    if figure == figures[0]:
        return is_pawn_move(start, end)
    elif figure == figures[1]:
        return is_knight_move(start, end)
    elif figure == figures[2]:
        return is_bishop_move(start, end)
    elif figure == figures[3]:
        return is_rock_move(start, end)
    elif figure == figures[4]:
        return is_queen_move(start, end)
    elif figure == figures[5]:
        return is_king_move(start, end)
    else:
        return "Wrong piece"

