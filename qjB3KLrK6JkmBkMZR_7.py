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

def onDiagonal(queens):
  l = 'ABCDEFGH'
  n = '12345678'
  n_delt = '87654321'
  a, b = l.index(queens[0][0]), n.index(queens[0][1])
  a1, b1 = l.index(queens[1][0]), n.index(queens[1][1])
  c, d = l.index(queens[0][0]), n_delt.index(queens[0][1])
  c1, d1 = l.index(queens[1][0]), n_delt.index(queens[1][1])
  if (a1-a) == (b1-b):
    return True
  elif (c1-c) == (d1-d):
    return True
  else:
    return False
​
def can_capture(queens):
  if queens[0][0] == queens[1][0]:
    return True
  if queens[0][1] == queens[1][1]:
    return True
  if onDiagonal(queens):
    return True
  else:
    return False

