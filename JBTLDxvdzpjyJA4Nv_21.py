"""


Steve has a string of lowercase characters in range `ascii[["a".."z"]]`. He
wants to reduce the string to its shortest length by doing a series of
operations. In each operation, he selects a pair of adjacent lowercase letters
that match, and he deletes them. For instance, the string **aab** could be
shortened to **b** in one operation.

Steve’s task is to delete as many characters as possible using this method and
print the resulting string. If the final string is empty, return `"Empty
String"`.

### Case

    super_reduced_string("aaabccddd") ➞ "abd"

Explanation:

    "aaabccddd" -> "abccddd" -> "abddd" -> "abd"

### Examples

    super_reduced_string("cccxllyyy") ➞ "cxy"
    
    super_reduced_string("aa") ➞ "Empty String"
    
    super_reduced_string("baab") ➞ "Empty String"
    
    super_reduced_string("fghiiijkllmnnno") ➞ "fghijkmno"
    
    super_reduced_string("chklssstt") ➞ "chkls"

### Notes

N/A

"""

import re
​
def super_reduced_string(txt):
  res = ''
  done = False
  while not done:
    i = 0
    # print(txt, res)
    while True:
      if i > len(txt) - 1:
        break
      if i == len(txt) - 1 or (txt[i] != txt[i+1]):
        res += txt[i]
        i += 1
      else:
        i += 2
    if res == txt:
      done = True
    else:
      txt = res
      res = ''
  if not res:
    res='Empty String'
  return res

