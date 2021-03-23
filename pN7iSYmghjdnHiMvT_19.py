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

from string import ascii_uppercase
​
char_to_num = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=1)}
​
class Battleship(object):
​
    def __init__(self, scheme, guesses):
        self.scheme = []
        for string in scheme:
            self.scheme.append(str(int(char_to_num[string[0]]) - 1) + str(int(string[1]) - 1))
        self.guesses = []
        for string in guesses:
            self.guesses.append(str(int(char_to_num[string[0]]) - 1) + str(int(string[1]) - 1))
        self.hit_num = 0
        self.point_num = 0
        self.cruisers = []
        self.game_board = [[" "," "," "," "," "],
                           [" "," "," "," "," "],
                           [" "," "," "," "," "],
                           [" "," "," "," "," "],
                           [" "," "," "," "," "]]
        for cord in self.scheme:
            if (cord[0] + str(int(cord[1]) + 1)) in self.scheme:
                self.cruisers.append([cord, cord[0] + str(int(cord[1]) + 1)])
            elif (str(int(cord[0]) + 1) + cord[1]) in self.scheme:
                self.cruisers.append([cord, str(int(cord[0]) + 1) + cord[1]])
​
    def board(self):
        for row in range(0, len(self.game_board)):
            for cell in range(0, len(self.game_board[row])):
                if str(row)+str(cell) in self.scheme:
                    self.game_board[row][cell] = "s"
​
                if str(row)+str(cell) in self.guesses and str(row)+str(cell) in self.scheme:
                    self.game_board[row][cell] = "X"
​
                elif str(row)+str(cell) in self.guesses and not str(row)+str(cell) in self.scheme:
                    self.game_board[row][cell] = "."
​
        return self.game_board
​
    def hits(self):
        for row in self.game_board:
            self.hit_num += row.count("X")
        return self.hit_num
​
    def sunk(self):
        self.cruiser_sunk = 0
        for cruiser in self.cruisers:
            if cruiser[0] in self.guesses and cruiser[1] in self.guesses:
                self.cruiser_sunk += 1
        return self.cruiser_sunk
​
    def points(self):
        return (self.hit_num + (self.cruiser_sunk * 2))

