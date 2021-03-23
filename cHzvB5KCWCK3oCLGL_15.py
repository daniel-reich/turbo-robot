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

def neighbours(arr, x, y):
    empty = populated = 0
    # locations outside the bounds of the array are dicarded by the filter operation
    for r,c in filter(lambda t: 0<=t[0]<len(arr) and 0<=t[1]<len(arr[0]), [(a,b) for a, b in [(x-1, y-1), (x, y-1), (x+1,y-1), (x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]]):
        if arr[r][c] == 0:
            empty += 1
        elif arr[r][c] == 1:
            populated += 1
    return (empty, populated)        
​
def game_of_life(board):
    nextgen = [['_' for _ in range(len(board[0]))] for _ in range(len(board))]
    for row in range(len(board)):
        for col in range(len(board[0])):
            e, p = neighbours(board, row, col)
            if (board[row][col] == 0 and p == 3) or (board[row][col] == 1 and 2 <= p <= 3):
                nextgen[row][col] = 'I'
    res = '\n'.join([''.join(row) for row in nextgen])
    return res

