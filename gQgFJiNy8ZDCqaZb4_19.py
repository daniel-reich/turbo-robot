"""


Given two words, overlap them in such a way, morphing the last few letters of
the first word with the first few letters of the second word. Return the
shortest overlapped word possible.

### Examples

    overlap("sweden", "denmark") ➞ "swedenmark"
    
    overlap("edabit", "iterate") ➞ "edabiterate"
    
    overlap("honey", "milk") ➞ "honeymilk"
    
    overlap("dodge", "dodge") ➞ "dodge"

### Notes

  * All words will be given in lowercase.
  * If no overlap is possible, return both words one after the other (example #3).

"""

def overlap(s1, s2):
​
  class Word:
​
    def __init__(self, word):
      self.w = word
      self.l = list(word)
    
    def possible_overlap(self, other):
​
      possibilities = []
​
      for n in reversed(range(1, len(self.l) + 1)):
        possibilities.append(''.join([str(i) for i in self.l[-n:]]))
      
      valid_pos = []
​
      for possibility in possibilities:
        if possibility in other.w:
          valid_pos.append(possibility)
      
      return valid_pos
    
    def end(self, n):
      return self.w[-n:]
    
    def beg(self, n):
      return self.w[:n]
  
  w1 = Word(s1)
  w2 = Word(s2)
​
  possabilities = w1.possible_overlap(w2)
​
  correct = None
​
  for possability in possabilities:
    w1end = w1.end(len(possability))
    w2beg = w2.beg(len(possability))
​
    if w1end == w2beg:
      correct = possability
      break
  
  if correct == None:
    tr = s1 + s2
  else:
    tr = ''.join([w1.w + w2.w[len(correct):]])
​
  return tr

