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
  out, min_overlap,overlap=lst[0],10**9,0
  out=lst[0]
  for i in range (len(lst)-1):
    overlap=0
    for j in range (min(len(lst[i]),len(lst[i+1]))):
      if lst[i][len(lst[i])-1-j:]==lst[i+1][:j+1]:
        overlap=j+1
        if (overlap < min_overlap):
          min_overlap=overlap
    out+=lst[i+1][overlap:]
  if(min_overlap==10**9):
    min_overlap=0
  return [out, min_overlap]

