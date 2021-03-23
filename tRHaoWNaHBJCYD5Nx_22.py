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
  p_enum = 0
  tracker_txt1 = {}
  tracker_txt2 = {}
  txt1_list = []
  txt2_list = []
  for i in txt1:
    if i not in tracker_txt1:
      tracker_txt1[i] = p_enum
      p_enum += 1
    txt1_list.append(p_enum)
  p_enum = 0
  for i in txt2:
    if i not in tracker_txt2:
      tracker_txt2[i] = p_enum
      p_enum += 1
    txt2_list.append(p_enum)
  if txt1_list == txt2_list:
    return True
  return False

