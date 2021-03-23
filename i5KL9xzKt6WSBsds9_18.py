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

def can_move(piece, pos1, pos2):
    # converts each character of pos1 and pos 2
    # to their int character codes
    pos1_R = ord(pos1[1])
    pos1_C = ord(pos1[0])
    pos2_R = ord(pos2[1])
    pos2_C = ord(pos2[0])
  
    colDif = abs(pos1_C - pos2_C)
    if (piece == "Pawn"):
        rowDif = pos2_R - pos1_R
        # if the pawn starts at row 2, it can either move 1
        # or 2 spaces forward within the same column
        # It does not use abs, because we want to make sure
        # the pawn moves forward. It cannot have a negative rowDif
        if (pos1[1] == '2'):
            return colDif == 0 and (rowDif == 1 or rowDif == 2)
        return colDif == 0 and rowDif == 1
​
    # for all other pieces rowDif can be the absolute value
    rowDif = abs(pos2_R - pos1_R)
    # A knight must either move 2 columns and 1 row or 1 row and 2 columns
    if (piece == "Knight"):
        return (colDif == 1 and rowDif == 2) or (colDif == 2 and rowDif == 1)
    # A bishop must move an equal number of rows and columns
    elif (piece == "Bishop"):
        return colDif == rowDif
    # A rook must move within the same column or row
    elif (piece == "Rook"):
        return (colDif == 0) or (rowDif == 0)
    # A queen must either move like a rook or like a bishop
    elif (piece == "Queen"):
        return (colDif == rowDif) or (colDif == 0 or rowDif == 0)
    # A king can move a maximum of 1 column and/or row at a time
    elif (piece == "King"):
        return (colDif == 1 or colDif == 0) and (rowDif == 1 or rowDif == 0)
    else:
        return False

