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
  pos = lambda p: (ord(p[0]) - ord('a'), int(p[1]) - 1)
  r1, c1 = pos(start)
  r2, c2 = pos(end)
  if (r1 + c1) % 2 != (r2 + c2) % 2:
    return False
  elif n == 0:
    return start == end
  elif n == 1:
    return abs(r1 - r2) == abs(c1 - c2)
  else:
    return True

