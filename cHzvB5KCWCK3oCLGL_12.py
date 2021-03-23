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

import copy
def game_of_life(board):
    board_copy = copy.deepcopy(board)
    string = ''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i == 0:
                if j == 0:
                    total = sum(board[i][:j+2]) + sum(board[i+1][:j+2])
                elif j == len(board[0])-1:
                    total = sum(board[i][j-1:]) + sum(board[i+1][j-1:])
                else:
                    total = sum(board[i][j-1:j+2]) + sum(board[i+1][j-1:j+2])
            elif i == len(board)-1:
                if j == 0:
                    total = sum(board[i-1][:j+2]) + sum(board[i][:j+2])
                elif j == len(board[0])-1:
                    total = sum(board[i-1][j-1:]) + sum(board[i][j-1:])
                else:
                    total = sum(board[i-1][j-1:j+2]) + sum(board[i][j-1:j+2])
            elif j == 0 and i != 0 and i != len(board)-1:
                total = sum(board[i-1][:j+2]) + sum(board[i][:j+2]) + sum(board[i+1][:j+2])
            elif j == len(board[0])-1 and i != 0 and i != len(board)-1:
                total = sum(board[i-1][j-1:]) + sum(board[i][j-1:]) + sum(board[i+1][j-1:])
            else:
                total = sum(board[i-1][j-1:j+2]) + sum(board[i][j-1:j+2]) + sum(board[i+1][j-1:j+2])
​
            if board_copy[i][j] == 0:
                if total == 3:
                    board_copy[i][j] = 1
            else:
                if total == 1 or total == 2 or total > 4:
                    board_copy[i][j] = 0
​
            string += str(board_copy[i][j])
        string += '\n'
    string = string.replace('0', '_')
    string = string.replace('1', 'I')
    return string[:-1]

