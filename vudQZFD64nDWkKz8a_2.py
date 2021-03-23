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
    txt = txt.split(' ')
    ans = []
    m = max(len(i) for i in txt)
    for i in txt:
        l = len(i)
        row = ['_'*l]
        ind = 1
        for j in range(len(i)):
            el = i[:ind] + ('_'*(l-ind))
            row.append(el)
            ind+=1
        for j in range(m-l):
            row.append(i)
        ans.append(row)    
    a = []
    for i in range(len(ans[0])):
        bl = []
        for j in range(len(ans)):
            bl.append(ans[j][i])
        a.append(" ".join(bl))  
    return a

