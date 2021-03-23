"""


Create a function that converts a string into a matrix of characters that can
be read vertically. Add spaces when characters are missing.

### Examples

    vertical_txt("Holy bananas") ➞ [
      ["H", "b"],
      ["o", "a"],
      ["l", "n"],
      ["y", "a"],
      [" ", "n"],
      [" ", "a"],
      [" ", "s"]
    ]
    
    vertical_txt("Hello fellas") ➞ [
      ["H", "f"],
      ["e", "e"],
      ["l", "l"],
      ["l", "l"],
      ["o", "a"],
      [" ", "s"]
    ]

### Notes

N/A

"""

def vertical_txt(txt):
  
  class Word:
​
    def __init__(self, word, l):
      self.w = word
      self.l = l
    
    def vertical(self):
      arr = []
​
      for l8r in self.w:
        arr.append([l8r])
      
      if len(arr) < self.l:
        for n in range(self.l-len(arr)):
          arr.append([' '])
      
      return arr
  
  words = txt.split(' ')
  #print(words)
  nw = []
  maxl = 0
​
  for word in words:
    if maxl < len(word):
      maxl = len(word)
  
  for word in words:
    nw.append(Word(word,maxl))
  
  verticals = []
​
  for word in nw:
    verticals.append(word.vertical())
 # print(verticals)
  new_arr = []
​
  for n in range(maxl):
    row = []
    for r in range(len(verticals)):
      row += verticals[r][n]
    new_arr.append(row)
  
  return new_arr

