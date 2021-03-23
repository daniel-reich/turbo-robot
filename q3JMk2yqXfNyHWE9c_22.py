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

def double_letters(word):
  for i in word:
    if i + i in word:
      return True
  return False

