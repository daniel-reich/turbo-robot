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

def overlap(word1, word2):
  common = 0
  for i in range(min(len(word1), len(word2))):
    if word1[-(i+1):] == word2[:i+1]:
      common = i+1
  return common
  
def join(lst):
  least = len(lst[0])
  phrase = lst[0]
  for i in range(len(lst)-1):
    common = overlap(lst[i], lst[i+1])
    phrase += lst[i+1][common:]
    if common < least:
      least = common
  return [phrase, least]

