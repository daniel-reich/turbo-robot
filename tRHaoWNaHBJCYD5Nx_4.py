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

def same_letter_pattern(txt1, txt2):
​
  d = {}
​
  if len(txt1) != len(txt2):
    return False
  
  for n in range(0, len(txt1)):
​
    t1l8r = txt1[n]
    t2l8r = txt2[n]
​
    if t1l8r not in d.keys():
      d[t1l8r] = t2l8r
    else:
      v = d[t1l8r]
      if t2l8r != v:
        return False
  
  return True

