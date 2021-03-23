"""


Create a function that returns `True` if two strings share the same letter
pattern, and `False` otherwise.

### Examples

    same_letter_pattern("ABAB", "CDCD") ➞ True
    
    same_letter_pattern("ABCBA", "BCDCB") ➞ True
    
    same_letter_pattern("FFGG", "CDCD") ➞ False
    
    same_letter_pattern("FFFF", "ABCD") ➞ False

### Notes

N/A

"""

def get_pattern(txt):
  c, patt, codes = 0, [], {}
  for k in txt:
    if not k in codes:
      codes[k] = c
      c += 1
    patt.append(codes[k])
  return patt
​
def same_letter_pattern(txt1, txt2):
  return get_pattern(txt1) == get_pattern(txt2)

