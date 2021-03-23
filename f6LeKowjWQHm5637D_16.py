"""


Create a function that moves all capital letters to the front of a word.

### Examples

    cap_to_front("hApPy") ➞ "APhpy"
    
    cap_to_front("moveMENT") ➞ "MENTmove"
    
    cap_to_front("shOrtCAKE") ➞ "OCAKEshrt"

### Notes

Keep the original relative order of the upper and lower case letters the same.

"""

import string
​
def cap_to_front(s):
  s1 = [c for c in s if c in string.ascii_uppercase]
  s2 = [c for c in s if c in string.ascii_lowercase]
  return ''.join(s1 + s2)

