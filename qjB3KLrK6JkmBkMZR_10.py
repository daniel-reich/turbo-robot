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
  l=[[ord(list(i)[0])-64,int(list(i)[1])] for i in queens]
  return abs(l[0][0]-l[1][0])==abs(l[0][1]-l[1][1]) or l[0][0]==l[1][0] or l[0][1]==l[1][1]

