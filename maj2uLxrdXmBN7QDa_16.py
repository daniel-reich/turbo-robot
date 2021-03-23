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

def bishop(sta, end, n):
    if n == 0: return sta == end
    dx, dy = (abs(ord(a)-ord(b)) for a, b in zip(sta, end))
    if n == 1: return dx == dy
    return dx%2 == dy%2

