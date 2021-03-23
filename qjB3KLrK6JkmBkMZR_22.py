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
  letters = ["A","B","C","D","E","F","G","H"]
  nums = ["1","2","3","4","5","6","7","8"]
  
  diff_l = abs(letters.index(queens[0][0]) - letters.index(queens[1][0]))
  diff_n = abs(nums.index(queens[0][1]) - nums.index(queens[1][1]))
  if diff_l == 0 or diff_n == 0:
    return True
  return diff_l == diff_n

