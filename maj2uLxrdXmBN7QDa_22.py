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

def is_diagonally_adjacent(start, end):
    board = [[j+str(i) for j in "abcdefgh"] for i in range(8, 0, -1)]
    center = [i for i in range(len(board)) if start in board[i]][0]
    center = [center, board[center].index(start)]
    spots = []
    for i, j in [[1, 1], [-1, 1], [1, -1], [-1, -1]]:
        x, y = center
        while len(board) > x >= 0 and len(board) > y >= 0:
            spots.append(board[x][y])
            x += i
            y += j
    return end in spots
    
def is_black(pos):
  letter, num = pos
  if ord(letter) % 2 == 0:
    return False if int(num) % 2 else True
  return True if int(num) % 2 else False
  
def bishop(start, end, n):
  if start == end:
    return True
  if is_black(start) == is_black(end):
    return n >= 1 if is_diagonally_adjacent(start, end) else n >= 2
  return False

