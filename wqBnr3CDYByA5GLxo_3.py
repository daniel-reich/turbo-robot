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

import string 
​
ans = []
​
def Solve(s, comb): 
  if len(s) == 0:
    ans.append(comb)
    return
  
  sub = ''  
  i = 0
  
  while i < len(s):
    if s[i] == '[' or s[i] == ']':      
      break
    if s[i].isalpha() or s[i].isdigit() or s[i] in string.punctuation + ' ':
      sub += s[i]           
    i += 1
  s = s[i + 1:]
  
  if '|' in sub:
    for i in sub.split('|'):
      Solve(s, comb + i)
  else:
    Solve(s, comb + sub)
  
    
      
    
    
def unravel(s):
  global ans
  ans = []
  
  Solve(s, '')
  mn = min(len(x) for x in ans)
  
  print(s)
  print(ans)
  
  return sorted(ans)

