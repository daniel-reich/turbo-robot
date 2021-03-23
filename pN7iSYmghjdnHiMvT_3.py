"""


In this challenge, you have to build a `class` that will store and manipulate
the data of a simplified clone of **Battleship** , the popular strategy game.

The game is played on a **5x5** square board, with rows indexed by uppercase
letters from **A to E** (from top to bottom), and columns indexed by numbers
from **1 to 5** (from left to right).

### Rules of the Game

  * There are two types of ship: the **Patrol** and the **Cruiser**. The Patrol occupies a single cell, the Cruiser occupies two cells, horizontally or vertically.
  * Three Patrols and three Cruisers will be placed randomly in the grid, **without ships adjacent in rows and columns** (in particular, two adjacent cells can only both be ship cells if they belong to the same Cruiser).
  * The player _calls_ six different cells, trying to guess if there's a Patrol or a Cruiser in it.
  * Hits and misses are recorded on the board. For every hit Patrol or Cruiser, a point is gained, and if a Cruiser is sunk, two additional points are gained.

### Class "Battleship"

Each instance of the Battleship class in the **Tests** tab will be declared
with two parameters:

  * `scheme` is a list containing **9** strings which are the coordinates indicating where the ships are placed on the board.
  * `guesses` is a list containing **6** strings which are the coordinates of the guesses made by the player.

### What do you have to implement?

The **Tests** will expect each instance of the `Battleship` class to possess
four methods:

  * `board()` will return the final state of the board, based on the placement of the ships and the results of the player guesses, as a matrix of size 5x5. To vizually represent the state of the game, you will use four different characters:

    * ' ' = a blank space on the board.
    * 's' = a space occupied by a ship.
    * '.' = a miss (wrong guess).
    * 'X' = a hit (a correct guess).
  * `hits()` will return the **total number of hits** made by the player (correct guesses), either on Patrols or on Cruisers.

  * `sunk()` will return the **total number of sunk** Cruisers (two adjacent correct guesses, either horizontally or vertically).
  * `points()` will return the **total number of points** gained by the player (1 for every hit, plus 2 for every sunk Cruiser).

### Examples

    scheme = ["A1", "C1", "B2", "B3", "D2", "E2", "E4", "E5", "A5"]
    
    guesses = ["A1", "B2", "C3", "D4", "E5", "E4"]
    
    battleship.board() ➞ [
      [X,  ,  ,  , s],
      [ , X, s,  ,  ],
      [s,  , .,  ,  ],
      [ , s,  , .,  ],
      [ , s,  , X, X]
    ]
    
    battleship.hits() ➞ 4
    # Total hits.
    
    battleship.sunk() ➞ 1
    # Sunk Cruisers only, sunk Patrols not included.
    
    battleship.points() ➞ 6
    # Hits + additional points given by sunk Cruisers.

### Notes

  * If two cruisers are in the same row or the same column, there will be a blank cell between them, so that it will be possible to distinguish them as different ships.
  * The board **is not** given, you have to build it.
  * In the **Examples** above, the symbols in the board are not between quotation marks for readability, but they are strings.

"""

# CHARACTER SET
# " " -> empty
# "s" -> ship
# "." -> miss
# "X" -> hit
​
class Battleship:
  #Rules
  #2 Types of Ships: Patrol or Cruiser
    #Patrol = 1 Spot
    #Cruiser = 2 Spots H/V
  #3 Patrols 3 Cruisers randomly on Board 
  #Player calls 6 guesses
  #For hit, player gets 1 point, for cruiser sunk, player gets 2 extra points
  
  def __init__(self, scheme, guesses):
    self.scheme = scheme
    self.guesses = guesses
​
    spaces = []
​
    for l8r in sorted(list('ABCDE')):
      for num in range(1, 6):
        spaces.append('{}{}'.format(l8r,num))
    
    self.spaces = {}
    self.hitts = 0
    for space in spaces:
      if space in self.scheme:
        if space in self.guesses:
          self.spaces[space] = 'X'
          self.hitts += 1
        else:
          self.spaces[space] = 's'
      else:
        if space in self.guesses:
          self.spaces[space] = '.'
        else:
          self.spaces[space] = ' '
    
    self.cruisers = []
    already_found = []
    self.score = self.hitts 
​
    for guess in self.guesses:
      print(guess)
      if guess in already_found:
        #print(guess)
        continue
      elif self.spaces[guess] == '.' or self.spaces[guess] == ' ':
        continue
      else:
        if l8r == 'D':
          print ('LHLjd')
        possible_next = []
        l8rs = 'ABCDE'
        nums = [str(i) for i in range(1, 6)]
​
        l8r = guess[0]
        num = guess[1]
​
        if l8r == 'A':
          poss_l8rs = ['B']
        elif l8r == 'E':
          poss_l8rs = ['D']
        else:
          index = None
          for n in range(len(l8rs)):
            tl8r = l8rs[n]
            if tl8r == l8r:
              index = n
              break
          poss_l8rs = [l8rs[n-1], l8rs[n+1]]
      
        if num == '1':
          poss_nums = ['2']
        elif num == '5':
          poss_nums = ['4']
        else:
          poss_nums = [str(int(num) - 1), str(int(num) + 1)]
      
        for pl8r in poss_l8rs:
          possible_next.append('{}{}'.format(pl8r, num))
        for pnum in poss_nums:
          possible_next.append('{}{}'.format(l8r, pnum))
        if l8r == 'D':
          print(guess, possible_next, 'hi')
        #print(guess, possible_next)
        for spot in possible_next:
          if spot in already_found:
            continue
          elif self.spaces[spot] == 'X':
            self.cruisers.append(False)
            already_found.append(spot)
            already_found.append(guess)
            print(guess, spot, False)
          elif self.spaces[spot] == 's':
            self.cruisers.append(True)
            already_found.append(spot)
            already_found.append(guess)
            print(guess, spot, True)
    
    for cruiser in self.cruisers:
      if cruiser == False:
        self.score += 2
​
  def board(self):
​
    l8rs = 'ABCDE'
    nums = [str(i) for i in range(1,6)]
​
    brd = []
​
    for l8r in l8rs:
      row = []
      for num in nums:
        row.append(self.spaces['{}{}'.format(l8r, num)])
      brd.append(row)
    
    return brd
  
  def hits(self):
    return self.hitts
    
  def sunk(self):
    return len([s for s in self.cruisers if s == False])
  
  def points(self):
    return self.score

