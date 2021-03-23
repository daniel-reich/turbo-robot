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
    if start == end:
        return True
    if n == 0:
        return False
    d = {"a": 1, "b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
    if n > 1:
        return (d[start[0]]+int(start[1])+d[end[0]]+int(end[1]))%2 == 0
    if n == 1:
        return d[start[0]]+int(start[1])==d[end[0]]+int(end[1]) or d[start[0]]+8-int(start[1])==d[end[0]]+8-int(end[1])

