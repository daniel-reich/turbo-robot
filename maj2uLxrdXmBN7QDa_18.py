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
    n_start = (ord(start[0]) - 96, int(start[1]))
    n_end = (ord(end[0]) - 96, int(end[1]))
    if n == 0:
        return True if start == end else False
    if n >= 2:
        return True if abs(n_start[0] - n_start[1]) % 2 == abs(n_end[0] - n_end[1]) % 2 else False
    if n == 1:
        return True if abs(n_start[0] - n_end[0]) == abs(n_start[1] - n_end[1]) else False

