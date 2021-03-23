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
  split = txt.split()
  maximum = max([len(x) for x in split])
  
  ret = []
  
  for i in range(0, maximum + 1):
    app = ""
    
    for word in split:
      tmp = ""
      for j, char in enumerate(word):
        if j < i:
          tmp += char
        else:
          tmp += '_'
      app += tmp + ' '
    
    ret.append(app[:len(app) - 1])
    
  return ret

