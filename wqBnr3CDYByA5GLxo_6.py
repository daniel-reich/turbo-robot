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

def unravel(txt):
  if '[' not in txt: return [txt]
  ret = []
  start = txt.index('[')
  end = txt.index(']')
  switches = txt[start+1:end].split('|')
  
  for switch in switches:
    toadd = txt[:start] + switch + txt[end+1:]
    if '[' in toadd:
      for option in unravel(toadd):
        ret.append(option)
    else:
      ret.append(toadd)
  return sorted(ret)

