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
    words = txt.split()
    Hint = []
    for i in range(0,len(str(max(words, key=len)))+1):
        Sentence = ""
        for word in words:
            Sentence += word[:i].ljust(len(word),"_") + " "
        Hint.append(Sentence[:len(Sentence)-1])
    
    return Hint

