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
  string = lst[0]
  overlap = []
  for i in range(1, len(lst)):
    check = False
    for x in range(len(lst[i-1])):
      temp = lst[i-1][x:]
      if lst[i].startswith(temp):
        overlap.append(len(temp))
        string += lst[i][len(temp):]
        check = True
        break
    if not check:
      string += lst[i]
  if overlap == []:
    overlap = [0]
  return [string, min(overlap)]

