"""


Create a function that takes a list of character inputs from a Tic Tac Toe
game. Inputs will be taken from player1 as `"X"`, player2 as `"O"`, and empty
spaces as `"#"`. The program will return the **winner** or **tie** results.

### Examples

    tic_tac_toe([
      ["X", "O", "O"],
      ["O", "X", "O"],
      ["O", "#", "X"]
    ]) ➞ "Player 1 wins"
    tic_tac_toe([
      ["X", "O", "O"],
      ["O", "X", "O"],
      ["X", "#", "O"]
    ]) ➞ "Player 2 wins"
    tic_tac_toe([
      ["X", "X", "O"],
      ["O", "X", "O"],
      ["X", "O", "#"]
    ]) ➞ "It's a Tie"

### Notes

N/A

"""

def tic_tac_toe(inputs):
  
  class TTT:
    
    def __init__(self, grid):
      
      self.grid = grid
      self.spaces = {}
      
      for r in range(3):
        for c in range(3):
          self.spaces['{},{}'.format(r,c)] = grid[r][c]
      
      self.cols = [[r[n] for r in self.grid] for n in range(3)]
      
      self.diags = [[self.spaces['0,0'], self.spaces['1,1'], self.spaces['2,2']], [self.spaces['2,0'], self.spaces['1,1'], self.spaces['0,2']]]
      
      self.winner = False
      
      for r in self.grid:
        if len(list(set(r))) == 1:
          self.winner = r[0]
      for c in self.cols:
        if len(list(set(c))) == 1:
          self.winner = c[0]
      for d in self.diags:
        if len(list(set(d))) == 1:
          self.winner = d[0]
  
  game = TTT(inputs)
  
  if game.winner == False:
    return 'It\'s a Tie'
  elif game.winner == 'X':
    return 'Player 1 wins'
  else:
    return 'Player 2 wins'

