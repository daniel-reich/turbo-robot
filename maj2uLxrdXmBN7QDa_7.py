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
    s_c, s_r = ord(start[0]) - 96, int(start[1])
    e_c, e_r = ord(end[0]) - 96, int(end[1])
    s_color, e_color = 0, 0
    if s_r % 2:
        if s_c % 2:
            s_color = 1
    else:
        if not s_c % 2:
            s_color = 1
    if e_r % 2:
        if e_c % 2:
            e_color = 1
    else:
        if not e_c % 2:
            e_color = 1
    if s_color == e_color:
        if n == 0:
            return False
        elif n == 1:
            if abs(s_r - e_r) == abs(s_c - e_c):
                return True
        else:
            return True
    return False

