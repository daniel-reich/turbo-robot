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
  pattern1 = []
  pattern1_dict = {}
  for char in txt1:
    if char not in pattern1_dict.keys():
      pattern1_dict[char] = len(pattern1_dict.keys())
    
    pattern1.append(pattern1_dict[char])
    
  pattern2 = []
  pattern2_dict = {}
  for char in txt2:
    if char not in pattern2_dict.keys():
      pattern2_dict[char] = len(pattern2_dict.keys())
    
    pattern2.append(pattern2_dict[char])
    
  if pattern1 == pattern2:
    return True
  
  return False

