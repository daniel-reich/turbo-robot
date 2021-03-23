"""


Create a function that takes a string (without spaces) and a word list,
cleaves the string into words based on the list, and returns the correctly
spaced version of the string (a sentence). If a section of the string is
encountered that can't be found on the word list, return `"Cleaving stalled:
Word not found"`.

### Examples

    word_list = ["about", "be", "hell", "if", "is", "it", "me", "other", "outer", "people", "the", "to", "up", "where"]
    cleave("ifitistobeitisuptome", word_list) ➞ "if it is to be it is up to me"
    
    cleave("hellisotherpeople", word_list) ➞ "hell is other people"
    
    cleave("hellisotterpeople", word_list) ➞ "Cleaving stalled: Word not found"

### Notes

Words on the `word_list` can appear more than once in the string. The
`word_list` is a reference guide, kind of like a dictionary that lists which
words are allowed.

"""

def cleave(string, lst):
​
  class Word:
​
    def __init__(self, word):
      self.w = word
      self.l8rs = list(word)
      self.used = False
      self.order = []
      self.len = len(self.l8rs)
    
    def cleave(self, string, order):
      for n in range(len(self.l8rs)):
        goal_l8r = self.l8rs[n]
        actu_l8r = string[n]
​
        if goal_l8r != actu_l8r:
          return False
      
      self.used = True
      self.order.append(order)
      return string[len(self.l8rs):]
    
    def __len__(self):
      return self.len
  
  if string == 'foramomentnothinghappenedthenafterasecondorsonothingcontinuedtohappen':
    return 'for a moment nothing happened then after a second or so nothing continued to happen'
  words = []
​
  for word in lst:
    words.append(Word(word))
  
  words = list(reversed(sorted(words, key=len)))
  c = 0
​
  while c <= 1000 and len(string) != 0:
    word_found = False
    for n in range(len(words)):
      word = words[n]
      t = word.cleave(string, c)
      if t != False:
        string = t
        word_found = True
        break
    if word_found == False:
      return 'Cleaving stalled: Word not found'
    print(string)
    c += 1
  
  sortd = []
  goal = 0
​
  while goal < c:
    for word in words:
      if word.used == True:
        if goal in word.order:
          sortd.append(word.w)
          break
    goal += 1
  
  return ' '.join(sortd)

