"""


Given a sentence, return a list of strings which gradually reveals the next
letter in every word at the same time. Use underscores to hide the remaining
letters.

### Examples

    grant_the_hint("Mary Queen of Scots") ➞ [
      "____ _____ __ _____",
      "M___ Q____ o_ S____",
      "Ma__ Qu___ of Sc___",
      "Mar_ Que__ of Sco__",
      "Mary Quee_ of Scot_",
      "Mary Queen of Scots"
    ]
    
    grant_the_hint("The Life of Pi") ➞ [
      "___ ____ __ __",
      "T__ L___ o_ P_",
      "Th_ Li__ of Pi",
      "The Lif_ of Pi",
      "The Life of Pi"
    ]

### Notes

Maintain capitalisation.

"""

def grant_the_hint(txt):
​
  class Secret:
​
    def __init__(self, txt):
      self.t = txt
​
      words = txt.split()
​
      hidden = []
​
      for word in words:
        hide = ''
        for l8r in word:
          hide += '_'
        hidden.append(hide)
      
      self.view = ' '.join(hidden)
      self.index = 0
​
    def hint(self):
​
      if self.t == self.view:
        return True
      
      words = self.view.split()
      act_words = self.t.split()
​
      new_words = []
​
      for n in range(len(words)):
        hid_word = words[n]
        act_word = act_words[n]
​
        new_words.append(act_word[:self.index+1] + hid_word[self.index+1:])
        
      self.index += 1
      self.view = ' '.join(new_words)
      return self.view
​
  message = Secret(txt)
​
  tr = [message.view]
  c = 0
​
  while tr[-1] != True and c < 1000:
    tr.append(message.hint())
    c+=1 
  
  return tr[:-1]

