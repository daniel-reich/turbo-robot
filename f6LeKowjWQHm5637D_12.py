"""


Create a function that moves all capital letters to the front of a word.

### Examples

    cap_to_front("hApPy") ➞ "APhpy"
    
    cap_to_front("moveMENT") ➞ "MENTmove"
    
    cap_to_front("shOrtCAKE") ➞ "OCAKEshrt"

### Notes

Keep the original relative order of the upper and lower case letters the same.

"""

def cap_to_front(s):
  up = ''
  low = ''
  for ch in s:
    if ch.isupper():
      up += ch
    else:
      low += ch
  return up + low

