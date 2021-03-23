"""


![Conway's Game of Life](https://s3.amazonaws.com/edabit-images/game-of-
life.gif)

The goal of this challenge is to implement the logic used in Conway's Game of
Life. Wikipedia will give a better understanding of what it is and how it
works (check the resources tab above).

### Rules

  *  **For a space that's "populated":**
    * Each cell with 0 or 1 neighbours dies, as if by solitude.
    * Each cell with 2 or 3 neighbours survives.
    * Each cell with 4 or more neighbours dies, as if by overpopulation.
  *  **For a space that's "empty" or "unpopulated":**
    * Each cell with 3 neighbours becomes populated.

### Parameters

`board`: a 2-dimensional list of values 0 to 1.

  * 0 means that the cell is empty.
  * 1 means the cell is populated.

### Return Value

A `string` containing the board's state after the game logic has been applied
once.

    On character: I
    Off character: _

### Notes

  * The string should be divided by newlines `\n` to signal the end of each row.
  * A cell's "neighbours" are the eight cells that are vertically, horizontally and diagonally adjacent to it.

"""

import numpy as np
​
​
def game_of_life(board):
    def convolution(matrix, kernel):  # padded w/ 0 to handle edge cases
        matrixWithBorder = np.pad(matrix, ([1, 1], [1, 1]), mode="constant")
        rows, cols = matrix.shape
        matrixNew = np.zeros(matrix.shape)
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                slice = matrixWithBorder[(i - 1):(i + 2), (j - 1):(j + 2)]
                matrixNew[i - 1, j - 1] = np.sum(kernel * slice).astype(int)
        return matrixNew
​
    board = np.array(board)
    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]])
    neighbors = convolution(board, kernel)
    rows, cols = board.shape
    for i in range(rows):
        for j in range(cols):
            if board[i, j]:
                board[i, j] = 1 if 2 <= neighbors[i, j] <= 3 else 0
            else:
                board[i, j] = 1 if neighbors[i, j] == 3 else 0
​
    return str(board).translate(str.maketrans("01", "_I", " []"))

