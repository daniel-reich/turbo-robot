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

def all_pos(x):
  return [j for i in x for j in range(len(x)) if i == x[j]]
​
def same_letter_pattern(txt1, txt2):
  return all_pos(txt1) == all_pos(txt2)

