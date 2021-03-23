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
    # Translation letters to numbers : a=>1, b=>2 , c=>3 ...
    case1 = start.translate(str.maketrans('abcdefgh', '12345678'))
    case2 = end.translate(str.maketrans('abcdefgh', '12345678'))
    # Check if the begin and the end are in the same color
    color = lambda position : "Black" if int(position[0])%2 == int(position[1])%2 else "White"
    if color(case1) != color(case2):
        return False
    if case1 == case2:
        return True
    if case2[0] != case1[0] :
        m = (int(case2[1]) - int(case1[1])) / (int(case2[0]) - int(case1[0]))
    else :
        m=0
    if n==1 and m in [ 1 , -1 ]:
        return True
    if n > 1:
        return True
    return False

