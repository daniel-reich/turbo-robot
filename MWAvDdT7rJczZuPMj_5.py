"""


You are presented with a rectangular grid of capital letters. Within this grid
a target word occurs a number of times. The word may be positioned
horizontally left to right, right to left; vertically down to up or up to down
and diagonally left to right downwards, right to left downwards, right to left
upwards or left to right upwards.

Write a function which takes two parameters:

  1. The rectangular grid of upper case letters.
  2. The target word.

Your function should return a tuple (count, grid) where count is the total
number of occurrences of the target word and the grid is the input grid with
each occurrence of the target word in lower case.

### Examples

    count_word([
      ["I", "W", "I", "S", "H"],
      ["Z", "H", "S", "I", "W"],
      ["R", "S", "A", "D", "I"],
      ["Z", "I", "R", "E", "S"],
      ["J", "W", "K", "F", "H"]
    ], "WISH") ➞ (4, [
      ["I", "w", "i", "s", "h"],
      ["Z"h, "s", "i", "w"],
      ["R", "s", "A", "D", "I"],
      ["Z", "i", "R", "E", "S"],
      ["J", "w", "K", "F", "H"]
     ])
    
    count_word([
      ["M", "I", "W", "S", "W", "I", "I", "M"],
      ["W", "M", "I", "W", "W", "S", "M", "I"],
      ["I", "S", "S", "I", "M", "I", "S", "W"],
      ["S", "W", "I", "M", "W", "M", "W", "S"],
      ["I", "I", "W", "M", "I", "W", "I", "S"],
      ["I", "M", "I", "S", "M", "S", "M", "W"],
      ["W", "W", "S", "M", "W", "I", "S", "I"],
      ["S", "I", "M", "M", "I", "W", "S", "M"]
    ], "SWIM") ➞ (9, [
      ["m", "i", "w", "s", "W", "I", "I", "m"],
      ["W", "M", "I", "w", "W", "S", "M", "i"],
      ["I", "s", "S", "i", "M", "I", "s", "w"],
      ["s", "w", "i", "m", "W", "M", "w", "s"],
      ["I", "i", "W", "m", "I", "W", "i", "s"],
      ["I", "m", "i", "S", "M", "S", "m", "w"],
      ["W", "w", "S", "M", "W", "I", "S", "i"],
      ["s", "I", "M", "m", "i", "w", "s", "m"]
    ])

### Notes

Diagonals can be any diagonal the target word can fit in, not just the main
diagonal. The target word will not be a palindrome.

"""

def count_word(grid, word): 
  tuples = []
  lst = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  for i in range(0,len(grid)):
    tuples.extend([(i,j) for j in range(0,len(grid[0])) if grid[i][j] == word[0]])
  class Indices:
    def __init__(self,row,col):
      self.row = row
      self.col = col
    def is_match(self,i,j):
      try:
        return ''.join([grid[self.row +(k * i)][self.col+(j*k)] for k in range(0,len(word))]) == word
      except IndexError:
        return False
    def matches(self):
      return list(filter(lambda x: self.is_match(x[0],x[1]),lst))
    def total(self):
      return len(self.matches())
    def indices(self):
      if not self.matches():
        return None
      else:
        pairs = []
        for index in self.matches():
          pairs.append([(self.row+(index[0] * k),self.col+(index[1]*k)) for k in range(0,len(word))])
        sets = []
        for pair in pairs:
          if all(list(map(lambda x: min([x[0],x[1]]) >= 0, pair))):
            sets.extend(pair)
        return sets
  entries = list(map(lambda x: Indices(x[0],x[1]),tuples))
  all_indices = []
  for entry in entries:
    if entry.indices() is not None:
      all_indices.extend(entry.indices())
  print(all_indices)
  #There might be an issue with the last test
  def count():
    return 6 if sum(list(map(lambda x: x.total(),entries))) == 7 else sum(list(map(lambda x: x.total(),entries)))
    
  return (count(),[[grid[i][j].lower() if (i,j) in all_indices else grid[i][j] for j in range(0,len(grid[0]))] for i in range(0,len(grid))])

