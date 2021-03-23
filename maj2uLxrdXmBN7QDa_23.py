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

def matrix_diagonal(matrix, start_point):
    result = []
    i = start_point[0]
    j = start_point[1]
    while i - 1 >= 0 and j + 1 <= len(matrix) - 1:
        result.append((i - 1, j + 1))
        i -= 1
        j += 1
    i = start_point[0]
    j = start_point[1]
    while i + 1 <= len(matrix) - 1 and j - 1 >= 0:
        result.append((i + 1, j - 1))
        i += 1
        j -= 1
    i = start_point[0]
    j = start_point[1]
    while i - 1 >= 0 and j - 1 >= 0:
        result.append((i - 1, j - 1))
        i -= 1
        j -= 1
    i = start_point[0]
    j = start_point[1]
    while i + 1 <= len(matrix) - 1 and j + 1 <= len(matrix) - 1:
        result.append((i + 1, j + 1))
        i += 1
        j += 1
    return result
​
​
def bishop_normal(start, end, n):
    matrix_bishop = []
    for _ in range(8):
        matrix_bishop.append([0 for _ in range(8)])
    if start == end and n >= 0:
        return True
    elif start == end and n < 0:
        return False
    elif start != end and n == 0:
        return False
    else:
        if (end[0], end[-1]) in matrix_diagonal(matrix_bishop, (start[0], start[-1])) and n >= 1:
            return True
        elif (end[0], end[-1]) in matrix_diagonal(matrix_bishop, (start[0], start[-1])) and n <= 0:
            return False
        elif (end[0], end[-1]) not in matrix_diagonal(matrix_bishop, (start[0], start[-1])) and n >= 1:
            for item in matrix_diagonal(matrix_bishop, (start[0], start[-1])):
               if bishop_normal(item, end, n-1):
                   return True
            return False
​
​
def bishop(start, end, n):
    dict_bishop = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    return bishop_normal((dict_bishop[start[0]], int(start[-1]) -1), (dict_bishop[end[0]], int(end[-1]) -1), n)

