"""


Create a function that takes the name of a chess piece, its position and a
target position. The function should return `True` if the piece can move to
the target and `False` if it can't.

The possible inputs are "Pawn", "Knight", "Bishop", "Rook", "Queen" and
"King".

### Examples

    can_move("Rook", "A8", "H8") ➞ True
    
    can_move("Bishop", "A7", "G1") ➞ True
    
    can_move("Queen", "C4", "D6") ➞ False

### Notes

  * Do not include pawn capture moves and en passant.
  * Do not include castling.
  * Remember to include pawns' two-square move on the second rank!
  * Look for patterns in the movement of the pieces.

"""

def can_move(piece, current, target):
  class Pawn: #By making each piece their own class, I can write different code for each unique piece
​
    def __init__(self, cr, cc):
      self.r = cr
      self.c = cc
​
    def moves(self):
​
      r = self.r
      cols = range(1, 9)
      c = self.c
​
      if c == 2:
        poss_moves = '{r}4 {r}3 {r}1'.format(r = r).split()
      elif c == 7:
        poss_moves = '{r}6 {r}5 {r}8'.format(r = r).split()
      else:
        
        if c - 1 > 0 and c + 1 <= 8:
          poss_moves = '{r}{c1} {r}{c2}'.format(r = r, c1 = c - 1, c2 = c + 1)
        elif c + 1 > 8:
          poss_moves = '{r}{c1}'.format(r = r, c1 = c - 1)
        else:
          poss_moves = '{r}{c2}'.format(r = r, c2 = c + 1)
      
      return poss_moves
  class Rook:
​
    def __init__(self, r, c):
      self.r = r
      self.c = c
    
    def moves(self):
​
      pms = []
      rows = 'a b c d e f g h'.upper().split()
      for n in range(1, 9):
        pms.append('{r}{n}'.format(r = self.r, n = n))
        r = rows[n - 1]
        pms.append('{r}{c}'.format(r = r, c = self.c))
      
      return pms
  class Bishop:
​
    def __init__(self, r, c):
      self.r = r
      self.c = c
​
    def moves(self):
​
      r = self.r
      b = self.c
​
      rows = 'a b c d e f g h'.upper().split()
​
      for n in range(0, len(rows)):
        row = rows[n]
​
        if row == r:
          a = n
      below_rows = range(0, a)
      above_rows = range(a, 9)
     
      below_cols = range(1, b)
      above_cols = range(b, 9)
​
      moves = []
​
      below_moves = []
      above_moves = []
      for number in range(1, 9):
        if a - number in below_rows:
          if b - number in below_cols:
            below_moves.append([a - number, b - number])
          if b + number in above_cols:
            below_moves.append([a - number, b + number])
        if a + number in above_rows:
          if b + number in above_cols:
            above_moves.append([a + number, b + number])
          if b - number in below_cols:
            above_moves.append([a + number, b - number])
      
      for move in below_moves:
        
        row = rows[int(move[0])]
        col = int(move[1])
​
        moves.append('{r}{c}'.format(r = row, c = col))
      for move in above_moves:
​
        row = rows[int(move[0])]
        col = int(move[1])
​
        moves.append('{r}{c}'.format(r = row, c = col))
      
      return moves
  class Knight:
​
    def __init__(self, r, c):
      self.r = r
      self.c = c
    
    def moves(self):
​
      r = self.r
      c = self.c
​
      rows = 'a b c d e f g h'.upper().split()
      rn = -1
​
      for n in range(0, len(rows)):
        row = rows[n]
​
        if row == r:
          rn = n
      
      down_two = None
      down_one = None
      left_two = None
      left_one = None
      up_two = None
      up_one = None
      right_two = None
      right_one = None
​
      if c - 2 <= 0:
        down_two = False
      else:
        down_two = True
      
      if c - 1 <= 0:
        down_one = False
      else:
        down_one = True
      
      if rn - 2 < 0:
        left_two = False
      else:
        left_two = True
      
      if rn - 1 < 0:
        left_one = False
      else:
        left_one = True
      
      if c + 2 > 8:
        up_two = False
      else:
        up_two = True
      
      if c + 1 > 8:
        up_one = False
      else:
        up_one = True
      
      if rn + 2 > 7:
        right_two = False
      else:
        right_two = True
      
      if rn + 1 > 7:
        right_one = False
      else:
        right_one = True
      
      pms = []
      if left_two == True:
        if down_one == True:
          pms.append('{r}{c}'.format(r = rows[rn - 2], c = c - 1))
        if up_one == True:
          pms.append('{r}{c}'.format(r = rows[rn - 2], c = c + 1))
      if down_two == True:
        if left_one == True:
          pms.append('{r}{c}'.format(r = rows[rn - 1], c = c - 2))
        if right_one == True:
          pms.append('{r}{c}'.format(r = rows[rn + 1], c = c + 2))
      if right_two == True:
        if down_one == True:
          pms.append('{r}{c}'.format(r = rows[rn + 2], c = c - 1))
        if up_one == True:
          pms.append('{r}{c}'.format(r = rows[rn + 2], c = c + 1))
      if up_two == True:
        if left_one == True:
          pms.append('{r}{c}'.format(r = rows[rn - 1], c = c + 2))
        if right_one == True:
          pms.append('{r}{c}'.format(r = rows[rn + 1], c = c + 2))
      
      return pms
  class Queen:
​
    def __init__(self, r, c):
      self.r = r
      self.c = c
    
    def moves(self):
      
      r = self.r
      c = self.c
​
      pms = []
​
      for n in range(1, 9):
        if n != c:
          pms.append('{r}{c}'.format(r = r, c = n))
      
      rows = 'a b c d e f g h'.upper().split()
​
      for row in rows:
        if row != r:
          pms.append('{r}{c}'.format(r = row, c = c))
      
      for n in range(0, len(rows)):
        row = rows[n]
​
        if row == r:
          a = n
      
      b = c
      
      below_rows = range(0, a)
      above_rows = range(a, 9)
      
      below_cols = range(1, b)
      above_cols = range(b, 9)
​
      moves = []
​
      below_moves = []
      above_moves = []
​
      for number in range(1, 9):
        if a - number in below_rows:
          if b - number in below_cols:
            below_moves.append([a - number, b - number])
          if b + number in above_cols:
            below_moves.append([a - number, b + number])
        if a + number in above_rows:
          if b + number in above_cols:
            above_moves.append([a + number, b + number])
          if b - number in below_cols:
            above_moves.append([a + number, b - number])
      
      for move in below_moves:
        
        row = rows[int(move[0])]
        col = int(move[1])
​
        moves.append('{r}{c}'.format(r = row, c = col))
      for move in above_moves:
​
        row = rows[int(move[0])]
        col = int(move[1])
​
        moves.append('{r}{c}'.format(r = row, c = col))
      
      for move in moves:
        pms.append(move)
      
      del moves
      return pms
  class King:
​
    def __init__(self, r, c):
      self.r = r
      self.c = c
    
    def moves(self):
​
      r = self.r
      c = self.c
​
      down_blocked = None
      up_blocked = None
      left_blocked = None
      right_blocked = None
​
      if r == 'A':
        left_blocked = True
      else:
        left_blocked = False
      
      if r == 'H':
        right_blocked = True
      else:
        right_blocked = False
      
      if c == 1:
        down_blocked = True
      else:
        down_blocked = False
      
      if c == 8:
        up_blocked = True
      else:
        up_blocked = False
      
      rows = 'a b c d e f g h'.upper().split()
      rn = None
​
      for n in range(0, len(rows)):
        row = rows[n]
​
        if row == r:
          rn = n
      
      possible_rows = [r]
      possible_cols = [c]
​
      if left_blocked == True:
        possible_rows.append(rows[rn + 1])
      elif right_blocked == True:
        possible_rows.append(rows[rn + 1])
      else:
        possible_rows.append(rows[rn - 1])
        possible_rows.append(rows[rn + 1])
​
      if up_blocked == True:
        possible_cols.append(c - 1)
      elif down_blocked == True:
        possible_cols.append(c + 1)
      else:
        possible_cols.append(c - 1)
        possible_cols.append(c + 1)
      
      pms = []
​
      for row in possible_rows:
        for col in possible_cols:
          move = '{r}{c}'.format(r = row, c = col)
          place = '{r}{c}'.format(r = self.r, c = self.c)
          if move != place:
            pms.append(move)
      
      return pms
​
  cl = list(current)
​
  cr = cl[0]
  cc = int(cl[1])
​
  c = None
  #Here I assign the piece to it's class
  if piece == 'Pawn':
    c = Pawn(cr, cc)
  elif piece == 'Rook':
    c = Rook(cr, cc)
  elif piece == 'Bishop':
    c = Bishop(cr, cc)
  elif piece == 'Knight':
    c = Knight(cr, cc)
  elif piece == 'Queen':
    c = Queen(cr, cc)
  elif piece == 'King':
    c = King(cr, cc)
  else:
    return 'Invalid Chess Piece!! ERROR!!'
  
  pmoves = c.moves()#This should provide a list of all valid spaces this particular peice should be able to move to.
​
  if target in pmoves: 
    return True
  else:
    return False

