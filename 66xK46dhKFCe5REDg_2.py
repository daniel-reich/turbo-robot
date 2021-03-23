"""


Given a list containing three strings, representing the rows of an O's and X's
board from top to bottom, return the row and column position of the winning
move for X's. Return `False` if the game cannot be won.

### Examples

    x_and_o(board = [" | | ", " |X| ", "X| | "]) ➞  [1, 3]
    
    # Board becomes:
    #    |   |
    #    |X |
    # X |   |
    
    x_and_o(board = ["X|X|O", "O|X| ", "X|O| "]) ➞ [3, 3]
    
    # Board becomes:
    # X|X|O
    # O|X|
    # X|O|

### Notes

There is no 0 index for the row or column.

"""

def x_and_o(board):
  class Row:
​
    def __init__(self, row):
      self.r = row
​
      if 'X' and 'O' in row:
        self.w = False
      elif 'X' in row:
        self.w = 'X'
      elif 'O' in row:
        self.w = 'O'
      else:
        self.w = False
      
    def extract(self, index):
      return self.r[index]
    
    def winnable(self, player):
      if self.r.count(player) == 2 and self.r.count(' ') == 1:
        return True
      else:
        return False
  class Col:
​
    def __init__(self, col):
      self.c = col
      
      if 'X' and 'O' in col:
        self.w = False
      elif 'X' in col:
        self.w = 'X'
      elif 'O' in col:
        self.w = 'O'
      else:
        self.w = False
      
    def extract(self, index):
      return self.c[index]
    
    def winnable(self, player):
      if self.c.count(player) == 2 and self.c.count(' ') == 1:
        return True
      else:
        return False   
  class Board:
  
    def __init__(self, board):
      self.b = board
      self.rows = {}
      self.cols = {}
​
      for n in range(len(board)):
        self.rows[n+1] = Row(board[n])
​
      for n in range(len(board[0])):
        col = []
        for row in board:
          col.append(row[n])
        self.cols[n+1] = Col(col)
​
      self.d1 = [self.rows[1].extract(0), self.rows[2].extract(1), self.rows[3].extract(2)] 
      self.d2 = [self.rows[1].extract(2), self.rows[2].extract(1), self.rows[3].extract(0)]
​
    def winning_move(self, player):
​
      for row in self.rows.keys():
        R = self.rows[row]
        if R.winnable(player) == True:
          winning_row = row
          wr = R.r
          for n in range(len(wr)):
            item = wr[n]
            if item == ' ':
              winning_col = n+1
              break
          return [winning_row, winning_col]
      
      for col in self.cols.keys():
        C = self.cols[col]
        if C.winnable(player) == True:
          winning_col = col
          wc = C.c
          for n in range(len(wc)):
            item = wc[n]
            if item == ' ':
              winning_row = n+1
              break
          return [winning_row, winning_col]
      
      if self.d1.count(player) == 2 and self.d1.count(' ') == 1:
        for n in range(3):
          if self.d1[n] == ' ':
            d1index = n
            break
        
        if d1index == 0:
          return [1, 1]
        elif d1index == 1:
          return [2, 2]
        else:
          return [3, 3]
      
      elif self.d2.count(player) == 2 and self.d2.count(' ') == 1:
        for n in range(3):
          if self.d2[n] == ' ':
            d2index = n
        
        if d2index == 0:
          return [1, 3]
        elif d2index == 1:
          return [2, 2]
        else:
          return [3, 1]
      
      else:
        return False
  
  
  nb = []
​
  for row in board:
    nb.append(row.split('|'))
  
  board = nb
  del nb
​
  b = Board(board)
​
  return b.winning_move('X')

