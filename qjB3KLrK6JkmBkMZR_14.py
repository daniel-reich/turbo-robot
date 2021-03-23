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
  print(queens)
  map = { 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
  print(map.get(queens[0][0]))
  print(map.get(queens[1][0]))
  diff_column = abs(map.get(queens[0][0]) -  map.get(queens[1][0]))
  diff_row = abs(int(queens[0][1]) - int(queens[1][1]))
  
  if queens[0][0] == queens[1][0]:
    # same colums
    return True
  elif queens[0][1] == queens[1][1]:
    # same row
    return True
  elif diff_column == diff_row:
    print(diff_column)
    print(diff_row)
    return True
  else:
    return False

