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

def get_diagonals(pos):
  diag = []
  x = pos[0]
  y = pos[1]
  while x < 'h' and y < '8':
    x = chr(ord(x) + 1)
    y = str(int(y) + 1)
    diag.append(x + y)
  x = pos[0]
  y = pos[1]
  while x > 'a' and y > '1':
    x = chr(ord(x) - 1)
    y = str(int(y) - 1)
    diag.append(x + y)
  x = pos[0]
  y = pos[1]
  while x < 'h' and y > '1':
    x = chr(ord(x) + 1)
    y = str(int(y) - 1)
    diag.append(x + y)
  x = pos[0]
  y = pos[1]
  while x > 'a' and y < '8':
    x = chr(ord(x) - 1)
    y = str(int(y) + 1)
    diag.append(x + y)
  return diag
  
def bishop(start, end, n):
  if start == end:
    return True
  if n == 0:
    return False
  for pos in get_diagonals(start):
    if bishop(pos, end, n - 1):
      return True
  return False

