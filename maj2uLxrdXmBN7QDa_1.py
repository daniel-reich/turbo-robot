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

deltas = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
​
def get_row_col(sq):
    return (ord(sq[0]) - 97, int(sq[1]) - 1)
​
def bishop(start, end, n):
    if start == end:
        return True
    if n == 0:
        return False
    start = get_row_col(start)
    end = get_row_col(end)
    dist = {start: 0}
    queue = [start]
    while len(queue) > 0:
        (row, col) = queue.pop(0)
        for drow, dcol in deltas:
            row2, col2 = row + drow, col + dcol
            while 0 <= row2 <= 7 and 0 <= col2 <= 7:
                if (row2, col2) not in dist:
                    dist[(row2, col2)] = dist[(row, col)] + 1
                    queue.append((row2, col2))
                    if (row2, col2) == end:
                        return dist[(row2, col2)] <= n
                row2, col2 = row2 + drow, col2 + dcol
    return False

