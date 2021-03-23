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
    # put wall of 0's around board
    b = []
    top = [0]*(2+len(board[0]))
    b.append(top)
    for row in board:
        b.append([0] + row + [0])
    b.append(top)
​
    loa = []
    for r in range(1, 1+len(board)):
        a = ''
        for c in range(1, 1+len(board[0])):
            a += get_new(b, r, c)
        loa.append(a)
    return '\n'.join(loa)
​
def get_new(b, r, c):
    cnt = 0
    rr = r-1
    for cc in [c-1, c, c+1]:
        if b[rr][cc] == 1:
            cnt +=1
    rr = r+1
    for cc in [c-1, c, c+1]:
        if b[rr][cc] == 1:
            cnt +=1
    rr = r
    for cc in [c-1, c+1]:
        if b[rr][cc] == 1:
            cnt +=1
    if b[r][c] == 1:
        if cnt in (0, 1, 4, 5, 6, 7, 8):
            return '_'
        else:
            return 'I'
    if cnt == 3:
        return 'I'
    return '_'

