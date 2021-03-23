"""


Your chess teacher wants to know if a bishop can reach a certain spot on the
board in the given amount of moves.

Given a starting square `start`, ending square `end` and the maximum number of
moves allowed `n`. Return `True` if the ending square can be reached from the
starting square within the given amount of moves. Keep in mind the chessboard
goes from a1 to h8 (8x8).

### Examples

    bishop("a1", "b4", 2) ➞ True
    
    bishop("a1", "b5", 5) ➞ False
    
    bishop("f1", "f1", 0) ➞ True

### Notes

  * Chessboard is always empty (only the bishop is there).
  * Bishop can move in any direction diagonally.
  * If the starting and ending square are the same, return `True` (even if the move is 0).
  * Square names will always be lowercase and valid.

"""

def bishop(start, end, n):
  if start == end and n>=0:
    return True
  elif start != end and n==0:
    return False
​
  def get_possible_move(point):
​
    start_x = point[0]
    start_y = point[1]
​
    top_right = [chr(ord(start_x) + i) + str(int(start_y) + i) for i in range(1,9) if ord(start_x) + i < 105 and int(start_y) + i < 9]
    down_left = [chr(ord(start_x) - i) + str(int(start_y) - i) for i in range(1,9) if ord(start_x) - i > 96 and int(start_y) - i > 0]
​
    top_left = [chr(ord(start_x) - i) + str(int(start_y) + i) for i in range(1,9) if ord(start_x) - i > 96 and int(start_y) + i < 9]
    down_right = [chr(ord(start_x) + i) + str(int(start_y) - i) for i in range(1, 9) if ord(start_x) - i < 105 and int(start_y) - i > 0]
​
    return top_left + top_right +down_left + down_right
​
  poss_for_start = get_possible_move(start)
  poss_for_end = get_possible_move(end)
​
  if start in poss_for_end or end in poss_for_start and n>0:
    return True
  for i in poss_for_start:
    if i in poss_for_end and n>1:
      return True
  return False

