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

def game_of_life(board):
    output = [['_' for a in range(len(board[0]))] for b in range(len(board))]
    output_string = ''
    for i in range(len(board)):
        for j in range(len(board[i])):
            neighbors = 0
            for k in range(max(0, i - 1), min(len(board), i + 2)):
                for l in range(max(0, j - 1), min(len(board[k]), j + 2)):
                    if i == k and j == l:
                        continue
                    neighbors += board[k][l]
            if board[i][j] == 1:
                if neighbors in (2, 3):
                    output[i][j] = 'I'
            else:
                if neighbors == 3:
                    output[i][j] = 'I'
    return '\n'.join([output_string + ''.join(k) for k in output])

