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
  if len(set(txt1))!= len(set(txt2)): return False
  for i in range(len(set(txt1))):
    for j in txt1:
      if j.isalpha():
        txt1 = txt1.replace(j, str(i))
        break
  for i in range(len(set(txt2))):
    for j in txt2:
      if j.isalpha():
        txt2 = txt2.replace(j, str(i))
        break
  return txt1 == txt2

