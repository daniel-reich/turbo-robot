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
    start = l2n(split(start))
    end = l2n(split(end))
    startPoints = diagonalley(start)
    endPoints = diagonalley(end)
    if start != end and n == 0:
        return False
    if n == 1 and start in endPoints:
        return True
    elif n == 1:
        return False
    for i in range(len(startPoints)):
        if startPoints[i] in endPoints:
            return True
    else:
        return False
​
​
​
​
​
def diagonalley(start):
    points = []
    for i in range(8):
        points.append([start[0] + i, start[1] + i])
        points.append([start[0] + i, start[1] - i])
        points.append([start[0] - i, start[1] + i])
        points.append([start[0] - i, start[1] - i])
    return points
​
​
def l2n(start):
    dick = ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5, "f", 6, "g", 7, "h", 8]
    for j in range(len(dick)):
        if dick[j] == start[0]:
            start[0] = dick[j + 1]
            start[1] = int(start[1])
            return start
​
def split(start):
    return [c for c in start]

