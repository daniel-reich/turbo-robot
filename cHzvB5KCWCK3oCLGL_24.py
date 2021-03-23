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
    next_board = [row[:] for row in board]
    for x in range(len(board)):
        for y in range(len(board[0])):
            next_board[x][y] = next_state(board,x,y)
    return displayer(next_board)
​
def displayer(board):
    s = ""
    for a in board:
        for b in a:
            if b == 1: s += "I"
            else: s += "_"
        s+="\n"
    return s[:-1]
​
def next_state(board,x,y):
    counter = 0
    if x>0:
        if board[x-1][y] == 1: counter +=1
        if y > 0 and board[x - 1][y - 1] == 1: counter += 1
        if y < len(board[0])-1 and board[x - 1][y + 1] == 1: counter += 1
    if y>0 and board[x][y-1] == 1: counter +=1
    if y < len(board[0])-1 and board[x][y + 1] == 1: counter += 1
    if x<len(board)-1: 
        if board[x + 1][y] == 1: counter += 1
        if y > 0 and board[x + 1][y - 1] == 1: counter += 1
        if y < len(board[0])-1 and board[x + 1][y + 1] == 1: counter += 1
    if board[x][y] == 1:
        if counter < 2: return 0
        elif counter >= 4: return 0
        else: return 1
    if board[x][y] == 0:
        if counter == 3: return 1
        return 0

