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
  a1,a2 = trans(start)
  b1,b2 = trans(end)
  if (a1+a2+b1+b2)%2:
    return False
  if n==0:
    return (a1,a2) == (b1,b2)
  if n==1:
    return abs(a1-b1) == abs(a2-b2)
  return True
​
def trans(coor):
  return ('abcdefghijk'.index(coor[0]),'12345678'.index(coor[1]))

