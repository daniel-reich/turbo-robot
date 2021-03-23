"""


Write a function that takes in a string and returns all possible combinations.
Return the final result in **alphabetical order**.

### Examples

    unravel("a[b|c]") ➞ ["ab", "ac"]
    
    unravel("a[b|c]de[f|g]") ➞ ["abdef", "acdef", "abdeg", "acdeg"]
    
    unravel("a[b]c[d]") ➞ ["abcd"]
    
    unravel("a[b|c|d|e]f") ➞ ["abf", "acf", "adf", "aef"]
    
    unravel("apple [pear|grape]") ➞ ["apple grape", "apple pear"]

### Notes

Think of each element in every block (e.g. `[a|b|c]`) as a **fork in the
road**.

"""

import re
def unravel(txt):
  if not "[" in txt:
    return [txt]
  elif not "|" in txt:
    txt = re.sub(r'\W+',"",txt)
    return [txt]
  else:
    pairs = re.findall(r'\[[^\]]+]',txt)
    for pair in pairs:
      if not "|" in pair:
        txt = txt.replace(pair,pair[1])
    def newlist(lst,pairs):
      newlst = []
      if not pairs:
        return lst
      else:
        chars = re.findall(r'\w+',pairs[0])
        for el in lst:
          for i in range(0,len(chars)):
            newlst.append(el.replace(pairs[0],chars[i]))
        pairs.pop(0)
        return newlist(newlst,pairs)
    return sorted(newlist([txt],pairs))

