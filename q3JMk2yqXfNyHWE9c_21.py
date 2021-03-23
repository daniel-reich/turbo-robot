"""


Create a function that takes a word and returns `True` if the word has two
consecutive identical letters.

### Examples

    double_letters("loop") ➞ True
    
    double_letters("yummy") ➞ True
    
    double_letters("orange") ➞ False
    
    double_letters("munchkin") ➞ False

### Notes

N/A

"""

import re
def double_letters(word):
  s=""
  s=re.search(r'((\w)\2)', word)
  if(s == None):
    return False
  else:
    return True

