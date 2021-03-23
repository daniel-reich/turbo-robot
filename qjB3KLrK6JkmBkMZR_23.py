"""


In chess, queens can move any number of squares horizontally, vertically or
diagonally.

Given the location of your queen and your opponents' queen, determine whether
or not you're able to capture your opponent's queen. Your location and your
opponents' location are the first and second elements of the list,
respectively.

### Examples

    can_capture(["A1", "H8"]) ➞ True
    # Your queen can move diagonally to capture opponents' piece.
    
    can_capture(["A1", "C2"]) ➞ False
    # Your queen cannot reach C2 from A1 (although a knight could).
    
    can_capture(["G3", "E5"]) ➞ True

### Notes

Assume there are no blocking pieces.

"""

def can_capture(queens):
    loc1, loc2 = queens
    r1 = ord(loc1[0])
    r2 = ord(loc2[0])
    c1 = int(loc1[1])
    c2 = int(loc2[1])
    if abs(r1 - r2) == abs(c1 - c2):
        return True
    return (r1 == r2) or (c1 == c2)

