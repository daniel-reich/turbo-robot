"""


Create a function that returns a number which can block the player from
reaching 3 in a row in a game of Tic Tac Toe. The number given as an argument
will correspond to a grid of Tic Tac Toe: topleft is 0, topright is 2,
bottomleft is 6, and bottomright is 8.

  * Create a function that takes two numbers `a`, `b` and returns another number.
  * This number should be the final one in a line to block the player from winning.

### Examples

    block_player(0, 3) ➞ 6
    
    block_player(0, 4) ➞ 8
    
    block_player(3, 5) ➞ 4

### Notes

The values given will always have two filled squares in a line.

"""

def block_player(a, b):
​
  class Tic_Tac_Toe:
    class Space:
    
      def __init__(self, ident, val = None):
        self.id = ident
        self.val = val
      
      def claim(self, player):
        if self.val == None:
          self.val = player
          return True
        else:
          return False
          
    def __init__(self):
​
      self.spaces = {}
      
      for n in range(9):
        self.spaces[n] = Tic_Tac_Toe.Space(n)
      
      self.win_conds = [[0,1,2], [0,3,6], [3,4,5], [1,4,7], [6,7,8], [2,5,8], [0,4,8], [2,4,6]] + [list(reversed(r) for r in [[0,1,2], [0,3,6], [3,4,5], [1,4,7], [6,7,8], [2,5,8], [0,4,8], [2,4,6]])]
      
      self.os = []
      self.xs = []
      
    def move(self, space, player):
      mv = self.spaces[space].claim(player)
      if mv == True:
        if player == 'O':
          self.os.append(space)
        else:
          self.xs.append(space)
      return mv
    
    def block(self, enemy):
      if enemy == 'O':
        win_cond = None
        for cond in self.win_conds:
          count = 0
          for space in cond:
            if self.spaces[space].val == 'O':
              count += 1
          if count == 2:
            win_cond = cond
            break
        if win_cond != None:
          for space in win_cond:
            if self.spaces[space].val == None:
              return space
          return False
        else:
          return win_cond
      else:
        win_cond = None
        for cond in self.win_conds:
          count = 0
          for space in cond:
            if self.spaces[space].val == 'X':
              count += 1
          if count == 2:
            win_cond = cond
            break
        if win_cond != None:
          for space in win_cond:
            if self.spaces[space].val == None:
              return space
          return False
        else:
          return win_cond
  
  board = Tic_Tac_Toe()
  
  board.move(a, 'O')
  board.move(b, 'O')
  
  return board.block('O')

