"""


Given two strings `s` and `t`, create a function to determine if they are
isomorphic. Two strings are isomorphic if the characters in `s` can be
replaced to get `t`. All occurrences of a character must be replaced with
another character while preserving the order of characters. No two characters
may map to the same character but a character may map to itself.

### Examples

    is_isomorphic("egg", "add") ➞ True
    
    is_isomorphic("aba", "baa") ➞ False
    
    is_isomorphic("paper", "title") ➞ True

### Notes

N/A

"""

def pattern(w):
  res,dic,x = [],{},0
  for c in w:
    if c not in dic:
      dic[c] = x
      x += 1      
    res.append(dic[c])
  return res
      
def is_isomorphic(s, t):
  return pattern(s) == pattern(t)

