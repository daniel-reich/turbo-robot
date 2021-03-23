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
  ss = ''
  tt = ''
  for x in s:
    if x not in ss:
      ss += x
  for x in t:
    if x not in tt:
      tt += x
  if len(ss) != len(tt): return False
  return s.translate(str.maketrans(ss, tt)) == t

