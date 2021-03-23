"""


Write a function that connects each previous word to the next word by the
shared letters. Return the resulting string (removing **duplicate characters**
in the overlap) and the **minimum** number of shared letters across all pairs
of strings.

### Examples

    join(["oven", "envier", "erase", "serious"]) ➞ ["ovenvieraserious", 2]
    
    join(["move", "over", "very"]) ➞ ["movery", 3]
    
    join(["to", "ops", "psy", "syllable"]) ➞ ["topsyllable", 1]
    
    # "to" and "ops" share "o" (1)
    # "ops" and "psy" share "ps" (2)
    # "psy" and "syllable" share "sy" (2)
    # the minimum overlap is 1
    
    join(["aaa", "bbb", "ccc", "ddd"]) ➞ ["aaabbbcccddd", 0]

### Notes

More specifically, look at the overlap between the previous words **ending
letters** and the next word's **beginning letters**.

"""

def join(lst):
  word = ''
  count = []
  for i in range(len(lst)-1):
    word+=lst[i]
    if lst[i][-1] in lst[i+1]:
      l = lst[i+1].index(lst[i][-1])
      if lst[i][-l-1:]==lst[i+1][:l+1]: word=word[:-l-1]
      count.append(l+1)
  word += lst[-1]
  return [word,min(count)] if count else [word,0]

