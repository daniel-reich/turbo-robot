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
    word_lst = txt.split()
    fin_str = ""
    fin_arr = []
    longest_word = max(word_lst, key=len)
    for i in range(len(longest_word)+1):
        for word in word_lst:
            fin_str += word[:i] + (len(word)-i)*'_' + ' ' if len(word)-i >= 0 else word+' '
        fin_arr.append(fin_str)
        fin_str = ""
​
    return [l.rstrip() for l in fin_arr]

