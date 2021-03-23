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
  ans=""
  neigh=neighbours(board)
  for y in range(len(board)):
    for x in range(len(board[0])):
      if board[y][x]==0:
        if neigh[y][x]==3:
          ans+="I"
        else:
          ans+="_"
      else:
        if neigh[y][x]<=1 or neigh[y][x]>=4:
          ans+="_"
        elif neigh[y][x]==2 or neigh[y][x]==3:
          ans+="I"
    ans+="\n"
  return ans[:-1]
​
​
def neighbours(board):
  empty=[[0 for i in range(len(board[0]))] for i in range(len(board))]
  for x in range(len(board[0])):
    for y in range(len(board)):
      if board[y][x]==1:
        for coord in [[y,x-1],[y,x+1],[y-1,x],[y+1,x],[y-1,x-1],[y+1,x+1],[y-1,x+1],[y+1,x-1]]:
          if len(board)-1>=coord[0]>=0 and len(board[0])-1>=coord[1]>=0:
            empty[int(coord[0])][int(coord[1])]+=1
  return empty

