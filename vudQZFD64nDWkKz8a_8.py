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
    lst = []
    p_lst = []
    max_len = max([len(x) for x in txt.split(" ")])
    for y in range(max_len + 1):
        if y == 0:
            lst.append("".join(["_" if x != " " else " " for x in txt]))
        else:
            p_lst.append([])
            for z in txt.split(" "):
                p_lst[y-1].append("".join([x if i < y else "_" for i, x in enumerate(z)]))
    for i, x in enumerate(p_lst):
        lst.append(" ".join(x))
    return lst

