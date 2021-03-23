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
  
  converter1 = {}
  converter2 = {}
  
  for n in range(len(s)):
    s_char = s[n]
    t_char = t[n]
    
    if s_char not in converter1.keys():
      converter1[s_char] = t_char
    else:
      if converter1[s_char] != t_char:
        return False
    
    if t_char not in converter2.keys():
      converter2[t_char] = s_char
    else:
      if converter2[t_char] != s_char:
        return False
  
  return True

