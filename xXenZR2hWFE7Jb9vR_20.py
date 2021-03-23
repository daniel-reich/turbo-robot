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
  return morph(s) == morph(t)
​
def morph(text):
  result = []
  chars = {}
  cur_val = 0
  for char in text:
    if char not in chars:
      chars[char] = cur_val
      cur_val += 1
    result.append(chars[char])
  return result

