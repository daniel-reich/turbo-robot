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
  frstpos="ABCDEFGH"
  if queens[0][0]==queens[1][0] or queens[0][1]==queens[1][1]:
    return True
  elif queens[1][0] in frstpos and queens[1][1]==str(frstpos.index(queens[1][0])-frstpos.index(queens[0][0])+int(queens[0][1])):
      return True
  elif queens[1][0] in frstpos and queens[1][1]==str(frstpos.index(queens[0][0])-frstpos.index(queens[1][0])+int(queens[0][1])):
      return True
  return False

