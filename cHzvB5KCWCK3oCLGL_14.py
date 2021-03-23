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
    output = []
    for i, row in enumerate(board):
        for t, element in enumerate(row):
            neighbours = get_neighbours(t, i, board)
            output.append(get_output(element, neighbours))
        output.append('\n')
    return ''.join(output[:-1])
​
def get_neighbours(element_idx, row_idx, board):
    neighbours = []
    if row_idx > 0:
        neighbours.append(board[row_idx - 1][element_idx])
        if element_idx > 0:
            neighbours.append(board[row_idx - 1][element_idx - 1])
        if element_idx < len(board[row_idx]) - 1:
            neighbours.append(board[row_idx -1][element_idx + 1])
    if row_idx < len(board) - 1:
        neighbours.append(board[row_idx + 1][element_idx])
        if element_idx > 0:
            neighbours.append(board[row_idx + 1][element_idx - 1])
        if element_idx < len(board[row_idx]) - 1:
            neighbours.append(board[row_idx + 1][element_idx + 1])
​
    if element_idx > 0:
        neighbours.append(board[row_idx][element_idx - 1])
    if element_idx < len(board[row_idx]) - 1:
        neighbours.append(board[row_idx][element_idx + 1])
    return neighbours
​
​
def get_output(element, neighbours):
    ones = neighbours.count(1)
​
    if element:
        if ones in [2, 3]:
            return 'I'
        else:
            return '_'
​
    elif not element:
        if ones == 3:
            return 'I'
        else:
            return '_'

