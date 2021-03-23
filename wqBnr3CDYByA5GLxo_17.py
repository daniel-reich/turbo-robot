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
  a,fork=(txt),[]
  b= re.sub('\[',',',a)
  b=re.sub('\]',',',b)
  lst = [c for c in b.split(',') if c !='']
  for i in range (len(lst)):
    if len(lst[i].split('|'))==1:
      if len(fork) ==0:
        fork.append(lst[i])
      else:
        for j in range (len(fork)):
          fork[j]+=lst[i]
    else:
      if (i==0):
        for j in range (len(lst[i].split('|'))):
          fork.append(lst[i].split('|')[j])
      else:
        comb=lst[i].split('|')
        fork =[''.join((x,y)) for x in fork for y in comb]
  return sorted(fork)

