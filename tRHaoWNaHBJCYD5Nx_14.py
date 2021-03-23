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
  if len(txt1) != len(txt2): return False
  used1 = []
  used2 = []
  txt1 = list(txt1)
  txt2 = list(txt2)
  for i in range(len(txt1)):
    if txt1[i] not in used1:
      used1.append(txt1[i])
    txt1[i] = str(used1.index(txt1[i]))
    if txt2[i] not in used2:
      used2.append(txt2[i])
    txt2[i] = str(used2.index(txt2[i]))
  txt1 = ''.join(txt1)
  txt2 = ''.join(txt2)
  print(txt1,txt2)
  return txt1 == txt2

