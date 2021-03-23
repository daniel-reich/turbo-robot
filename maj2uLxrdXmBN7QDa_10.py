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
    board = [[(x+y)%2 for x in range(0, 8)] for y in range(0,8)]
    startCol = ord(start[0]) - 97
    startRow = (int(start[1])  + (8-int(start[1])) + (1-int(start[1])) )- 1
    endCol = ord(end[0]) - 97
    endRow = (int(end[1])  + (8-int(end[1])) + (1-int(end[1])) )- 1
    
    if start == end:
        return True
    elif n==0:
        return False
    elif board[startRow][startCol] != board[endRow][endCol]:
        return False
    elif n == 1:
        if abs(startCol - endCol) == abs(startRow - endRow):
            return True
        else:
            return False
    else:
        return True

