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

from itertools import repeat
def grant_the_hint(txt):
    txt = txt.split(" ")
    txt_len = len(txt)
    holder,final = [], []
    longest = len(max(txt, key = len))
    counter = 0
    while txt:
        elem = txt.pop(0)
        holder.append(elem)
        holder.extend(repeat(elem, longest - len(elem)))
        for char in elem[::-1]:
            k = elem.rfind(char)
            elem = elem[:k] + ("_" * (len(elem) - len(elem[:k])))
            holder.append(elem)
    step = int(len(holder) / txt_len)
    while counter < step:
        final.append(" ".join([holder[x] for x in range(counter, len(holder), step)]))
        counter += 1
    return final[::-1]

