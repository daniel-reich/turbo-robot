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
    ans=''
    v=len(board)
    h=len(board[0])
    d=((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))
    for y in range(v):
        for x in range(h):
            k=0
            for p in range(8):
                xn=x+d[p][0];yn=y+d[p][1]
                if h>xn>-1 and v>yn>-1:
                    if board[yn][xn]==1:
                        k+=1
            if board[y][x]==1:
                if k<2 or k>3:
                    ans+='_'
                else:
                    ans+='I'
            else:
                if k==3:
                    ans+='I'
                else:
                    ans+='_'
        if y<v-1:
            ans+='\n'
    return ans

