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
    txtlst = txt.split()
    finalst = []
    sublst = []
    maxlength = max([len(word) for word in txtlst])
    for i in range(-1, maxlength):
        for txt in txtlst:
            if i == -1:
                sublst.append('_' * len(txt))
            else:
               sublst.append(txt[0:i+1] + ('_' * (len(txt)-(i+1))))
        finalst.append(" ".join(sublst))
        sublst = []
##        if i == 4:
##            break
    return finalst

