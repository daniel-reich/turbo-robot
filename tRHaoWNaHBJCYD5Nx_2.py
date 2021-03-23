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
  if (len(txt1) != len(txt2)):
    return False;
    
  dict1 = dict();
  for i, letter in enumerate(txt1):
    if letter in dict1:
      if (dict1[letter] != txt2[i]):
        return False;
    else:
      dict1[letter] = txt2[i];
      
  return True;

