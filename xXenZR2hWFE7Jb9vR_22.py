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

def is_isomorphic(s, t):
  if len(s) != len(t):
    return False
  mapping = {}
  for c1, c2 in zip(s, t):
    if c1 in mapping:
      if c2 != mapping[c1]:
        return False
    else:
      if c2 in mapping.values():
        return False
      mapping[c1] = c2
  return True

