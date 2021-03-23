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

from itertools import product
def unravel(txt):
  if '[' not in txt:
    return [txt]
  lsts = []
  for i in txt.split('['):
    if ']' in i:
      lsts.append(i.split(']')[0].split('|'))
  combos = []
  for s in product(*lsts):
    combos.append(list(s))
  temp = ''
  switch = False
  for i in txt:
    if i == '[':
      switch = True
    if not switch:
      temp += i
    if i == ']':
      temp += '_'
      switch = False
  txt = temp
  ans = []
  for i in combos:
    temp = ''
    it = 0
    for x in txt:
      if x != '_':
        temp += x
      else:
        temp += i[it]
        it += 1
    ans.append(temp)
  return sorted(ans)

