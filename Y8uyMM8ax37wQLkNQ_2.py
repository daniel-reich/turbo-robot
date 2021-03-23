"""


Write a function that accepts an integer `n` and returns an `n * n` spiral
matrix.

### Examples

    matrix(2) ➞ [
      [1, 2],
      [4, 3]
    ]
    
    matrix(3) ➞ [
      [1, 2, 3],
      [8, 9, 4],
      [7, 6, 5]
    ]
    
    matrix(4) ➞ [
      [1,  2,  3,  4],
      [12, 13, 14, 5],
      [11, 16, 15, 6],
      [10,  9,  8, 7]
    ]

### Notes

In the examples, traverse the matrix in the clock-wise direction to observe
the spiral pattern.

"""

# re-use solution from "Primes Spiral":
def matrix(n):
    primes = list(range(1, n**2 + 1))
    M = [[0 for row in range(n)] for col in range(n)]
    directions = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
    pos = 0
    row, col = 0, 0
    direction = 0
    while pos < n**2 - 1:
        M[row][col] = primes[pos]
        nxt_row, nxt_col = row + directions[direction][0], col + directions[direction][1]
        while nxt_row < 0 or nxt_row == n or nxt_col < 0 or nxt_col == n or \
              M[nxt_row][nxt_col] != 0:
            direction = (direction + 1) % 4
            nxt_row, nxt_col = row + directions[direction][0], col + directions[direction][1]
        row, col = nxt_row, nxt_col
        pos += 1
    M[row][col] = primes[-1]
    return M

