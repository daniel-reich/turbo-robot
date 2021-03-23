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
  textList = txt.split()
  hint = ''
  hintList = []
  textLen = len(textList)
  hintLvl = 0
  while(hint != txt):
    for i in range(textLen):
      if(i!=0):
        hintList += ' '
      wordLen = len(textList[i])
      for j in range(wordLen):
        if(hintLvl > j):
          hint += '_'
        else:
          hint += textList[i][j]
    hintList.append(hint)
  hintList.append(txt)
  return hintList

