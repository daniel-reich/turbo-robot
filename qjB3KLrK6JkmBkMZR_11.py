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
  pos1 = queens[0]
  pos2 = queens[1]
  if pos1[0] == pos2[0]:
    return True
  elif pos1[1] == pos2[1]:
    return True
  else:
    if abs(ord(pos1[0])-ord(pos2[0])) == abs(int(pos1[1]) - int(pos2[1])):
      return True
    else:
      return False

