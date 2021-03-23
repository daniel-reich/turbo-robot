"""


Create a function that takes **a character from a to h** as the column number
and **an integer from 1 to 8** as the row number which together represent the
location of a queen on a normal-sized chess board. Return this two dimensional
8x8 list.

This list must consist of zeroes and ones. The ones are placed in positions
where the queen can move in one move and zeroes represent positions on the
board where it cannot.

### Examples

    check_board("a", 1) ➞ [
      [1, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 1, 0],
      [1, 0, 0, 0, 0, 1, 0, 0],
      [1, 0, 0, 0, 1, 0, 0, 0],
      [1, 0, 0, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 0],
      [1, 1, 0, 0, 0, 0, 0, 0],
      [0, 1, 1, 1, 1, 1, 1, 1]
    ]
    
    check_board("h", 4) ➞ [
      [0, 0, 0, 1, 0, 0, 0, 1],
      [0, 0, 0, 0, 1, 0, 0, 1],
      [0, 0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 0],
      [0, 0, 0, 0, 0, 0, 1, 1],
      [0, 0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 1, 0, 0, 1]
    ]
     
    check_board("c", 8) ➞ [
      [1, 1, 0, 1, 1, 1, 1, 1],
      [0, 1, 1, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 0, 1, 0],
      [0, 0, 1, 0, 0, 0, 0, 1],
      [0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0]
    ]

### Notes

The queens' current position is a zero as it is impossible to move to this
position during one turn, because the queen is already there.

"""

def check_board(col, row):
  class Board:
​
    def __init__(self, a = [], b = [], c = [], d = [], e = [], f = [], g = [], h= []):
      self.a = a
      self.b = b
      self.c = c
      self.d = d
      self.e = e
      self.f = f
      self.g = g
      self.h = h
​
    def update(self, moves):
​
      a = self.a
      b = self.b
      c = self.c 
      d = self.d
      e = self.e
      f = self.f
      g = self.g
      h = self.h
​
      for n in range(0, 8):
        a.append(0)
        b.append(0)
        c.append(0)
        d.append(0)
        e.append(0)
        f.append(0)
        g.append(0)
        h.append(0)
​
      for move in moves:
        col = eval(move[0])
        row = int(move[1]) - 1
​
        col[row] = 1
      
      self.a = a
      self.b = b
      self.c = c
      self.d = d
      self.e = e
      self.f = f
      self.g = g
      self.h = h
      return True
    
    def show(self):
​
      cols = [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h]
​
      board = []
​
      for n in range(1, 9):
        row = []
        index = n - 1
​
        for col in cols:
          row.append(col[index])
        
        board.append(row)
​
      return list(reversed(board))
​
​
  class Queen:
​
    def __init__(self, col, row):
      self.c = col
      self.r = row
    
    def poss_moves(self):
      def row_cols(c, r):
        cols = 'a b c d e f g h'.split()
        rows = list(range(1, 9))
​
        pms = []
        cp = [self.c, self.r]
​
        for n in range(0, len(cols)):
          m1 = [cols[n], r]
          m2 = [c, rows[n]]
​
          if m1 != cp:
            pms.append(m1)
          if m2 != cp:
            pms.append(m2)
        
        return pms
      def diag(c, r):
​
        cols = 'a b c d e f g h'.split()
        rows = [1, 2, 3, 4, 5, 6, 7, 8]
​
        pms = []
        cp = [c, r]
​
        for n in range(0, len(cols)):
          i = cols[n]
          if i == self.c:
            cn = n
            break
       
        for n in range(0, cn):
          col = cols[n]
          d = cn - n
​
          if r - d > 0:
            pms.append([col, r - d])
          if r + d <= 8:
            pms.append([col, r + d])
        
        for n in range(cn + 1, 8):
          
          col = cols[n]
          
            
          d = n - cn
​
          if r - d > 0:
            pms.append([col, r - d])
          if r + d <= 8:
            pms.append([col, r + d])
       
        return pms
​
      rc = row_cols(self.c, self.r)
      d = diag(self.c, self.r)
​
      tr = rc
​
      for item in d:
        tr.append(item)
      
      del rc
      del d
​
      return tr
  
  q = Queen(col, row)
​
  pm = q.poss_moves()
​
  board = Board()
​
  b = board.update(pm)
​
  b = board.show()
​
  return b

