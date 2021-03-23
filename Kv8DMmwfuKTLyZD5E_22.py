"""


Create a function which creates a square dartboard of side length `n`. The
value of a number should increase, the closer it is to the centre of the
board.

### Examples

    make_dartboard(3) ➞ [
      111,
      121,
      111
    ]
    
    make_dartboard(8) ➞ [
      11111111,
      12222221,
      12333321,
      12344321,
      12344321,
      12333321,
      12222221,
      11111111
    ]
    
    make_dartboard(5) ➞ [
      11111,
      12221,
      12321,
      12221,
      11111
    ]

### Notes

If the size given is an even number, the centre should be made up of the 4
highest values.

"""

def make_dartboard(n):
    board = [[1 for _ in range(n)] for __ in range(n)]
    if n % 2 == 1:
        max_val = n // 2 + 1
        board[n // 2][n // 2] = max_val
        val = max_val - 1
        while val > 1:
            for row in [n // 2 - (max_val - val), n // 2 + (max_val - val)]:
                for col in range(n // 2 - (max_val - val), n // 2 + (max_val - val) + 1):
                    board[row][col] = val
            for col in [n // 2 - (max_val - val), n // 2 + (max_val - val)]:
                for row in range(n // 2 - (max_val - val), n // 2 + (max_val - val) + 1):
                    board[row][col] = val
            val -= 1    
    else:
        max_val = n // 2
        board[n // 2][n // 2] = max_val
        board[n // 2 - 1][n // 2] = max_val
        board[n // 2 - 1][n // 2 - 1] = max_val
        board[n // 2][n // 2 - 1] = max_val
        val = max_val - 1
        while val > 1:
            for row in [n // 2 - 1 - (max_val - val), n // 2 + (max_val - val)]:
                for col in range(n // 2 - 1 - (max_val - val), n // 2 + (max_val - val) + 1):
                    board[row][col] = val
            for col in [n // 2 - 1 - (max_val - val), n // 2 + (max_val - val)]:
                for row in range(n // 2 - 1 - (max_val - val), n // 2 + (max_val - val) + 1):
                    board[row][col] = val
            val -= 1    
    for i in range(n):
        board[i] = int(''.join(map(str, board[i])))
    return board

