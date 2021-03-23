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
    low = txt.split()
    lou = ['_'*len(w) for w in low]
    ans = [' '.join(lou)]
    idx = len(max(low, key=len))
​
    for i in range(idx):
        nxt = []
        for j, w in enumerate(lou):
            if '_' in w:
                nxt.append(w[:i] + low[j][i] + w[i+1:])
            else:
                nxt.append(low[j])
        lou = nxt
        ans.append(' '.join(lou))
    return ans

