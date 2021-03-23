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
  print (lst)
  i=1
  res=lst[0]
  min_j = 9999
  while i < len(lst):
    j=0
    w1 = lst[i-1]
    w2 = lst[i]
    while j <= len(w1) and j <= len(w2):
        if w1[len(w1)-j-1] == w2[0]:
          break
        else:
          j+=1
    if j == len(w1)+1 or j == len(w2)+1:
      min_j = -1
      res+= w2
    else:
      if min_j > j:
        min_j = j
      print (j)
      res+= w2[j+1::]
    i+=1
  print (min_j)
  return ([res, min_j+1])

