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
  Row = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
  Q1R = queens[0][0]
  Q1C = queens[0][1]
  Q2R = queens[1][0]
  Q2C = queens[1][1]
  if Row[Q1R] == Row[Q2R] or int(Q1C) == int(Q2C):
    return True
  else:
    if abs(Row[Q1R]-Row[Q2R]) == abs(int(Q1C)-int(Q2C)):
      return True
    else:
      return False

