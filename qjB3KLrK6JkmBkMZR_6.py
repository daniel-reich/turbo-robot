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
  row = "ABCDEFGH"
  col = "12345678"
  diags = []  
  Q = [i.translate(i.maketrans(row,col)) for i in queens]
  a1,a2,b1,b2 =int(Q[0][0]),int(Q[0][1]),int(Q[1][0]),int(Q[1][1]),
  if a2==b2 or a1==b1:
    return True
  elif abs(a1-b1)==abs(a2-b2):
    return True 
  return False

