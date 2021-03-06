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
    def word_show(word,n):
        return word[:n] + ('_' * (len(word) - n))
    final = []    
    words_list = txt.split()
    max_len = max([len(word) for word in words_list])
    for i in range(0,max_len+1):
        res = ''
        for word in words_list:
            res += word_show(word,i) + ' '
        final.append(res.rstrip())
    return final

