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

import string
​
def bishop(start, end, n):
    alphabet = string.ascii_lowercase
​
    int_s, int_e = int(start[1]), int(end[1])
    i_s, i_e = alphabet.find(start[0])+1, alphabet.find(end[0])+1
    t = i_s + i_e + int_s + int_e
​
    if (t % 2) == 0:
        if start == end:
            return True
​
        if abs(i_e-i_s) == abs(int_s-int_e):
            if n > 0:
                return True
            else:
                return False
​
        if n > 1:
            return True
​
    return False

