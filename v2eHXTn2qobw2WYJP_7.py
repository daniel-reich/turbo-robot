"""


Create a function that takes a list representation of a Minesweeper board, and
returns another board where the value of each cell is the amount of its
neighbouring mines.

### Examples

The input may look like this:

    [
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 1, 0, 1],
      [1, 1, 0, 0]
    ]

The `0` represents an **empty space** . The `1` represents a **mine**.

You will have to replace each **mine** with a `9` and each **empty space**
with the number of adjacent mines, the output will look like this:

    [
      [1, 9, 2, 1],
      [2, 3, 9, 2],
      [3, 9, 4, 9],
      [9, 9, 3, 1]
    ]

### Notes

  * Since in the output the numbers `0-8` are used to determine the amount of adjacent mines, the number `9` will be used to identify the mines instead.
  * A wikipedia page explaining how Minesweeper works is available in the **Resources** tab.

"""

def minesweeper_numbers(board):
​
  class Board:
    class Space:
      
      def __init__(self, bomb, r, c, mr, mc, val = 9):
        self.bomb = bomb
        self.row  = r
        self.col = c
        self.maxrow = mr-1
        self.maxcol = mc-1
        self.val = val
      
        nearby_rows = [self.row]
        nearby_cols = [self.col]
​
        if self.row != 0:
          nearby_rows.append(self.row - 1)
        if self.row != self.maxrow:
          nearby_rows.append(self.row + 1)
        
        if self.col != 0:
          nearby_cols.append(self.col - 1)
        if self.col != self.maxcol:
          nearby_cols.append(self.col + 1)
        
        self.nearby = []
​
        for row in nearby_rows:
          for col in nearby_cols:
            space = '{},{}'.format(row, col)
            if space != '{},{}'.format(self.row, self.col):
              self.nearby.append(space)
      
      def nearby_mines(self, spaces):
        if self.bomb == False:
          mine_count = 0
​
          for space in self.nearby:
            if spaces[space].bomb == True:
              mine_count += 1
        
          self.val = mine_count
        
        return True
    
    def __init__(self, rawboard):
      
      self.raw = rawboard
      self.spaces = {}
​
      for r in range(len(rawboard)):
        for c in range(len(rawboard[0])):
          space = '{},{}'.format(r, c)
          bomb = rawboard[r][c] == 1
​
          self.spaces[space] = Board.Space(bomb, r, c, len(rawboard), len(rawboard[0]))
​
    def update(self):
      for space in self.spaces.values():
        space.nearby_mines(self.spaces)
      return True
​
    def display(self):
      tr = []
​
      for r in range(len(self.raw)):
        row = []
        for c in range(len(self.raw[0])):
          row.append(self.spaces['{},{}'.format(r,c)].val)
        tr.append(row)
      
      return tr
​
  board = Board(board)
  board.update()
  return board.display()

