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
  for let in range(len(txt1)):
    if ord(txt1[let]) > 58: #ASCII table value
      txt1 = txt1.replace(txt1[let], chr(let))
  for let in range(len(txt2)):
    if ord(txt2[let]) > 58: #ASCII table value
      txt2 = txt2.replace(txt2[let], chr(let))
  if txt1 == txt2:
    return True
  return False

