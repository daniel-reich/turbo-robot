"""


Create a function that, given a phrase and a number of letters guessed,
returns a string with hyphens `-` for every letter of the phrase not guessed,
and each letter guessed in place.

### Examples

    hangman("helicopter", ["o", "e", "s"]) ➞ "-e---o--e-"
    
    hangman("tree", ["r", "t", "e"]) ➞ "tree"
    
    hangman("Python rules", ["a", "n", "p", "r", "z"]) ➞ "P----n r----"
    
    hangman("He"s a very naughty boy!", ["e", "a", "y"]) ➞ "-e"- a -e-y -a----y --y!"

### Notes

  * The letters are always given in lowercase, but they should be returned in the same case as in the original phrase (see example #3).
  * All characters other than letters should always be returned (see example #4).

"""

def hangman(phrase, lst):
​
  class Hangman:
​
    def __init__(self, phrase):
      self.phrase = phrase
      words = phrase.split()
      self.shown = list(' '.join(['-' * len(w) for w in words]))
​
      for item in self.phrase:
        if item in '0123456789.!':
          self.shown[self.phrase.index(item)] = item
    
    def guess(self, l8r):
​
      indexes = []
​
      if l8r.lower() in self.phrase or l8r.upper() in self.phrase:
        for n in range(len(self.phrase)):
          if self.phrase[n] == l8r.lower() or self.phrase[n] == l8r.upper():
            indexes.append(n)
      
      for index in indexes:
        self.shown[index] = self.phrase[index]
      
      return True
  
  game1 = Hangman(phrase)
​
  for guess in lst:
    game1.guess(guess)
  
  return ''.join(game1.shown)

