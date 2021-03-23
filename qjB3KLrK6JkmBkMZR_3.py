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
  q1,q2 = map(list,queens)
  x1,y1 = list(q1)
  x2,y2 = list(q2)
  return abs(int(y1)-int(y2)) == abs(ord(x1)-ord(x2)) or \
    y1 == y2 or x1 == x2

